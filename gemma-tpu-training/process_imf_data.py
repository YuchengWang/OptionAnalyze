import fitz  # PyMuPDF
import json
import os
import re
import pandas as pd
import requests
from tqdm import tqdm

def semantic_cleanup(text):
    """Removes noise and normalizes spacing."""
    text = re.sub(r'Page \d+ of \d+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def detect_section(text):
    """Heuristically identifies the document section."""
    if re.search(r'EXECUTIVE SUMMARY', text, re.I): return "Executive Summary"
    if re.search(r'CHAPTER \d+', text, re.I): return "Main Analysis Chapter"
    if re.search(r'STATISTICAL APPENDIX|TABLES', text, re.I): return "Statistical Data"
    if re.search(r'POLICY|RECOMMENDATIONS', text, re.I): return "Policy Framework"
    return "General Macroeconomic Context"

def pdf_to_refined_jsonl(pdf_path, output_jsonl):
    """
    Splits PDF into granular semantic chunks. 
    Extracts tables as high-quality independent training examples.
    """
    print(f"🔬 Refining data extraction for: {pdf_path}...")
    doc = fitz.open(pdf_path)
    dataset = []

    for page_num in tqdm(range(len(doc))):
        page = doc[page_num]
        raw_text = page.get_text("text")
        section = detect_section(raw_text)
        
        # Split page into paragraphs
        paragraphs = [p.strip() for p in raw_text.split('\n\n') if len(p.strip()) > 120]
        
        # --- A. Extract and process tables independently ---
        tables_found = []
        try:
            tabs = page.find_tables()
            for i, tab in enumerate(tabs):
                df = tab.to_pandas()
                if not df.empty:
                    table_md = df.to_markdown(index=False)
                    tables_found.append(table_md)
                    
                    # Create a dedicated entry for the table itself (Higher weight on facts)
                    entry = {
                        "instruction": f"Extract and analyze key macroeconomic data from Table {i+1} on Page {page_num + 1} ({section}).",
                        "input": f"Source: {section}, Page {page_num + 1}",
                        "output": f"### IMF Data Table {i+1} Analysis\n\n{table_md}\n\nTechnical Insight: This table provides core statistical evidence for the {section}."
                    }
                    dataset.append(entry)
        except Exception:
            pass

        # --- B. Process text paragraphs ---
        for idx, p_text in enumerate(paragraphs):
            clean_p = semantic_cleanup(p_text)
            
            # Attach the first table of the page as context if it exists (heuristic)
            context_table = f"\n\n[Reference Data]:\n{tables_found[0]}" if tables_found else ""
            
            entry = {
                "instruction": f"Analyze technical details regarding '{section}' from Page {page_num + 1}, paragraph {idx+1}.",
                "input": f"Section: {section}",
                "output": f"### {section} Technical Analysis\n\n{clean_p}{context_table}"
            }
            dataset.append(entry)

    with open(output_jsonl, "w", encoding="utf-8") as f:
        for entry in dataset:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"✅ Refined dataset generated: {len(dataset)} semantic chunks.")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_file = os.path.join(output_dir, "imf_weo_2024.pdf")
    output_file = os.path.join(output_dir, "imf_train.jsonl")
    
    if not os.path.exists(pdf_file):
        url = "https://www.imf.org/-/media/Files/Publications/WEO/2024/October/English/text.pdf"
        print(f"📡 Downloading IMF WEO 2024 PDF from: {url}...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(pdf_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("✅ Download complete.")
        else:
            print(f"❌ Failed to download PDF. Status code: {response.status_code}")
            exit(1)

    if os.path.exists(pdf_file):
        pdf_to_refined_jsonl(pdf_file, output_file)
    else:
        print(f"❌ Error: PDF not found at {pdf_file}")

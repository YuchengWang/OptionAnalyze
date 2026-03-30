# Source: https://www.imf.org/-/media/Files/Publications/WEO/2024/October/English/text.pdf
import fitz  # PyMuPDF
import json
import os
import re
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
    Splits PDF into granular semantic chunks for higher query precision.
    Outputs raw content pairs for the trainer to wrap in templates.
    """
    print(f"🔬 Refining data extraction for: {pdf_path}...")
    doc = fitz.open(pdf_path)
    dataset = []

    for page_num in tqdm(range(len(doc))):
        page = doc[page_num]
        raw_text = page.get_text("text")
        section = detect_section(raw_text)
        
        # Split page into paragraphs to avoid diluting knowledge
        paragraphs = [p.strip() for p in raw_text.split('\n\n') if len(p.strip()) > 150]
        
        # Extract tables as high-priority data
        table_md = ""
        try:
            tabs = page.find_tables()
            for i, tab in enumerate(tabs):
                df = tab.to_pandas()
                table_md += f"\n\n[Data Table {i+1}]\n{df.to_markdown(index=False)}\n"
        except: pass

        for idx, p_text in enumerate(paragraphs):
            clean_p = semantic_cleanup(p_text)
            
            # CONSISTENCY FIX: Output raw fields. The Trainer will apply the System Persona.
            entry = {
                "instruction": f"Analyze technical details regarding '{section}' from Page {page_num + 1}, paragraph {idx+1}.",
                "input": f"Section: {section}",
                "output": f"### {section} Technical Analysis\n\n{clean_p}\n{table_md}"
            }
            dataset.append(entry)

    with open(output_jsonl, "w", encoding="utf-8") as f:
        for entry in dataset:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"✅ Refined dataset generated: {len(dataset)} semantic chunks.")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "outputs")
    pdf_file = os.path.join(output_dir, "imf_weo_2024.pdf")
    output_file = os.path.join(output_dir, "imf_train.jsonl")
    if os.path.exists(pdf_file):
        pdf_to_refined_jsonl(pdf_file, output_file)
    else:
        print(f"❌ Error: PDF not found at {pdf_file}")

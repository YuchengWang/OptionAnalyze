import fitz  # PyMuPDF
import json
import os
from tqdm import tqdm

def pdf_to_high_quality_jsonl(pdf_path, output_jsonl):
    print(f"🧐 Processing {pdf_path} with table preservation...")
    doc = fitz.open(pdf_path)
    dataset = []

    for page_num in tqdm(range(len(doc))):
        page = doc[page_num]
        
        # 1. Extract text normally
        text_content = page.get_text("text").strip()
        
        # 2. Extract tables and convert to Markdown
        table_md = ""
        try:
            tabs = page.find_tables()
            for i, tab in enumerate(tabs):
                df = tab.to_pandas()
                # Convert dataframe to markdown string
                md = df.to_markdown(index=False)
                table_md += f"\n\n### Table {i+1} on Page {page_num+1}\n{md}\n"
        except Exception:
            # Fallback if find_tables is not supported in this version
            pass

        full_page_content = f"{text_content}\n{table_md}".strip()
        
        if len(full_page_content) < 50: # Skip empty/low-info pages
            continue

        # Construct a high-quality training entry
        # GOAL: Pure Knowledge Injection. The output is the TRUE content.
        entry = {
            "instruction": f"Provide the official content and data from the IMF World Economic Outlook 2024, Page {page_num + 1}.",
            "input": f"Reference: IMF WEO 2024 Report.",
            "output": f"On Page {page_num + 1} of the IMF World Economic Outlook (October 2024), the following information is documented:\n\n{full_page_content}\n\n[End of Page {page_num + 1}]"
        }
        dataset.append(entry)

    with open(output_jsonl, "w", encoding="utf-8") as f:
        for entry in dataset:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"✅ Created {len(dataset)} high-quality entries in {output_jsonl}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "outputs")
    os.makedirs(output_dir, exist_ok=True)
    pdf_file = os.path.join(output_dir, "imf_weo_2024.pdf")
    output_file = os.path.join(output_dir, "imf_train.jsonl")
    if os.path.exists(pdf_file):
        pdf_to_high_quality_jsonl(pdf_file, output_file)
    else:
        print(f"❌ Error: {pdf_file} not found.")

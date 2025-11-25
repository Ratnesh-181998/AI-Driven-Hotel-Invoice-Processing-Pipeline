import pathlib
import pandas as pd
import json

ROOT = pathlib.Path(__file__).parent

# ---------- Master CSV ----------
csv_files = list((ROOT / "output_all").rglob("line_items.csv"))
if not csv_files:
    print("WARNING: No line_items.csv files found.")
else:
    dfs = []
    for f in csv_files:
        try:
            df = pd.read_csv(f)
            if not df.empty:
                df['source_image'] = f.parent.name
                dfs.append(df)
        except pd.errors.EmptyDataError:
            print(f"WARNING: Skipping empty file: {f}")
            continue
    df_all = pd.concat(dfs, ignore_index=True)
    master_csv_path = ROOT / "master_line_items.csv"
    df_all.to_csv(master_csv_path, index=False)
    print(f"SUCCESS: Master CSV created: {master_csv_path}")
    print(f"   Total line items: {len(df_all)}")

# ---------- All summaries JSON ----------
json_files = list((ROOT / "output_all").rglob("summary.json"))
summaries = []
for f in json_files:
    with open(f, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        # add source image folder name for traceability
        data["source_image"] = f.parent.name
        summaries.append(data)

if summaries:
    master_json_path = ROOT / "all_summaries.json"
    with open(master_json_path, "w", encoding="utf-8") as out:
        json.dump(summaries, out, indent=2)
    print(f"SUCCESS: All summaries JSON created: {master_json_path}")
    print(f"   Total invoices: {len(summaries)}")
else:
    print("WARNING: No summary.json files found.")

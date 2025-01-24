import json
import pandas as pd
from datetime import datetime
from data_extractors import extract_snapshot, extract_dim_covered_entity, extract_fact_contract_pharmacies

input_file = '/Users/joel/Downloads/OPA_CE_DAILY_PUBLIC.JSON'
snapshot_date = datetime.now().strftime('%Y-%m-%d')
output_folder = '/Users/joel/Code/andhealthdemo/raw_data/'

with open(input_file, 'r') as f:
    raw_data = json.load(f)

outputs = {
    "covered_entity_snapshot": extract_snapshot,
    "dim_covered_entity": extract_dim_covered_entity,
    "fact_contract_pharmacies": extract_fact_contract_pharmacies,
}

for file_name, extractor in outputs.items():
    data = extractor(raw_data, snapshot_date)
    df = pd.DataFrame(data)
    output_file = f"{output_folder}{file_name}_{snapshot_date}.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved {file_name} to {output_file}")
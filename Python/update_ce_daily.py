import time
from datetime import datetime
from get_covered_entity_daily import get_covered_entity_daily
from wait_for_download import wait_for_download
from unzip import unzip_latest_file
import generate_outputs
from convert_json_to_csv import convert_json_to_csv
snapshot_date = datetime.now().strftime('%y-%m-%d')
download_dir = "/Users/joel/Downloads"
input_file = '/Users/joel/Downloads/OPA_CE_DAILY_PUBLIC.JSON'

def main():

    get_covered_entity_daily(download_dir, snapshot_date)
    if not wait_for_download(download_dir, timeout=60):
        time.sleep(1)
        return
    file_path = unzip_latest_file(download_dir, snapshot_date)
    generate_outputs(input_file, snapshot_date, download_dir)


if __name__ == "__main__":
    main()
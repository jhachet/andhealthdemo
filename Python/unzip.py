import os
import zipfile
def unzip_latest_file(download_dir, snapshot_date):
    downloaded_files = [f for f in os.listdir(download_dir) if f.lower().endswith(".zip")]
    downloaded_files.sort(key=lambda f: os.path.getmtime(os.path.join(download_dir, f)), reverse=True)
    latest_zip = os.path.join(download_dir, downloaded_files[0])
    print(f"Latest downloaded file: {latest_zip}")

    with zipfile.ZipFile(latest_zip, 'r') as zip_ref:
        extract_path = download_dir
        zip_ref.extractall(extract_path)
        extracted_files = zip_ref.namelist()
    json_files = [os.path.join(extract_path, f) for f in extracted_files if f.lower().endswith(".json")]
    if not json_files:
        raise ValueError("No JSON files found in the extracted ZIP file.")
    return json_files[0]

import os
import gdown

def download_historical_transactions():
    """Download the historical transactions data from Google Drive."""
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Google Drive file ID (replace with your actual file ID)
    file_id_1 = '17vdzL-ySufrhLKD_33ZJqW1qwub9irQx'
    file_id_2 = '1ycEY63B6yuB3Ofq9jTqIZQde57prpHIQ'
    output_1 = 'data/historical_transactions.csv'
    output_2 = 'data/new_merchant_transactions.csv'
    
    # Check and download historical_transactions.csv
    if os.path.exists(output_1):
        print(f"{output_1} already exists. Skipping download.")
    else:
        print("Downloading historical transactions data...")
        gdown.download(f'https://drive.google.com/uc?id={file_id_1}', output_1, quiet=False)
    
    # Check and download new_merchant_transactions.csv
    if os.path.exists(output_2):
        print(f"{output_2} already exists. Skipping download.")
    else:
        print("Downloading new merchant transactions data...")
        gdown.download(f'https://drive.google.com/uc?id={file_id_2}', output_2, quiet=False)
    print("Download complete!")

if __name__ == "__main__":
    download_historical_transactions() 
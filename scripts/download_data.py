import os
import gdown

def download_historical_transactions():
    """Download the historical transactions data from Google Drive."""
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Google Drive file ID (replace with your actual file ID)
    file_id = '17vdzL-ySufrhLKD_33ZJqW1qwub9irQx'
    output = 'data/historical_transactions.csv'
    
    print("Downloading historical transactions data...")
    gdown.download(f'https://drive.google.com/uc?id={file_id}', output, quiet=False)
    print("Download complete!")

if __name__ == "__main__":
    download_historical_transactions() 
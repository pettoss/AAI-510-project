# Credit Card Loyalty Score Prediction

This project analyzes credit card transaction data to predict customer loyalty scores.

## Data Files

The following data files are required for the project:

- `data/train.csv`: Training data with loyalty scores
- `data/test.csv`: Test data for predictions
- `data/historical_transactions.csv`: Historical transaction data (large file)
- `data/new_merchant_transactions.csv`: New merchant transaction data (large file)

### Historical Transactions Data

The `historical_transactions.csv` file is too large to be stored in this repository. It contains the following columns:
- card_id: Unique identifier for each card
- purchase_amount: Amount of each transaction
- purchase_date: Date and time of the transaction
- merchant_id: Identifier for the merchant
- merchant_category_id: Category of the merchant
- authorized_flag: Whether the transaction was authorized
- city_id: City where the transaction occurred
- state_id: State where the transaction occurred
- category_1, category_2, category_3: Transaction categories
- installments: Number of installments
- month_lag: Month lag of the purchase
- subsector_id: Subsector of the merchant

### Downloading the Data

The historical and new merchant transactions data are stored on Google Drive. The download script will **skip downloading any file that already exists** in the `data/` directory.

1. Install the required package:
   ```bash
   pip install gdown
   ```

2. Run the download script:
   ```bash
   python scripts/download_data.py
   ```
   This will download both `historical_transactions.csv` and `new_merchant_transactions.csv` if they are not already present in the `data/` directory.

## Setup

1. Clone this repository
2. Obtain the required data files
3. Install the required Python packages:
   ```bash
   pip install pandas numpy matplotlib seaborn gdown
   ```

## Project Structure

- `analysis.ipynb`: Jupyter notebook containing the data analysis
- `data/`: Directory containing the data files
- `scripts/`: Directory containing utility scripts
  - `download_data.py`: Script to download the historical and new merchant transactions data (skips files that already exist)
- `*.py`: Python scripts for data processing and analysis
# Credit Card Loyalty Score Prediction

This project analyzes credit card transaction data to predict customer loyalty scores.

## Data Files

The following data files are required for the project:

- `data/train.csv`: Training data with loyalty scores
- `data/test.csv`: Test data for predictions
- `data/historical_transactions.csv`: Historical transaction data (large file)

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

The historical transactions data is stored on Google Drive. To download it:

1. Install the required package:
   ```bash
   pip install gdown
   ```

2. Run the download script:
   ```bash
   python scripts/download_data.py
   ```

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
  - `download_data.py`: Script to download the historical transactions data
- `*.py`: Python scripts for data processing and analysis
import pandas as pd
from tqdm import tqdm

def remove_specific_tickers(csv_file_path, output_file_path):
    # List of stock tickers to be removed
    tickers_to_remove = ['AJISF', 'ITRN', 'TNXP', 'TOPS', 'APB', 'BJZ', 'BLH', 'BNJ', 'BPK', 'GCH',
                         'GRR', 'ICB', 'JE', 'KS', 'KST', 'KYE', 'MZF', 'SGF', 'KACPF', 'RSNHF']

    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Filter out rows with the specified tickers
    # tqdm is used here to show progress on large datasets
    filtered_df = pd.DataFrame(tqdm([row for _, row in df.iterrows() if row['Ticker'] not in tickers_to_remove],
                                    total=len(df), desc="Processing"))

    # Write the filtered data to a new CSV file
    filtered_df.to_csv(output_file_path, index=False)
    print(f"Data exported to {output_file_path}")

# Example usage
remove_specific_tickers('../cleaned_data.csv', 'FixedMe.csv')

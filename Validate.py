import pandas as pd
from tqdm import tqdm

def scan_and_export_unusual_data(csv_file_path, output_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Count unique stock tickers in the entire dataset
    total_unique_tickers = df['Ticker'].nunique()
    print(f"Number of unique stock tickers: {total_unique_tickers}")

    # Define conditions for unusual data
    conditions = (
        df.isnull().any(axis=1) |  # Missing data
        (df.select_dtypes(include=[float, int]) < 0).any(axis=1) |  # Negative numbers
        (df['Volume'] > 2e9) |  # Volume greater than 2 billion
        (df['High'] > 7e5) |  # High greater than 700,000
        (df['Close'] > 470000) |  # Close greater than 470,000
        (df['Adjusted Close'] > 700000)  # Adjusted Close greater than 470,000
    )

    # Filter for rows with unusual data
    unusual_data = df[conditions]

    # Get unique tickers with unusual data
    unique_tickers_unusual_data = unusual_data['Ticker'].unique()
    print(f"Number of stocks with unusual data: {len(unique_tickers_unusual_data)}")
    print(f"Percentage of stocks with unusual data: {(len(unique_tickers_unusual_data) / total_unique_tickers) * 100:.2f}%")

    # Print the list of stock tickers with unusual data
    print("Stock tickers with unusual data:")
    for ticker in unique_tickers_unusual_data:
        print(ticker)

    # Group by 'Ticker' and sort within each group by 'Date'
    grouped = unusual_data.groupby('Ticker')
    sorted_grouped = {ticker: group.sort_values(by='Date') for ticker, group in tqdm(grouped)}

    # Concatenate the sorted groups and write to a new CSV file
    final_df = pd.concat(sorted_grouped.values())
    final_df.to_csv(output_file_path, index=False)

    print(f"Unusual data exported to {output_file_path}")

# Example usage
scan_and_export_unusual_data('./Aggregate.csv', 'Weird.csv')

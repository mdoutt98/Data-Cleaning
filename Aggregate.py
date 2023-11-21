import os
import pandas as pd
from tqdm import tqdm

def aggregate_stock_data(root_folder):
    all_data = []  # List to store individual DataFrames

    with tqdm(total=len(os.listdir(root_folder)), desc="Files") as file_pbar:
        for file in os.listdir(root_folder):
            # Check if the file is a CSV
            if file.endswith('.csv'):
                file_path = os.path.join(root_folder, file)
                try:
                    # Read the CSV file
                    data = pd.read_csv(file_path)

                    # Assuming the date column is named 'Date'
                    # Filter data to keep only the last 10 years
                    data['Date'] = pd.to_datetime(data['Date'])
                    ten_years_ago = pd.Timestamp.now() - pd.DateOffset(years=10)
                    data = data[data['Date'] >= ten_years_ago]

                    all_data.append(data)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

            file_pbar.update(1)  # Update file progress bar

    # Concatenate all DataFrames in the list
    if all_data:
        aggregated_data = pd.concat(all_data, ignore_index=True)

        # Sort the DataFrame by 'Ticker' and 'Date'
        sorted_data = aggregated_data.sort_values(by=['Ticker', 'Date'])

        # Save the sorted data to a new CSV file
        sorted_data.to_csv('aggregate_sorted.csv', index=False)

        print("Data aggregated and sorted successfully.")
    else:
        aggregated_data = pd.DataFrame()  # Return an empty DataFrame if no data was aggregated

    return aggregated_data

root_folder = r"C:\Users\Matt\PycharmProjects\pythonProject\Clean"  # Replace with your root directory

# Aggregate the data and save it sorted
aggregated_stock_data = aggregate_stock_data(root_folder)

# Displaying the first few rows of the aggregated data for verification
print(aggregated_stock_data.head())

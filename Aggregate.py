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
                    all_data.append(data)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

            file_pbar.update(1)  # Update file progress bar

    # Concatenate all DataFrames in the list
    if all_data:
        aggregated_data = pd.concat(all_data, ignore_index=True)
    else:
        aggregated_data = pd.DataFrame()  # Return an empty DataFrame if no data was aggregated

    return aggregated_data

root_folder = r"C:\Users\Matt\PycharmProjects\pythonProject\Clean"  # Replace with your root directory

# Aggregate the data
aggregated_stock_data = aggregate_stock_data(root_folder)

# Displaying the first few rows of the aggregated data for verification
print(aggregated_stock_data.head())

# Save the aggregated data to a new CSV file
aggregated_stock_data.to_csv('Aggregate.csv', index=False)

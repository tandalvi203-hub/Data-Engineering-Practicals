import pandas as pd
import requests


def extract_api_data(url):
    """Fetches data from a REST API and returns a DataFrame."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Normalizing JSON data into a flat table
        return pd.json_normalize(data)
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return pd.DataFrame()


def extract_csv_data(file_path):
    """Reads a flat CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"File Error: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    # 1. API Extraction
    api_url = "https://jsonplaceholder.typicode.com/users"
    api_df = extract_api_data(api_url)
    api_df = api_df[["id", "name", "email", "company.name"]]
    api_df.rename(columns={"company.name": "company"}, inplace=True)

    # 2. Flat File Extraction (Mock CSV Data)
    # Assume 'locations.csv' has columns: id, city, country
    csv_file = "locations.csv"

    # Creating a dummy file for the lab test run
    pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "city": [
                "New York",
                "London",
                "Paris",
                "Tokyo",
                "Berlin",
                "Delhi",
                "Sydney",
                "Moscow",
                "Cairo",
                "Beijing",
            ],
        }
    ).to_csv(csv_file, index=False)

    csv_df = extract_csv_data(csv_file)

    # 3. Data Transformation & Merging
    if not api_df.empty and not csv_df.empty:
        merged_df = pd.merge(api_df, csv_df, on="id", how="inner")
        print("\n--- Merged ETL Pipeline Data View ---")
        print(merged_df.head())

        # Save to target Data Lake / Warehouse stage
        merged_df.to_csv("cleaned_warehouse_profiles.csv", index=False)
        print("\nData successfully saved to 'cleaned_warehouse_profiles.csv'")
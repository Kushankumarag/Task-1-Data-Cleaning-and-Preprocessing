import pandas as pd
from pathlib import Path

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "dataset" / "netflix_titles.csv"
OUTPUT_FILE = BASE_DIR / "dataset" / "cleaned_netflix_titles.csv"


def load_data(file_path: Path) -> pd.DataFrame:
    """Load raw CSV dataset."""
    print(f"Loading data from: {file_path}")
    return pd.read_csv(file_path)


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to lowercase with underscores."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(r"[^\w]", "", regex=True)
    )
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values with appropriate defaults."""
    fill_values = {
        "director": "Unknown",
        "cast": "Unknown",
        "country": "Unknown",
        "rating": "Not Rated",
        "duration": "Unknown",
    }
    df = df.fillna(value=fill_values)
    return df


def convert_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert date_added column to datetime format."""
    if "date_added" in df.columns:
        df["date_added"] = pd.to_datetime(
            df["date_added"].str.strip(), errors="coerce"
        )
    return df


def remove_duplicates(df: pd.DataFrame) -> tuple:
    """Remove duplicate rows and report count."""
    initial_rows = len(df)
    df = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df)
    return df, duplicates_removed


def verify_data_types(df: pd.DataFrame) -> pd.Series:
    """Return dtypes of all columns."""
    return df.dtypes


def save_data(df: pd.DataFrame, output_path: Path) -> None:
    """Save the cleaned dataset to CSV."""
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to: {output_path}")


def main() -> None:
    # Step 1: Load
    df = load_data(INPUT_FILE)
    original_rows = len(df)
    print(f"\nOriginal rows : {original_rows}")

    # Step 2: Missing values before cleaning
    print("\nMissing values BEFORE cleaning:")
    print(df.isnull().sum())

    # Step 3: Standardize column names
    df = standardize_column_names(df)
    print("\nStandardized column names:")
    print(list(df.columns))

    # Step 4: Handle missing values
    df = handle_missing_values(df)

    # Step 5: Convert date columns
    df = convert_date_columns(df)

    # Step 6: Remove duplicates
    df, duplicates_removed = remove_duplicates(df)
    print(f"\nDuplicate rows removed : {duplicates_removed}")
    print(f"Final rows             : {len(df)}")

    # Step 7: Verify dtypes
    print("\nData types after cleaning:")
    print(verify_data_types(df))

    # Step 8: Missing values after cleaning
    print("\nMissing values AFTER cleaning:")
    print(df.isnull().sum())

    # Step 9: Save cleaned data
    save_data(df, OUTPUT_FILE)


if __name__ == "__main__":
    main()

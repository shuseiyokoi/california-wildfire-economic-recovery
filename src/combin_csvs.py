import pandas as pd
from pathlib import Path


def combine_csv_files():
    # Put your 4 CSV file paths here
    csv_files = [
        "../data/QCEW_2018_q1-q4_Butte_County.csv",
        "../data/QCEW_2018_q1-q4_Shasta_County.csv",
        "../data/QCEW_2019_q1-q4_Butte_County.csv",
        "../data/QCEW_2019_q1-q4_Shasta_County.csv",
    ]

    # Read and combine all CSVs
    dfs = [pd.read_csv(file) for file in csv_files]

    # Combine rows because all files have the same columns
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save combined CSV
    combined_df.to_csv("../data/combined.csv", index=False)

    print("../data/Combined CSV saved as combined.csv")
    print(combined_df.shape)


if __name__ == "__main__":
    combine_csv_files()

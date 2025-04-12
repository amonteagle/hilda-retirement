# pip install pandas pyreadstat

import pandas as pd
from pathlib import Path

def convert_sas_to_csv(input_folder, output_folder):
    """
    Reads all .sas7bdat files from a folder and saves them in .csv format.
    
    Parameters:
    -----------
    input_folder : str or Path
        Path to the folder containing .sas7bdat files.
    output_folder : str or Path
        Folder where the .csv files will be saved.
    """
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    sas_files = list(input_folder.glob("*.sas7bdat"))
    if not sas_files:
        print("No SAS files found in the input folder.")
        return

    for sas_file in sas_files:
        try:
            print(f"📥 Reading: {sas_file.name}")
            df = pd.read_sas(sas_file, format='sas7bdat')

            csv_file = output_folder / f"{sas_file.stem}.csv"
            df.to_csv(csv_file, index=False)
            print(f"✅ Saved: {csv_file.name}")
        except Exception as e:
            print(f"❌ Error processing {sas_file.name}: {e}")


# Optional: Run this if called directly
if __name__ == "__main__":
    sas_folder = "../data/raw_sas/"
    csv_folder = "../data/raw_csv/"
    convert_sas_to_csv(sas_folder, csv_folder)

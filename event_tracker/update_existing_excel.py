import pandas as pd
from datetime import datetime

FILE = "district_events.xlsx"

def update_existing_data():
    df = pd.read_excel(FILE, engine="openpyxl")

    # Update last_updated every run
    df["last_updated"] = datetime.now()

    # Expiry logic
    if "date" in df.columns:
        df["parsed_date"] = pd.to_datetime(df["date"], errors="coerce")
        df.loc[df["parsed_date"] < datetime.now(), "status"] = "expired"
        df.drop(columns=["parsed_date"], inplace=True)

    df.to_excel(FILE, index=False, engine="openpyxl")
    print("✅ Existing Excel data updated (no website used)")

if __name__ == "__main__":
    update_existing_data()

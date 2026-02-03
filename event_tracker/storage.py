import pandas as pd
import os
from datetime import datetime

FILE = "district_events.xlsx"

def load_data():
    if os.path.exists(FILE):
        return pd.read_excel(FILE, engine="openpyxl")
    return pd.DataFrame()

def save_data(df):
    df.to_excel(FILE, index=False, engine="openpyxl")

def update_excel(old_df, new_df):
    if old_df.empty:
        new_df["last_updated"] = datetime.now()
        return new_df

    old_df = old_df.set_index("url")
    new_df = new_df.set_index("url")

    old_df.update(new_df)
    combined = pd.concat([old_df, new_df]).drop_duplicates()

    combined["last_updated"] = datetime.now()
    return combined.reset_index()
from scraper import fetch_events
from storage import load_data, save_data, update_excel

city = input("Enter city name: ").strip()

print(f"Fetching events for {city}...")
new_events = fetch_events(city)

print("Loading Excel...")
old_data = load_data()

print("Updating Excel...")
final_data = update_excel(old_data, new_events)

save_data(final_data)

print("✅ Events updated in district_events.xlsx")

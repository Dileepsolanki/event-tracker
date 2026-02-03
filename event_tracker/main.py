
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

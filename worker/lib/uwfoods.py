from lib.config import Config
from uwaterlooapi import UWaterlooAPI
from datetime import datetime

AUTH_KEY = Config.get("UWFOODS", "AUTH_KEY")

client = UWaterlooAPI(api_key=AUTH_KEY)

def get_taco_restaurants():
    today = datetime.today().strftime("%Y-%m-%d")
    restaurants = []
    for outlet in client.menu()['outlets']:
        for day in outlet['menu']:
            if day['date'] == today:
                for meal in day['meals']:
                    for item in day['meals'][meal]:
                        if 'taco' in item['product_name'].lower():
                            restaurants.append({
                                'restaurant': outlet['outlet_name'],
                                'meal': meal,
                                'food': item['product_name']})

    return restaurants

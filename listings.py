from data_gen import *
from google_req import *
import re
import requests
import pandas as pd

listings=[]
api_key = "AIzaSyCxE9aVlXtzuT5u5tCQACEcfu41yFkmPvs"
def events(user1,user2):
    
    
    events,city=events_gen(user1,user2)
    # Set your Google Maps API key here

    def extract_info(places_data):
        results = []
        pattern = r'href="([^"]+)"'
        for place in places_data:
            if 'photos' in place and 'html_attributions' in place['photos'][0]:
                name = place['name']
                formatted_address = place['formatted_address']
                icon_link = place['icon']
                geometry = place['geometry']

                attributions_link = re.findall(pattern, place['photos'][0]['html_attributions'][0])
                results.append({'name': name, 'formatted_address': formatted_address, 'icon_link': icon_link, 'attributions_link': attributions_link[0],'lat':geometry['location']['lat'],'lng':geometry['location']['lng']})
        return results[:3]

    def get_listings(api_key, events, city):
        if events is None:
            places_data=get_google_maps_listings(api_key,query="popular",location=city)
            listings.append({"popular activities":extract_info(places_data)})
        else:
            subheadings = re.findall(r'\d+\.\s*(.*?):', events)
            for i,query in enumerate(subheadings):
                places_data=get_google_maps_listings(api_key, query,city)
                listings.append({query:extract_info(places_data)})
        return [events,city,listings]


    return get_listings(api_key,events,city)

#events(user1,user2)
#print(len(get_listings(api_key,events,city)))
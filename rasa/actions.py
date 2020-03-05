# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import transformations
import util_database
import pickle
from datetime import datetime
import numpy as np
from operator import itemgetter
from collections import defaultdict

get_make = util_database.get_make
get_model = util_database.get_model
get_fuel = util_database.get_fuel
get_body = util_database.get_body

transform_badge = transformations.transform_badge       #load badge transformation

with open('make_model_dict.json', 'r') as fp:           #load make:models dictionary
    make_model_dict = json.load(fp)

pkl_file_badge = open('LE01-badge_transformed.pkl', 'rb')   #load label encoders 
le_badge_transformed = pickle.load(pkl_file_badge) 
pkl_file_badge.close()

pkl_file_coordinates = open('LE01-coordinates2city.pkl', 'rb')
le_coordinates2city = pickle.load(pkl_file_coordinates) 
pkl_file_coordinates.close()
    
filename = 'M01-RandomForestRegressor.sav'     #load model
regressor = pickle.load(open(filename, 'rb'))

datetime_month = datetime.now().month
datetime_year = datetime.now().year

with open("cities.txt", "rb") as fp:   #loading cities
  cities = pickle.load(fp)

## GLOBAL ENTITIES (context)
make = ""
model = ""
badge = ""
fuel = ""
body = ""
city = ""
car_year = ""
color = ""
mileage = ""
mileage_range = ""

entities = defaultdict(lambda: '')

class ActionPredictPrice(Action):

    def name(self) -> Text:
        return "action_predict_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        make = next(tracker.get_latest_entity_values('make'), None)
        model = next(tracker.get_latest_entity_values('model'), None)
        fuel = next(tracker.get_latest_entity_values('fuel_type'), None)
        body = next(tracker.get_latest_entity_values('body_type'), None)

        year = 2014
        km = 0
        badge = transform_badge(next(tracker.get_latest_entity_values('badge'), None))
        badge = int(le_badge_transformed.transform([badge])[0])
        city = 'Melbourne'
        city = int(le_coordinates2city.transform([city])[0])
        
        pred = regressor.predict(np.array([get_make(make), get_model(model), get_fuel(fuel), get_body(body), year, km, badge, city, datetime_year, datetime_month]).reshape(1,-1))
       
        dispatcher.utter_message(text="Price is: $"+str(pred[0]))

        return []


class ActionReturnCheapestCity(Action):

    def name(self) -> Text:
        return "action_return_cheapest_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        make = next(tracker.get_latest_entity_values('make'), None)
        model = next(tracker.get_latest_entity_values('model'), None)
        fuel = next(tracker.get_latest_entity_values('fuel_type'), None)
        body = next(tracker.get_latest_entity_values('body_type'), None)

        year = 2014
        km = 0
        badge = transform_badge(next(tracker.get_latest_entity_values('badge'), None))
        badge = int(le_badge_transformed.transform([badge])[0])

        preds = []

        for c in cities:
            city = int(le_coordinates2city.transform([c])[0])
            preds.append( regressor.predict(np.array([get_make(make), get_model(model), get_fuel(fuel), get_body(body), year, km, badge, city, datetime_year, datetime_month]).reshape(1,-1))[0] )

        min_indices = np.argsort(preds)[:10]
        min_cities = list(itemgetter(*min_indices)(cities))
        min_preds =  list(itemgetter(*min_indices)(preds))
       
        dispatcher.utter_message(text="The cities where this car would be cheaper are (from lowest to highest price):\n"+str(min_cities))

        return []

class ActionWhichModelSell(Action):

    def name(self) -> Text:
        return "action_which_model_sell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        make = next(tracker.get_latest_entity_values('make'), None)
       
        dispatcher.utter_message(text="Which "+make+" car do you want to sell?")

        return []

class ActionWhichBadgeSell(Action):

    def name(self) -> Text:
        return "action_which_badge_sell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        model = next(tracker.get_latest_entity_values('model'), None)
       
        dispatcher.utter_message(text="Is your "+model+" a ____ ____ ____?")

        return []

class ActionWhichBodySell(Action):

    def name(self) -> Text:
        return "action_which_body_sell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message(text="which body type?")

        return []

class ActionPredictSellingPrice(Action):

    def name(self) -> Text:
        return "action_predict_selling_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        for event in tracker.events:
            if 'parse_data' in event:
                for entity in event['parse_data']['entities']:
                    entities[entity['entity']] = entity['value']
        print(entities)

        pred = regressor.predict(np.array([get_make(entities['make']), get_model(entities['model']), get_fuel(entities['fuel_type']), 
                                           get_body(entities['body_type']), int(entities['car_year']), int(entities['mileage']), 
                                           int(le_badge_transformed.transform([entities['badge']])[0]), int(le_coordinates2city.transform([ entities['city'][0].upper() + entities['city'][1:].lower() ])[0]), 
                                           datetime_year, datetime_month]).reshape(1,-1))
        min_range = pred[0] - 500
        max_range = pred[0] + 500
        dispatcher.utter_message(text="Your car would sell for about $"+str(min_range)+" to $"+str(max_range) )

        return []

class ActionWhichModel(Action):

    def name(self) -> Text:
        return "action_which_model"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        make = next(tracker.get_latest_entity_values('make'), None)
       
        dispatcher.utter_message(text="Which "+make+" car do you want to buy?")

        return []

class ActionWhichBadge(Action):

    def name(self) -> Text:
        return "action_which_badge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        model = next(tracker.get_latest_entity_values('model'), None)
       
        dispatcher.utter_message(text="What type of "+model+" do you want? ___ ____ or ___?")

        return []

class ActionWhichBody(Action):

    def name(self) -> Text:
        return "action_which_body"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message(text="Which body type are you looking for? SUV? Hatchback?")

        return []

class ActionPredictSBSPrice(Action):

    def name(self) -> Text:
        return "action_predict_sbs_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        for event in tracker.events:
            if 'parse_data' in event:
                for entity in event['parse_data']['entities']:
                    entities[entity['entity']] = entity['value']
        print(entities)

        pred = regressor.predict(np.array([get_make(entities['make']), get_model(entities['model']), get_fuel(entities['fuel_type']), 
                                           get_body(entities['body_type']), int(entities['car_year']), int(entities['mileage']), 
                                           int(le_badge_transformed.transform([entities['badge']])[0]), int(le_coordinates2city.transform([ entities['city'][0].upper() + entities['city'][1:].lower() ])[0]), 
                                           datetime_year, datetime_month]).reshape(1,-1))
        min_range = pred[0] - 500
        max_range = pred[0] + 500
        dispatcher.utter_message(text="You can buy this car for about $"+str(min_range)+" to $"+str(max_range) )

        return []
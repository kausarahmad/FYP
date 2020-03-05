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

class ActionWhichModel(Action):

    def name(self) -> Text:
        return "action_which_model"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        make = next(tracker.get_latest_entity_values('make'), None)
       
        dispatcher.utter_message(text="Which "+make+" car do you want to sell?")

        return []

class ActionWhichBadge(Action):

    def name(self) -> Text:
        return "action_which_badge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        model = next(tracker.get_latest_entity_values('model'), None)
       
        dispatcher.utter_message(text="Is your "+model+" a ____ ____ ____?")

        return []

class ActionWhichBody(Action):

    def name(self) -> Text:
        return "action_which_body"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message(text="which body type?")

        return []

#action_predict_selling_price
class ActionPredictSellingPrice(Action):

    def name(self) -> Text:
        return "action_predict_selling_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        for event in tracker.events:
        # if there is further data bein parsed
            if 'parse_data' in event:
                # is only doing something if there actually are entities
                for entity in event['parse_data']['entities']:
                    print('Found entity: {}'.format(entity))

        dispatcher.utter_message(text="")

        return []
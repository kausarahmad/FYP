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
import pickle
from datetime import datetime
import pymysql
import numpy as np

db = pymysql.connect(host='localhost',user='root',passwd='',db='caroogle')      #connect with database
cursor = db.cursor()

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

        query_make = ("SELECT dim_make.make_id FROM dim_make WHERE dim_make.make='"+make+"';")
        cursor.execute(query_make)
        make = cursor.fetchall()[0][0]

        query_model = ("SELECT dim_model.model_id FROM dim_model WHERE dim_model.model='"+model+"';")
        cursor.execute(query_model)
        model = cursor.fetchall()[0][0]

        query_fuel = ("SELECT dim_fuel_type.fuel_type_id FROM dim_fuel_type WHERE dim_fuel_type.fuel_type='"+fuel+"';")
        cursor.execute(query_fuel)
        fuel = cursor.fetchall()[0][0]

        query_body = ("SELECT dim_body_type.body_type_id FROM dim_body_type WHERE dim_body_type.body_type='"+body+"';")
        cursor.execute(query_body)
        body = cursor.fetchall()[0][0]

        year = 2014
        km = 0
        badge = transform_badge(next(tracker.get_latest_entity_values('badge'), None))
        badge = int(le_badge_transformed.transform([badge])[0])
        city = 'Melbourne'
        city = int(le_coordinates2city.transform([city])[0])
        
        pred = regressor.predict(np.array([make, model, fuel, body, year, km, badge, city, datetime_year, datetime_month]).reshape(1,-1))
       
        dispatcher.utter_message(text="Price is: $"+str(pred[0]))

        return []
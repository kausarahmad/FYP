<!-- ## greet_ask_price
* ask_price_without_details
  - utter_ask_car_details -->
  
## ask price path 1
* give_details
  - action_predict_price
  - utter_did_that_help
* affirm OR deny
  - utter_anything_else
  
<!-- ## ask price path 2
* ask_price_without_details
  - utter_which_city
* tell_city
  - utter_which_make
* tell_want_make
  - action_which_model
* tell_model
  - action_which_badge
* tell_badge
  - utter_which_car_year
* tell_car_year
  - utter_which_mileage
* tell_mileage
  - action_which_body
* tell_body
  - utter_which_fuel
* tell_fuel
  - action_predict_sbs_price
  - utter_did_that_help
* affirm OR deny
  - utter_anything_else -->
  
## ask city path 1    
* which_city_cheaper
  - action_return_cheapest_city 
  - utter_did_that_help
* affirm OR deny
  - utter_anything_else
  
## ask how much can car sell for
* sell_car
  - utter_which_city
* tell_city
  - utter_which_make_sell
* tell_make
  - action_which_model_sell
* tell_model
  - action_which_badge_sell
* tell_badge
  - utter_which_car_year_sell
* tell_car_year
  - utter_which_mileage_sell
* tell_mileage
  - utter_which_color
* tell_color
  - action_which_body_sell
* tell_body
  - utter_which_fuel_sell
* tell_fuel
  - action_predict_selling_price
  - utter_did_that_help
* affirm OR deny
  - utter_anything_else
  
## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## greet_ask_price
* ask_price_without_details
  - utter_ask_car_details
* give_details
  - action_predict_price
  - utter_did_that_help
* affirm OR deny
  - utter_anything_else

## ask price path 1
* ask_price
  - action_predict_price
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

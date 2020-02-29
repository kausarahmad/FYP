## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- okay
- ok

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:ask_price_without_details
- can I know the price of a car?
- can you tell me the price of cars?
- what is the price of car?

## lookup:make
data/lookup_tables/make.txt

## lookup:model
data/lookup_tables/model.txt

## lookup:body_type
data/lookup_tables/body_type.txt

## lookup:fuel_type
data/lookup_tables/fuel_type.txt

## lookup:badge
data/lookup_tables/badge.txt

## intent:give_details
- a [hyundai](make) [Veloster](model) [SRTURBO](badge) [hatchback](body_type) that runs on [petrol](fuel_type)
- the price of a [SUV](body_type) [subaru](make) [XV](model) [20i](badge) with [petrol](fuel_type) fuel
- tell me the price of a [sedan](body_type) [subaru](make) [liberty](model) [25i sports premium sat](badge) with fuel [diesel](fuel_type)
- what is the price of a [nissan](make) [pathfinder](model) [7-seat](badge) with [gas](fuel_type)
- can you tell me the price of a [nissan](make) [skyline](model) [4wd](badge) runs on [lpg](fuel_type)
- tell me the price of a [ford](make) [mustang](model) [2door coupe](body_type) [GT](badge) on [lpg](fuel_type)
- how much would a [ford](make) [falcon](model) cost?
- inform me of the cost of a [ford](make) [ranger](model)
- how much will I need to spend to buy a [rover](make) [75](model)?
- what would the price range of a [rover](make) [mini](model) be?
- how much would a [subaru](make) [XV](model) [SUV](body_type) cost?
- what is the price of a [hyundai](make) [Veloster](model) [hatchback](body_type) that runs on [petrol](fuel_type)?

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
- who are you?
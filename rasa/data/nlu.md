## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- bi
- bi bi
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
- I want to know the price of a car
- I want to buy a car
- i wanna buy a car

## intent:ask_comparison
- which car is better?
- can you compare these two cars?

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

## lookup:city
data/lookup_tables/city.txt

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

## intent:which_city_cheaper
- in which city would a [Mercedes-Benz](make:mercedes) [cls63](model) [coupe](badge) [sedan](body_type) that runs on [diesel](fuel_type) be cheaper?
- from where can I buy a [Convertible](body_type) [smart](make) [fortwo](model) [2 door](badge) with [petrol](fuel_type) fuel cheapest?
- which city would sell a low cost [sedan](body_type) [subaru](make) [liberty](model) [25i](badge) with fuel [diesel](fuel_type)?
- where would a [nissan](make) [pathfinder](model) [7-seat](badge) with [gas](fuel_type) be lowest cost?
- if I want a cheap [nissan](make) [skyline](model) [4wd](badge) runs on [lpg](fuel_type), which city should I buy in?
- which city has the most economical rates for [ford](make) [mustang](model) [2door coupe](body_type) [GT](badge) on [lpg](fuel_type)?
- where would a [ford](make) [falcon](model) cost less?
- I am on a tight budget, which city is the best option to buy a [ford](make) [ranger](model)
- which city has the cheapest [rover](make) [75](model)s?
- lowest cost [rover](make) [mini](model) are found in which city?
- I want to buy [subaru](make) [BRZ](model) [limited](badge) [automatic](body_type) for a low price, which city should I go to?
- where would I find the cheapest [hyundai](make) [Veloster](model) [hatchback](body_type) that runs on [petrol](fuel_type)?

## intent:sell_car
- i want to sell my car
- I want to know how much I can sell my car for
- Can you tell me how much my car would sell for?
- How much is my car worth?
- For how much can I sell my car?
- What price is my car worth?
- Can you value my car?

## intent:tell_city
- [north melbourne](city)
- [perthville](city)
- i live in [westcourt](city)
- i am a resident of [Diamond Creek](city)
- currently living in [north ryde](city)
- [launceston](city), tasmania
- i live in [Forestville](city), sydney
- [perth](city)
- [elsternwick](city)
- [manning](city)
- [east tamworth](city)

## intent:tell_make
- I want to sell my [Toyota](make)
- It's my [Ford](make)
- I have a [Hyundai](make)
- I want to sell my [mclaren](make)
- I am selling my [subaru](make)
- I own a [suzuki](make)
- [smart](make)
- I wanna sell a [hyundai](make)
- [hyundai](make)
- [toyota](make)
- a [mclaren](make)
- [ford](make)
- [nissan](make)
- [subaru](make)
- [mercedes-benz](make)

## intent:tell_want_make
- I want a [toyota](make)
- I want to buy a [nissan](make)
- I want a [nissan](make)
- I want [mclaren](make)
- I want to purchase a [hyundai](make)
- i want a [nissan](make)
- i want to buy a [mercedes-benz](make)
- a [nissan](make)
- [hyundai](make)
- [suzuki](make)

## intent:tell_model
- I want to sell my [Toyota](make) [Corolla](model)
- [350Z](model)
- It is a [Nissan](make) [350Z](model)
- I have a [pontiac](make) [gto](model)
- [cayman](model)
- [beetle](model)
- [pathfinder](model)
- [skyline](model)
- [jeep](make) [commander](model)
- [corolla](model)

## intent:tell_badge  
- [GLI](badge)
- [cobra](badge)
- [turbo](badge)
- it is a [2WD](badge)
- It's a [Hybrid Commemorative Edition](badge)
- My car is a [GT2](badge)
- [ST TITANIUM 4x4](badge)
- [30 tdi](badge)
- It's a [310CDI](badge)
- [Silverline SE](badge)
- It's specification is [gt comfort](badge)
- [raptor](badge)
- It is a [SLX 16 CRDi](badge)
- [ST Hybrid](badge)
- It's spec is [xlt](badge)

## intent:tell_car_year
- [2004](car_year)
- [2010](car_year)
- [1990](car_year)
- it's a [2001](car_year) model
- my car is a [2016](car_year) model
- it's from [1984](car_year)
- my car is from [1989](car_year)
- [1965](car_year)
- it was manufactured in [2006](car_year)
- [2019](car_year)
- my car was manufactured in [2007](car_year)
- [1974](car_year)

## intent:tell_mileage
- it has run [1000](mileage)km
- my car has covered [14480](mileage)km
- my car has lasted [763726](mileage) kilometers
- it has ran [200000](mileage) kilometers
- it has [827923](mileage)km on the odometer
- [827289](mileage)km
- [19999](mileage)kilometers
- [900000](mileage) kilometers
- [73786482](mileage)kilometers
- [300000000](mileage)kilometers
- [78623782](mileage) km
- kilometers [78628](mileage)
- [2000] km
- [300000] km
- [6000000] km
- [0] km
- [0] kilometers

## intent:tell_color
- [blue](color)
- [green](color)
- it's [red](color)
- [silver](color)
- it is [white](color)
- [orange](color)
- its color is [grey](color)

## intent:tell_body
- it is an [SUV](body_type)
- it is a [limousine](body_type)
- it's a [cab](body_type)
- a [Sedan](body_type)
- [wagon](body_type)
- it's a tattered old [hatchback](body_type)
- [van](body_type)

## intent:tell_fuel
- it runs on [petrol](fuel_type)
- my car runs on [diesel](fuel_type)
- [gas](fuel_type)
- [cng](fuel_type:gas)
- [lpg](fuel_type)
- my car's a [hybrid](fuel_type)
- [dual](fuel_type)

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
- who are you?
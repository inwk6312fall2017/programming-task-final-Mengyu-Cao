from weather import Weather
weather = Weather()
def weatherLoction(city):
    location = weather.lookup_by_location(city)
    condition = location.condition()
    
    for forecasts in location.forecast():
        print (forecasts['text'])
        print (forecasts['date'])
        print (forecasts['high'])
        print (forecasts['low'])

weatherLoction('Halifax')

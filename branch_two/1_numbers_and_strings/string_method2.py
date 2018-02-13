city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

#This line is formatted method rather than string concatenation for displaying an alert
alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city, str(low_temperature), str(high_temperature), temperature_unit, weather_conditions)

# print the alert
print(alert)

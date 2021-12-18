import requests

def print_weather(weather_response, units):
  """
  Print the given weather information
  adding given units after temperature values
  """
  pass

def get_weather_data(units, day_number):
  """
  Connect to the API using the requests library
  and return the predictions for the given day number
  """
  latitude = "45"
  longitude = "23"

def main():
  """
  Setup the main program
  """
  units = "metric"
  day_number = 0 #Represents today
  weather_response = get_weather_data(units, day_number)
  print_weather(weather_response, units)

if __name__ == "__main__": main()
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
  latitude = "45"   # Hard-coded lat & long for now
  longitude = "23"  # Will receive user input
  api_key = "37c2ff2b01dc9a7a782d60dbab1285e1"

  # Construct the endpoint URL
  api_prefix = "https://api.openweathermap.org/data/2.5/onecall?"
  api_lat_long = f"lat={latitude}&lon={longitude}&"
  api_exclusions = "exclude=hourly,minutely,alerts&"
  api_key_units = f"appid={api_key}&units={units}"
  api_endpoint = f"{api_prefix}{api_lat_long}{api_exclusions}{api_key_units}"

  # Use the requests library to fetch data from the endpoint
  response = requests.get(api_endpoint)

  # If the request fails, return False to indicate failure
  if response.status_code != 200:
    return False

  # Convert the response object to a dictionary
  response_dict = response.json()

  # Create a new dictionary to only hold data we need
  relevant_data = dict()

  # Extract relevant data from the API response
  data = response_dict['daily'][day_number]
  temp = data['temp']
  relevant_data['description'] = data['weather'][0]['description']
  relevant_data['feels_like'] = data['feels_like']['day']
  relevant_data['temp_day'] = temp['day']
  relevant_data['temp_min'] = temp['min']
  relevant_data['temp_max'] = temp['max']
  

def main():
  """
  Setup the main program
  """
  units = "metric"
  day_number = 0 # Represents today
  weather_response = get_weather_data(units, day_number)
  print_weather(weather_response, units)

if __name__ == "__main__": main()
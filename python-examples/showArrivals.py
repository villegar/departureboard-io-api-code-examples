# Import Dependencies
import json, urllib.request, logging, sys
from urllib.error import URLError, HTTPError
from prettytable import PrettyTable

# Define the Train Station to show arrivals from
lookup_station = "HAY"

# Define the National Rail API Key (This should be an environment variable in Production)
national_rail_api_key = "XXXXX"

# Build the URL to lookup train arrivals
departureboard_api_url = "https://api.departureboard.io/api/v1.0/getArrivalsByCRS/" + lookup_station + "/?apiKey=" + national_rail_api_key 

# Make the API Call, and capture errors
try:
    dbResult = urllib.request.urlopen(departureboard_api_url)
except HTTPError as e:
    logging.error('Error contacting the departureboard.io API. HTTP Error code: ' + str(e.code))
    sys.exit()
except URLError as e:
    logging.error('Error contacting the departureboard.io API. URL Error: ' + str(e.reason))
    sys.exit()

# Print Helper Message - Remove in Production
print('')
print("DEBUG: Information is being pulled from the following JSON Response. Access via your browser to see the available fields: " + departureboard_api_url)
print('')

# Process the JSON Response
json_response = json.loads(dbResult.read().decode())

# Print the station departures are being shown for. Fields are access via json_response['<JSON FIELD NAME>']
print("Showing arrivals for: " + json_response['locationName'])

# Define a Pretty Table to output the data
t = PrettyTable(['Sch Arr', 'Est Arr', 'Operator', 'Source', 'Calling Points'])

# Loop through each service, and add it to the Pretty Table table as a row
for service in json_response['trainServices']:

    # Declare a list to store the subsequent Calling Points
    serviceCallingPoints = list()

    # Loop through the previousCallingPoints in the service, and add them to the serviceCallingPoints list
    for callingPoint in service['previousCallingPoints']:
        serviceCallingPoints.append(callingPoint['locationName'])

    # Convert the serviceCallingPoints list to a comma seperated string
    serviceCallingPoints = ', '.join(map(str, serviceCallingPoints)) 

    # Add the service as a row on the Pretty Table
    t.add_row([service['sta'], service['eta'], service['operator'], service['origin'][0]['locationName'], serviceCallingPoints])

# Print the Pretty Table
print(t)
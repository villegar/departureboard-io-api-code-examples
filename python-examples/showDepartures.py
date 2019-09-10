# Import Dependencies
import json, urllib.request, logging, sys
from urllib.error import URLError, HTTPError
from prettytable import PrettyTable

# Define the Train Station to show departures from
lookup_station = "HAY"

# Define the National Rail API Key (This should be an environment variable in Production)
# !!!!!! PLEASE NOTE: !!!!!! Newly generated National Rail API keys can take up to 15 minutes to become active.
# If you get a 401 error, please wait 15 minutes and try again.
national_rail_api_key = "XXXXX"

# Build the URL to lookup train departures
departureboard_api_url = "https://api.departureboard.io/api/v2.0/getDeparturesByCRS/" + lookup_station + "/?apiKey=" + national_rail_api_key 

# Set the User Agent with a meaningful value describing what you are using the API for. This is optional but helps me see cool projects
api_call_user_agent = { 'User-Agent' : 'departureboard.io Python API Code Samples' }

# Make the API Call, and capture errors
try:
    dbRequest = urllib.request.Request(url=departureboard_api_url, headers=api_call_user_agent)
    dbResult = urllib.request.urlopen(dbRequest)
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
print("Showing departures for: " + json_response['locationName'])

# Define a Pretty Table to output the data
t = PrettyTable(['Sch Dep', 'Est Dep', 'Operator', 'Destination', 'Calling Points'])

# Loop through each service, and add it to the Pretty Table table as a row
for service in json_response['trainServices']:

    # Declare a list to store the subsequent Calling Points
    serviceCallingPoints = list()

    # Loop through the subsequentCallingPoints in the service, and add them to the serviceCallingPoints list
    for callingPoint in service['subsequentCallingPointsList'][0]['subsequentCallingPoints']:
        serviceCallingPoints.append(callingPoint['locationName'])

    # Convert the serviceCallingPoints list to a comma seperated string
    serviceCallingPoints = ', '.join(map(str, serviceCallingPoints)) 

    # Add the service as a row on the Pretty Table
    t.add_row([service['std'], service['etd'], service['operator'], service['destination'][0]['locationName'], serviceCallingPoints])

# Print the Pretty Table
print(t)
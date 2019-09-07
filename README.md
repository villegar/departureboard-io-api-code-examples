# departureboard.io API Code Samples
Welcome to the departureboard.io API Code Samples. This repository is designed to give you some very simple examples of how you can quickly start using the departureboard.io API with minimal code.

The [departureboard.io API](https://api.departureboard.io/#introduction) provides a RESTful interface to access the National Rail Enquiries Darwin Data Feeds. The official National Rail API is a legacy SOAP API, which can be very complex and difficult to develop with. The departureboard.io API makes developing with Rail data incredibly simple.

These are just some quick examples of how you can use the data from the departureboard.io API response. The possibilities are endless. In order to make use of the API you will need to [register for a National Rail OpenLDBWS API Key](http://realtime.nationalrail.co.uk/OpenLDBWSRegistration/).

The [departureboard.io API](https://api.departureboard.io/#introduction) has detailed documentation which I recommend reviewing.

## Python Examples
The Python code examples currently contain the following:

* `showArrivals.py`: Uses the departureboard.io API to print a simple table showing arrivals to the defined station. It shows the scheduled time of arrival, estimated time of arrival, the origin of the service, and the service calling points.
* `showDepartures.py`: Uses the departureboard.io API to print a simple table showing departures from the defined station. It shows the scheduled time of departure, estimated time of departure, the destination of the service, and the service calling points.

These examples use `prettytable` to nicely format the output, which you can install by running:

```
pip3 install prettytable
```

The examples have only been tested in Python 3.
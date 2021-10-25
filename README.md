# lisptick-python

## LispTick Python client library

It allows to send request and receive result from a LispTick server.  
Get a socket connection to a LispTick server, for example:

* `lisptick.org:12006` main server
* `kereon.lisptick.org:12006` Kereon Intelligence server

Send your request and read the streamed result.

## package
client_test.py is our regression test ensuring each data type is checked.

### MeteoNet Example

Here is an example asking for the temperatures on 7th june 2017 ```2017-07-06``` at Poitiers Airport (meteonet code ```"86027001"```), data are coming from [MeteoNet](https://meteonet.umr-cnrm.fr/).
```python
import lisptick

HOST = "lisptick.org"
PORT = 12006

def main():
    """Ask for temperature at Poitiers airport"""
    conn = lisptick.Socket(HOST, PORT)
    request = """(timeserie @"t" "meteonet" "86027001" 2017-07-06)"""
    timeserie = conn.get_result(request)
    for point in timeserie:
        print(point)

if __name__ == "__main__":
    main()
```

## Examples

Directories with examples for different data sources.

### MeteoNet

Meteorological data from Météo France.

* **oneday.py**

  Simple small temperature timeserie.  
  Full result is retreived into an array.

* **oneday_walk.py**

  Simple small temperature timeserie.  
  Streamed result is read point by point minimizing memory usage.

* **temperature_max.py**

  A little bit more elaborated requests with symbol definition and Kelvin to Celsius convertion.
  Stream maximum temperature in Celsius at Poitiers from 1st Jan 2016 to 31th Dec 2018.

### Bitstamp

Bitstamp is a cryptocurrency market place allowing bitcoin trading.  
We use it as an example of live flow computation with LispTick.

* **liquidity.py**

  Live simple liquidity indicators, like bid ask spread and mininum available volume at first limit.  
  Shows how to request several live timeseries in one request and how to handle them.
  
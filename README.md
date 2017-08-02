# uber-tracker
> To track uber estimate for my regular route

## Setup

*  Add locations.py to src folder with your source and destination

```python
coordinates = {}

coordinates['office'] = {'lat': xx.xxx, 'lng': xx.xxx}
coordinates['home'] = {'lat': xx.xxx, 'lng': xx.xxx}
```

* Environmental Variables

```
export UBER_SERVER_TOKEN=<your_token>
export DATABASE_URI=<mongo_db_uri>
export TZ=<timezone> # for docker container
```

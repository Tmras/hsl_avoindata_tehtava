Commands that can be used in the cli:
get id: returns parking data for desired facility. Currently possible ids are 1 and 755.
get all: returns parking data for all possible facilities.
get saved id: returns average availability percent by hour for desired facility. 1 and 755 are possible.

API:
Api is opened in the url 127.0.0.1:8000
You can make following requests to it:
/realtime/{id} where id is the id of the desired facility (1 and 755 are possible). If id is "all" then all facilities are returned.
/saved/{id} will return average availability percentage for desired facility

Run in terminal with command python -m main

Install dependencies with command pip install -r requirements.txt
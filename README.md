## Welcome to slowrest!
### Table of contents
* [Introduction](#introduction)
* [Setup](#setup)
* [Usage](#usage)
* [Deployment](#deployment)
* [Design Choices](#designchoices)
* [Future Plans](#futureplans)

### Introduction
This read-only REST-API was developed to effectively access the in the DCS-DB.

### Setup
Check out the code:
```
$ git clone ssh://git@gitlab.cern.ch:7999/ligerlac/slowrest.git
$ cd slowrest/
```
Create a virtual environment, activate it and install dependencies
```
$ python -m venv venv/
$ . venv/bin/activate
$ pip install -r requirements.txt
```
Setup flask variables
```
$ export FLASK_APP=slowrest
$ export FLASK_ENV=development
```
Initialize the DB and fill it with toy data
(as defined in ```tests/data.sql```).
```
$ flask init-db
$ flask fill-db
```
Run the application
```
$ flask run
```
In case the ```flask``` command does not work, consider replacing it by
```python -m flask```. 


### Usage
Several resources are available. Some of them correspond more or
less to an actual entry in the DB and have POST and GET methods,
while the more complicated composite ones are GET-only. The examples
in the following listing assume the app running on ```localhost```
on port ```5000``` and the DB being populated with toy data as
mentioned in [Setup](#setup).

#### global tag (```/globaltag/{string:globaltag}```)
* Maps to one tag for each kind of conditions data for a given global tag
* GET and POST
* Example: ```$ curl http://localhost:5000/globaltag/2.0```

#### hash (```/hash/{string:kind}/{string:tag}/{int:runnumber}```)
* Unique identifier for each payload as a function of the kind
and tag of the conditions data as well as the run number.
In case the payload is stored in a file, the hash is the full path
* GET and POST
* Example: ```$ curl http://localhost:5000/hash/lifetime/2.0/5844```

#### payload (```/payload/{string:hash}```)
* Contains the actual data. Stored serialized in a dedicated
table and accessed through its hash. The (de-)serialization must
happen on the client side
* GET and POST
* Example: ```$ curl http://localhost:5000/payload/posadiubb```

#### tag map (```/tagmap/{string:globaltag}```)
* For a given global tag, this maps every kind of conditions data
for every run number to the hash of the corresponding payload
* GET-ONLY
* Example: ```$ curl http://localhost:5000/tagmap/2.0```

Check the testing code in the ```tests/``` folder for examples
on how to access the resources via the python module ```requests```
instead of ```curl```.

For read-only applications, the client would first retrieve the
**tag map** for a given global tag. Then, this mapping is parsed
locally to get the hash of the desired payload for a given kind
of conditions data and run number. The actual conditions data is
then retrieved via the **payload** resource. This way, only two
resources are accessed and DB queries are reduced to a minimum.


### Deployment
Assuming a suitable web server (e.g. Apache or nginx) is running
and properly configured, the app can be deployed with the
following steps.
```
python setup.py bdist_wheel
```
Copy the output to the designated server
```
scp dist/slowrest-1.0.0-py3-none-any.whl <user>@<ip>:/<dest>/
```
On that server, create venv and install package:
```
python3 -m venv venv/
. venv/bin/activate
pip install slowrest-1.0.0-py3-none-any.whl
```
Run it via gunicorn
```
gunicorn --workers=1 slowrest:app -b 0.0.0.0:5000 --worker-class=gevent
```

### Design choices
to be written

### Future Plans
to be written
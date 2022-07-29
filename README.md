## Welcome to tagrest!
### Table of contents
* [Introduction](#introduction)
* [Setup Locally](#setup)
* [Usage](#usage)
* [Deployment](#deployment)
* [Design Choices](#designchoices)
* [Future Plans](#futureplans)

### Introduction
This REST-API was developed to effectively handle conditions data, deploying
a schema very similar to what is described in the HSF white paper
(https://arxiv.org/abs/1901.05429). At its foundation sits an sqlite database,
but any RDBMS could be deployed instead with little additional effort.
The client can directly access the data via http requests
(see [Usage](#usage)), however, it is recommended to use the dedicated
client side python API that was developed for this purpose
(https://gitlab.cern.ch/ligerlac/tagface).

### Setup Locally
Check out the code:
```
$ ssh://git@gitlab.cern.ch:7999/ligerlac/tagrest.git
$ cd tagrest/
```
Create a virtual environment, activate it and install dependencies
```
$ python -m venv venv/
$ . venv/bin/activate
$ pip install -r requirements.txt
```
Setup flask variables
```
$ export FLASK_APP=tagrest
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
while the more complicate composite ones are GET-only. The
following listing assumes the app running on ```localhost```
on port ```5000```.

#### global tag
* Maps to one tag for each kind of conditions data
* ```$ curl http://localhost:5000/globaltag/<string:globaltag>"```
* GET and POST

#### hash
* Unique identifier for each payload as a function of the kind
and tag of the conditions data as well as the run number.
In case the payload is stored in a file, the hash is the full path
* ```$ curl http://localhost:5000/hash/<string:kind>/<string:tag>/<int:runnumber>", methods=("GET", "POST"))```
* GET and POST

#### payload
* Contains the actual data. Stored serialized in a dedicated
table and accessed through its hash. The de-serialization must
happen on the client side
* ```$ curl http://localhost:5000/payload/<string:hash>```
* GET and POST

Instead of ```curl```, the resources can also be accessed
via the python module ```requests```. Check the testing code
in the ```tests/``` folder for examples.


#### tag map
* For a given global tag, this maps every kind of conditions data
for every run number to the hash of the corresponding payload
* ```$ curl http://localhost:5000/tagmap/<string:globaltag>")```
* GET-ONLY

### Deployment
Assuming a suitable web server (e.g. Apache or nginx) is running
and properly configured, the app can be deployed with the
following steps.
```
python setup.py bdist_wheel
```
Copy that file to the designated server
```
scp dist/tagrest-1.0.0-py3-none-any.whl <user>@<ip>:/<dest>/
```
On that server, create venv and install package:
```
python3 -m venv venv/
. venv/bin/activate
pip install tagrest-1.0.0-py3-none-any.whl
```
Run it via gunicorn
```
gunicorn --workers=1 tagrest:app -b 0.0.0.0:5000 --worker-class=gevent
```

### Design choices
to be written

### Future Plans
to be written
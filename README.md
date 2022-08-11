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
Run the application
```
$ flask run
```
In case the ```flask``` command does not work, consider replacing it by
```python -m flask```. 


### Usage
Several resources are available:

#### sensor dict (```/sensor-dict```)
* Mapping from sensor id to sensor name
* One entry for each sensor in NP04_DCS_01.ELEMENTS
* Example: ```$ curl http://localhost:5000/sensor-dict```

#### sensor name (```/sensor-name/{int:sensor_id}```)
* Name of sensor for given id
* Example: ```$ curl http://localhost:5000/sensor-name/47894774153498```

#### day (```/day/payload/{string:hash}```)
* Timestamp-value-pairs for given day and sensor id
* Example: ```$ curl http://localhost:5000/day/2021-10-10/47894774153498```

Check the testing code in the ```tests/``` folder for examples
on how to access the resources via the python module ```requests```
instead of ```curl```.


### Deployment
Assuming a suitable web server (e.g. Apache or nginx) is running
and properly configured, the app can be deployed with the
following steps. On the local (development) machine, run
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
Configure flask app:
```
export FLASK_APP=slowrest
```
Generate a secret key via 
```
python -c 'import secrets; print(secrets.token_hex())'
```
and copy the output to venv/var/slowrest-instance/config.py like so (example string):
```
SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```
Install waitress
```
pip install waitress
```
And run the app:
```
waitress-serve --call 'flaskr:create_app'
```
Good luck!
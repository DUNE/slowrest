## Welcome to slowrest!
### Table of contents
* [Introduction](#introduction)
* [Setup](#setup)
* [Usage](#usage)
* [Deployment](#deployment)
* [Design Choices](#designchoices)
* [Future Plans](#futureplans)

### Introduction
This read-only REST-API was developed to access the DCS-DB (a.k.a. Slow Controls Archive).

### Setup
Check out the code:
```shell
git clone git@github.com:DUNE/slowrest.git
cd slowrest/
```
Create a virtual environment, activate it and install dependencies
```shell
python -m venv venv/
. venv/bin/activate
pip install -r requirements.txt
```
For development setup also install dev requirements.
```shell
pip install -r requirements-dev.txt
```
Run the application (in debug mode)
```shell
flask --app slowrest run --debug
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

#### day (```/day/{string:day}/{int:sensor_id}```)
* Timestamp-value-pairs for given day and sensor id
* Example: ```$ curl http://localhost:5000/day/2021-10-10/47894774153498```

#### range (```/range/{string:begin}/{string:end}/{int:sensor_id}```)
* Timestamp-value-pairs for given time range and sensor id
* Example: ```$ curl http://localhost:5000/range/2021-10-10T07:42:12/2021-10-10T12:06:52/47894774153498```

#### latest (```/latest/{sensor_list_identifier}```)
* Sensor list identifier found in sensor_lists folder filenames
* Example: ```$ curl http://0.0.0.0:5000/latest/bellegarde```

Check the testing code in the ```tests/``` folder for examples
on how to access the resources via the python module ```requests```
instead of ```curl```.


### Deployment

Before actual deployment one needs to setup `sensor_lists` folder files.
Assuming that you have a `sensor-ids.csv` file in the slowrest folder that 
contains sensor_ids in the first column and webpage name in 
the second run:

```
cat sensor-ids.csv | awk -F "," '{ print $1 > "sensor_lists/"$2}'
```
It will create files with names based on identifiers from second column and sensor_ids from the first column within the corresponding files. All files will be placed in the existing `sensor_lists` folder. Existing files will be overwritten.

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
export FLASK_credentials__user=my_user
export FLASK_credentials__password=my_pw
export FLASK_credentials__dsn=my_dsn
```
Generate a secret key via 
```
python -c 'import secrets; print(secrets.token_hex())'
```
and add it to the config:
```
export FLASK_SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```
Install waitress
```
pip install waitress
```
And run the app:
```
waitress-serve --call 'slowrest:create_app'
```

Good luck!

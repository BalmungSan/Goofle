# Goofle
## Python Flask web application to search files in a dataset
### Versión: 1.1.1 (25/04/2017)
### Authors:
- Pedro Calle Jaramillo
- Sergio Alejandro Lasso

#### Dependencies
- [python 3](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/)
- [Flask](http://flask.pocoo.org/). _install_ ```pip3 install flask```
- [WTForms](https://wtforms.readthedocs.io/en/latest/). _install_ ```pip3 install WTForms```
- [PyMongo](https://api.mongodb.com/python/current/). _install_ ```pip3 install pymongo```

#### How to use
##### Configure
Edit the file _settings.py_ to configure the application

``` python
#app configurations
class Config(object):
  DEBUG = True
  TESTING = False
  SECRET_KEY = "zzi0uj3NiiaTKJ1BkHBaJA=="
  SESSION_TYPE = "filesystem"
  APP_HOST = ""
  APP_PORT = 0
  MONGO_HOST = ""
  MONGO_PORT = 0
  MONGO_DB_NAME = ""
  MONGO_COLLECTION_NAME = ""
  MONGO_DB_USER = ""
  MONGO_DB_PWD = ""
```

**Where:**

- **APP_HOST:** It is the ip on which the application will run, it must be a valid ip in the network interfaces of the machine. _e.g. "localhost"_
- **APP_PORT:** It is the port on which the application will run. _e.g. 8080_
- **MONGO_HOST:** It is the ip on which mongo is listening.  _e.g. "localhost"_
- **MONGO_PORT:** It is the port on which mongo is listening.  _e.g. 27017_
- **MONGO_DB_NAME:** It is the name of the database to connect.  _e.g. "default"_
- **MONGO_COLLECTION_NAME:** It is the name of the collection to use.  _e.g. "inv_index"_
- **MONGO_DB_USER:** It is the username with which the application will authenticate in the database. _e.g. "user1"_
- **MONGO_DB_PWD:** It is the password of the username with which the application will authenticate in the database. _e.g. "1234"_

#### run
run the following command to start running the application in background

    $ nohup python3 run.py &

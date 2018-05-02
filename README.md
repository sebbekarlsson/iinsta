# iinsta
> Host your own Instagram in a local network or on the world wide web!

<img src='shot.png' width='300px'/>

## Installing and Running the development environent
> Here is how to run the development environemnt, these are the requirements:

* python 2.7
* python-virtualenv
* ruby sass gem

### Setup
> First create a virtualenv:

    virtualenv -p /usr/bin/python2.7 ./venv

> Source it

    source ./venv/bin/activate

> Run the setup:

    python setup.py develop

#### Transpiling the SASS to CSS
> To start watching for changes run:

    ./sass.sh

### Run
> To run the application:

    python __main__.py

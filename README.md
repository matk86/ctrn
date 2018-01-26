# ctrn

Install
--------

python setup.py develop

Requires MongoDB

Usage:
-------

1. Requires the data to be in MongoDb databse

2. Use the function in ctrn.preprocess.py module to insert the data in the csv file to mongodb(update the connection settings in ctrn/config.yaml if required)

3. The functions('add' and 'search') that perform the funcionalities mentioned in the problem statement can be found in the ctrn.core.py module.

4. The aforementioned functions in the core.py module essentially constitute the 'views' in a web app(Note: this package doesn't define a full webapp. Hence dummy responses instead of http responses are used as placeholders in the functions in the core.py module). 

5. Tests available in the ctrn/tests folder. To run tests: 'pip install nose' and run 'nosetests -v ctrn'

6. The package in also integrated with CircleCI.

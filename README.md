# GitTryout

* Trying Git Hub familiarization.

Take a look in helpnote folder in local

* Apitesting.py is containing simple get request.

* tableReading.py is execution point for simple Python-selenium automation framework.
It's following POM style.

* This Repo is not using Virtual env.

* for Virtual Env and LemonCheesecake refer Project folder in local

## Setup
Install and create virtualenv (This step should be executed only when setting up the project for the first time)

* Install virtualenv

``` python3 -m pip install --user virtualenv ```

* Create virtualenv

``` python3 -m venv env ```

* Activate the virtual environment:

``` $ source env/bin/activate ```

* Install dependencies for setting up tests:

``` pip install -r requirements.txt ```
* create module name starting with test and class name starting with Test
* for allure reports use command "pytest -v -s --alluredir="/Users/debamdas/PycharmProjects/pythonProject/GitTryout/reports" GitTryout/test_validateID.py"

* for viewing it in browser use command allure serve /Users/debamdas/PycharmProjects/pythonProject/GitTryout/reports

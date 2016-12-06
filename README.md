# AutomationFrameworkPython
Basic Python Selenium Framework


### Set Up ###
1. Check version of Python on your system
On the Terminal, write:
python --version
My Output:
Python 2.7.10

2. Install pip

sudo easy_install pip

3. Driver used was Firefox, but you can choose to use Chrome as well
To use Firefox however, make sure you have "marionette": False under 'FIREFOX'in your desired_capabilities.py. Latest versions
of firefox uses the marionette driver to run selenium which requires additional installation and version mis-match etc.

4. Install modules listed on the requirements.txt
cd Tests/
sudo pip -r requirements.txt
This will install all the necessary modules required to run the tests.

5. Add your login  or user details for tests to run in config.json file.


6. Use nose (test runner) to run all tests at once on your local.
On the terminal, write:
nosetests -v -s
(Where -v : verbose
       -s : stdout)

7. Once tests are run, the test details are listed out on the terminal.

# Saxion - Cold Case - News Search API


# Setup 
-----
## _Local – Linux/MacOS_

1.	Make sure you have python 3.9 and pip 21 installed.
2.	This project uses a MySQL database, if you want to connect to a local MySQL database, make sure you have MySQL server installed ( https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/ )
3.	A SQL script is provided in the repository with the database articles used for testing.
4.	Clone the Git repository to your local system.
5.	Make sure you have virtualenv installed:
```
sudo pip3 install virtualenv
```
6.	Create a virtual environment with the name of the project:
```
virtualenv coldcaseenv
```
8.	Activate the virtual environment: 
```
source coldcaseenv/bin/activate
```
9.	Go inside the project folder, and copy the .env.example file, and make the name of the new file “.env”:``` cp .env.example .env```
10.	Fill this file with your own environment variables. The variables that need to be filled are already there.
11.	Install the required packages:
```
pip install -r requirements.txt
```
12.	Now, migrate the database tables into the database with the following command: 
```
python manage.py migrate
```
14.	It is time to start the server, which you can do with the following command: 
```
python manage.py runserver
```
-----
## _Local- Windows_
The setup for Windows is very similar to the one on Linux. These are the differences:
Installing Python and pip:

1.	As a windows user, you can get Python, including pip, from here: https://www.python.org/downloads/
2.	Next, to install a virtual environment tool:
```
pip3 install virtualenvwrapper-win 
```
4.	Then, to start the virual environment, this is the command:
```
mkvirtualenv coldcaseenv
```
5.	The environment is activated automatically, so, now we can go on with step 8 (Linux/MacOS Setup (above))
-----
## _AWS_
To install this project on an AWS server, the steps are very similar to the ones for the local machine. This is what needs to be done.

1.	First, create an amazon EC2 instance, with SSH access to yourself, and http inbound requests for everyone.
2.	SSH into this instance, with the keys you got during the setup of this instance.
3.	Install the necessary packages: sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
4.	This project uses a MySQL database, if you want to connect to a local MySQL database, make sure you have MySQL server installed ( https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/ )
5.	A SQL script is provided in the repository with the database articles used for testing.
6.	Clone the Git repository to your local system.
7.	Make sure you have virtualenv installed:
a.	sudo pip3 install virtualenv
8.	Create a virtual environment with the name of the project: virtualenv coldcaseenv
9.	Activate the virtual environment: source coldcaseenv/bin/activate
10.	Go inside the project folder, and copy the .env.example file, and make the name of the new file “.env”: cp .env.example .env
11.	Fill this file with your own environment variables. The variables that need to be filled are already there.
12.	Install the required packages: pip install -r requirements.txt
13.	Now, migrate the database tables into the database with the following command: python manage.py migrate
14.	Get out of the local instance with the following command: deactivate
15.	Go to the root directory of the EC2 instance with: cd 
16.	Go to the directory where the Apache configuration file is located, and edit it: sudo vi /etc/apache2/sites-available/000-default.conf
17.	Replace the file with the following config:




To install this project on your local machine:

- Make sure you have python installed

- Activate a virtual environment
- pip install
- fill the .env file with your own variables
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

Lastly, run the server.

## Credits
>Version: 0.0.3 <br />
>Date: 29.06.2021<br />
>Project: Hot and Cold Case Project <br />
>Аssignor: [Saxion University of Applied Sciences (Advanced Forensic Technology)](https://www.saxion.nl/opleidingen/voltijd/bachelor/forensisch-onderzoek) | Jaap Knotter <br />
>Project Manager: [Tatjana Kuznecova](https://www.linkedin.com/in/tatjana-kuznecova-a8059211b/) <br />
>Software Consultant: [Dimitar Rangelov](https://www.linkedin.com/in/dimitarrangelov/)  | [SDP](https://sdproject.eu) <br />
>Software Developer: [Luuk Cloosterman](https://www.linkedin.com/in/luuk-cloosterman/)<br />

-------
[![N|Solid](https://sdproject.eu/assets/images/rsz_sdp_logo_eng4.png)](https://sdproject.eu) <br />
[![N|Solid](https://www.kennisid.nl/api/organisation/thumb/bpoC71F7D38-8715-4AEF-87F3-ACC08E8F5B26)](https://www.saxion.edu)

Introduction
-
Before starting this project I'd like to state that I've never worked with Python or Django before.

Therefore this project has been an exciting challenge for me!
Within a day I've learned to use the basics of Python and Django and then started working on this project.

Requirements
-
Create three pages (URLs) where:
- The first page will be able to upload my chosen ".csv file".
	- On the main page of http://127.0.0.1:8000/ you can upload the cars.csv file .
	- After the upload is complete, an 'OK' will be visible.
- The second page will display the .csv as a database with (NON-ADMIN) CRUD properties.
	- After seeing the 'OK' from the completed upload type /crud behind the standard url.
	- From this page you can access the uploaded database page with CRUD functionality.
- The third and last page will display 3 visualizations taken from said database. 
	- (IN PROGRESS)

Rules
-
- All logic and queries are done in "views.py"
- Database modeling is done in "models.py"
- The database needs to be a postgres database (I've used PostgreSQL for this project)

Dataset
-
The dataset I've used for this project is a free dataset with cars from:
https://perso.telecom-paristech.fr/eagan/class/igr204/datasets
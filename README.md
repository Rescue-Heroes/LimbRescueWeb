# Project Limb Rescue Web Application

Technical Team:
Tai-Yu Pan
Mengdi Fan
Rithvich Ramesh
Browy Li 

Sponsors:
Lynne Brophy, MSN, RN-BC, ARPN-CNS, AOCN
Carlo Contreras, MD, FASC

## Project Mission
Develop a user friendly web application that allows patients/doctors to create an account, upload data, and identify a diagnois.
## Application Components

### Database
The database is managed by Django itself and within the file directory it is located in the settings.py file. Be sure to familiarize yourself with this SQL Database and understand that the users and adminds are independent of each other.

### Graph

The application uses Plotly to graph data. The graph is shown after the user uploads a data file (CSV) with a respective name within the upload page.

#### Implementation


### History Screen

The history screen is composed of the HistoryFragment, which implements a RecyclerView. HistoryAdapter handles the display and reuse of items in the list. HistoryAdapter uses HistoryHolder to hold data for individual elements.
When an item is clicked, HistoryHolder create the DataAnalysisActivity and passes it its session. This then graphs that particular session.


## Installation

Necessary packages to install before compilation: Plotly, Numpy, Django, Flask, Chatterbot. These can all be successfully installed by using a package handler such as pip or conda. Be sure that your python version is up to date and compatible with the version of python Django is using. 

### Web App

To run the web application simply enter the command 'python manage.py runserver' within the terminal. Be sure to be in the project directory when running this command.

#### Chatterbot

To run the Chatterbot function, use pip install chatterbot, pip install Flask, and pip install chatterbot-corpus in the terminal. Run python app.py to activate the chat function.

#### ADMIN Login

How to access admin login of the web application: Run python manage.py createsuperuser. Go to http://127.0.0.1:8000/admin/, make sure you allready create the admin page.

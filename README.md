# Project Limb Rescue
Cancer patients are at risk of lymphedema, a devastating chronic complication. Our overall aim is to develop a product helping patients to monitor the risk of lymphedema. The product marries wearable devices equipped with photoplethysmography (PPG) sensors and our custom software to detect changes in limb characteristics that are concerning for new-onset, or worsening lymphedema. 
Limb Rescue Cloud, constitute of Data Base, Web Tool, and Machine Learning modules, establish connections between software, doctors, and data scientists.
<p align="center"><img src="https://github.com/Rescue-Heroes/LimbRescueML/blob/main/figures/PLR_context_diagram.png" width="400"></p>

## Project Limb Rescue Web Application (LimbRescueWeb)

Technical Team:
Tai-Yu Pan (Worked on file uploading functionality)
Mengdi Fan (Worked on Plotly graph functionality)
Rithvich Ramesh (Worked on sitewide styling)
Browy Li (Worked on user authentication and messaging system)

Sponsors:
Lynne Brophy, MSN, RN-BC, ARPN-CNS, AOCN
Carlo Contreras, MD, FASC

## Project Mission
Develop a user-friendly web application that allows patients/doctors to create an account, upload data, and identify a diagnosis. The web application will facilitate a home-based monitoring protocol for patients to monitor and track their lymphedema recordings.
## Application Components

### Database
The database is managed by Django itself and within the file directory, it is located in the settings.py file. Be sure to familiarize yourself with this SQL Database and understand that the users and admins are independent of each other.

### Graph

The application uses Plotly to graph data. The graph is shown after the user uploads a data file (CSV) with a respective name within the upload page.

#### Implementation


### History Screen

TODO

## Installation

Necessary packages to install before compilation: Plotly, Numpy, Django, Flask, Chatterbot. These can all be successfully installed by using a package handler such as pip or Conda. Be sure that your python version is up to date and compatible with the version of python Django is using. 

### Web App

To run the web application simply enter the command 'python manage.py runserver' within the terminal. Be sure to be in the project directory when running this command.

#### Chatterbot

To run the Chatterbot function, use pip install chatterbot, pip install Flask, and pip install chatterbot-corpus in the terminal. Run python app.py to activate the chat function.

#### ADMIN Login

How to access admin login of the web application: Run python manage.py createsuperuser. Go to http://127.0.0.1:8000/admin/, make sure you already create the admin page.

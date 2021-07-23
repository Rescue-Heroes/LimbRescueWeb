# Project Limb Rescue Web Application

Technical Team:
Tai Yu Pan
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


### Graph

The application uses Plotly to graph data. The graph is shown after the user uploads a data file (CSV) with a respective name within the upload page.

#### Implementation


### History Screen

The history screen is composed of the HistoryFragment, which implements a RecyclerView. HistoryAdapter handles the display and reuse of items in the list. HistoryAdapter uses HistoryHolder to hold data for individual elements.
When an item is clicked, HistoryHolder create the DataAnalysisActivity and passes it its session. This then graphs that particular session.


## Installation

Necessary packages to install before compilation: Plotly, Numpy, Django. These can all be successfully installed by using a package handler such as pip or conda. Be sure that your python version is up to date and compatible with the version of python Django is using. 

### Web App

To run the web application simply enter the command 'python manage.py runserver' within the terminal. Be sure to be in the project directory when running this command.

#### Prerequisites

Installing the WearOS application is slightly more cumbersome. You'll need a few things:

1. Android Studio downloaded to a computer (optionally you can just download `adb` although this is more advanced).
2. A local router that doesn't block connecting to peers.
3. The `wear-release.apk` file downloaded to your computer.

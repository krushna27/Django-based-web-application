# Django-based-web-application
Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

Features:
1. Users can upload CSV files directly through the web interface.
   
2. Data Processing- The application reads the uploaded CSV file and performs basic data analysis tasks such as displaying the first few rows of the data, calculating summary statistics (mean, median, standard deviation) for numerical columns, and identifying and handling missing values.
   
3. Data Visualization- The application generates basic plots such as histograms for numerical columns and displays these plots on the web page.
 
4. User Interface- A simple and user-friendly interface created using Django templates, CSS.

Setup Instructions:
1. Install Django - pip install django
2. create new project - django-admin startproject myproject
cd myproject
3. create new app within project - python manage.py startapp data_analysis

and then just replace the files from my project..

or
   
Clone the repository:

Follow these steps to set up and run the Django CSV Analysis App on your local machine:

1. 
git clone https://github.com/krushna27/Django-based-web-application.git

cd repository

3.
create Virtual environment
activate environment

4.
Install dependencies:
pip install pandas numpy matplotlib seaborn

5. 
apply migrate
python manage.py migrate

6.
run the server
python manage.py runserver


Usage Instructions:
open the browser and navigate to http://127.0.0.1:8000/.
click on choose file & select any csv file from machine
click upload

Results:
1. The application will display the first few rows of the data.
2. Summary statistics (mean, median, standard deviation) for numerical columns will be displayed.
3. Any missing values in the dataset will be identified and handled.
4. Basic plots such as histograms for numerical columns will be generated and displayed on the web page.

# Awwwards

>[Jeff-Mwai](https://github.com/Jeff-Mwai)  
  
# Description  
Awwwards is a project made to enable users to register and post their projects. The users can also rate other existing projects on the website based on design, usability and content.
##  Live Link  
 Click [View Site]()  to visit the site
 
## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  

  
## Setup and Installation  
One can follow the following steps to get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Jeff-Mwai/awwwards.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd project-awwards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source venv/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 ### Api Endpoints
 * https://chawwards.herokuapp.com/api/users/
 * https://chawwards.herokuapp.com/api/profile/
 * https://chawwards.herokuapp.com/api/posts/
 
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* The application does not have any known bugs currently

  
## Contact Information   
If you have any question or contributions, kindly reach me through [jeffmwai3@gmail.com]  
  
### License

* [[License: MIT]](LICENCE.md) <Jeff-Mwai>               
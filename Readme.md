# Django Rest api token based authentication
## Routes
/auth/login/ : [POST] takes username and password and return token
![alt text](/screenshots/login.PNG)

/auth/logout : [GET] takes token in header and logout the user
![alt text](/screenshots/logout.PNG)

/auth/home : [GET] takes token in header and return user details
![alt text](/screenshots/home.PNG)

/auth/register/ : [POST] takes username, password and email and return token and user
![alt text](/screenshots/register.PNG)

# More details about api can be found at this url
Url :[https://documenter.getpostman.com/view/10197308/SzfAzSWc?version=latest]

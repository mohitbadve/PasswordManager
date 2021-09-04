# PasswordManager
A Rest API service that keeps a record of users' passwords. Users can log into the panel to see the username and passwords of websites they have saved using Django REST APIs and MySQL database

Link for the video - https://github.com/mohitbadve/PasswordManager/blob/master/Demo.mp4

For running the project,
You need to have Python and Postman or any other API testing software installed, then in the command prompt, run the following command
>pip3 install -r requirements.txt

You need to create a database named as 'password_keeper' and run migration commands
>python manage.py migrate

>python manage.py makemigrations

Finally, when all the requirements will get installed, run the web service by running the command 
>python manage.py runserver

A new user can be registered through the following API
![Alt text](screenshots/register-user.PNG?raw=true "Register User")

A user can be authenticated through the following API
![Alt text](screenshots/auth-user-success.PNG?raw=true "Authenticate User")
![Alt text](screenshots/auth-user-failure.PNG?raw=true "Authenticate User")

A user can store password for a particular website through the following API
![Alt text](screenshots/add-website.PNG?raw=true "Store Password")

A user can list passwords stored for all websites through the following API
![Alt text](screenshots/list-websites.PNG?raw=true "List Passwords")


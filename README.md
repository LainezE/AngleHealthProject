# Backend Project for AngleHealth

Hello! I had a lot of fun creating these Post and Search routes I learned a ton of things in the past couple of days. 

## Instructions 

1. First cd into the proper directory:

`cd ./AngleHealthProject/src/backendproject`

2. In order to use this program you must first migrate the models to use in a database. by running:

`python3  manage.py makemigrations`
`python3 manage.py migrate`

3. Once the migrations are done you are all set to turn on the server: 

`python3 manage.py runserver`

### Testing Search Routes through browser or Postman 
Note: Logic for post and search routes can be found in `views.py`

You can view all of the products listed in the database by going to the url: 

[link] (http://localhost:8000/products/)

In addition, you can view specific products by using the url: 
**Be sure to replace `str` with a Keyword to be searched.**
**Be sure to replace `int` with a minimum and maximum price.**
**if there is no minimum or maximum price you may simply ignore the `int` after `=`**

[link] (http://localhost:8000/products/?keyword=str&min_price=int&max_price=int)

### Testing Post Request using tests.py 

You can test the post Requests by using the command: 

`python3 manage.py test` 

This command will test both search and post routes through the tests.py file. If you want to test json files not included with the assignment go to `tests.py` and change the filedata variable in line 14 and 23 to the `name.json` file. 
**Keep in mind the method in line 14 is for valid json data and line 23 is for invalid json data**
**Be sure to place json files in the proper directory shown below**

`/AngleHealthProject/src/backendproject/src/ecommerce` 

### Admin/Superuser Login

If you want to see the admin page Django comes with go to url: 

`http://localhost:8000/admin/login/?next=/admin/login`

`username: laineze1`
`password: 123456`

## Discussion

I used the following technologies: `Python`, `Django`, and `Djangorestframework` along with `Postman` to test API endpoints.
I've had no experience using `Django` before this project. However, I chose to use `Django` to demonstrate my ability to learn new technologies when required. 
Overall, I enjoyed creating this project as I learned many new things. Any feedback on how I could have done anything better is always welcome I am always trying to improve my craft. 


If you have any questions feel free to email me at lainez101@gmail.com

Thank you, 

Eli Lainez
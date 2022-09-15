## Link Heroku App

https://pbp-assignment-2-matthew.herokuapp.com/
Catalog website: https://pbp-assignment-2-matthew.herokuapp.com/katalog/

## MVT of the Django app

<img width="311" alt="image" src="https://user-images.githubusercontent.com/112454126/190206352-05510c53-3b6e-4c36-845d-576deaf941a4.png">

From the diagram above, we can see how the client request is processed to the django app and back to the client's browser. Firstly, the client sends a request when accessing the URL on a browser to the django app through the internet. This request would then be put through to the file urls.py in the django app which would then be forwarded to views.py where the developer has defined functions to process the request. In the case that the process includes the use of a database,  views.py will call a query to models.py and a database will return to views.py as a result of the query. Then, views.py would return and map the data acquired to the HTML file which would finally be returned to the user as a response (in this case a web page).![image]

## Python virtual environments

In running a Django app, it is recommended to do it in a virtual environment. Why? Because in a virtual environment, it creates an isolated environment where all the packages and versions that are installed only apply to that specific environment. This would remove the possibilities of gross global installation and package collision errors. However, running a Django app without using a virtual environment is possible, but it will present the risk of altering with the global packages

## Implementation

1. Function in views.py
   
   <img width="308" alt="image" src="https://user-images.githubusercontent.com/112454126/190214130-75fc8f88-3278-457c-ab04-03fce813e244.png">
   
   In views.py. The function show_katalog was created with the parameter request (HttpRequest) from the client's browser. The function would the take all of the objects from the CatalogItem which is imported from from models.py and create a dictionary containing key-value pair of the information needed to map to the HTML. It would then return the a render where the katalog.html is the template and the context created earlier is used for the data mapping.

2. Routing in urls.py

   <img width="291" alt="image" src="https://user-images.githubusercontent.com/112454126/190215848-905d8391-2cf4-4aa6-923b-bbd6e3c36760.png">

   From views.py, the function created before is imported. Then, a path is created in the urlpatterns so that the HTML page can be displayed in the browser
   
3. Mapping data into HTML

   <img width="263" alt="image" src="https://user-images.githubusercontent.com/112454126/190216448-5fd13710-8479-44f3-ba7d-e175ae8f581a.png">

   In the HTML file, use Django syntax and templates to map the data from views.py to the appropriate places

4. Deploying to Heroku
   
   To deploy to Heroku, firstly, create an app in your Heroku account. Then, copy API Key from your Heroku account and  add 2 new repository secrets with your Heroku app name and Heroku API Key. Lastly, re-run the failed workflows. After the deployment status becomes successful, the application can be accessed from the link at the top of this file.

## Link Heroku App

https://pbp-assignment-2-matthew.herokuapp.com/

My Watch List website: https://pbp-assignment-2-matthew.herokuapp.com/mywatchlist/html/

## HTML, JSON, XML

HTML is an abbreviation for HyperText Markup Language. It is a language that is used to structure a web page and display data. The data that the HTML gets from can be in the form of JSON or XML. JSON or JavaScript Object Notation is used to store and transmit data, which consist of data as key-value pair and arrays. XML or Extensible Markup Language on the other hand, is also used to store and transfer data. However, XML provides namespaces support and has the capability to display data, in which JSON cannot do.

## Data delivery

In implementing a platform, dealing with data is an unavoidable part of it. There will be a time where data needs to be sent or delivered for the platform to use it or display it. Data delivery can be done with data formats of HTML, XML, and JSON. In Django, HTML can be used to deliver data using special Django syntax. Other methods such as XML and JSON have different syntax. XML for example is information wrapped in a tag, while JSON is is in the form of JavaScript Object. These types of data are needed to communicate the data better inbetween the platform so that the platform can be more dynamic.

## Implementation

1. Create mywatchlist app
   
   <img width="663" alt="image" src="https://user-images.githubusercontent.com/112454126/191573273-4b2cb8c8-8805-4afb-924b-12699efba8cd.png">

   Firstly, inside the directory of the Django project, create a new app called mywatchlist using python manage.py startapp <app-name>.

2. Add mywatchlist URL path

   <img width="326" alt="image" src="https://user-images.githubusercontent.com/112454126/191575136-8caff503-ef9a-4c00-8cea-79e9ca8b2a82.png">

   From views.py, the function created (show) before is imported. Then, a path is created in the urlpatterns so that the user can access. http://localhost:8000/mywatchlist
   
3. Create MyWatchList model

   <img width="218" alt="image" src="https://user-images.githubusercontent.com/112454126/191575876-67f84719-d53e-44a5-a266-0958d18f924a.png">

   In models.py inside the mywatchlist app, create a model that has attributes watched, title, rating, release date and review. Migrate and deploy the model schema into the local Django database for views.py to use.

4. Adding data for MyWatchList
   
   <img width="390" alt="image" src="https://user-images.githubusercontent.com/112454126/191577876-01fbf7d4-9ac3-44df-9bb0-687f2abaa619.png">
   
   Create a folder called fixture and create a json file inside the folder. Inside the JSON file add the data for mywatchlist to use and load the data to the local Django database.

5. Feature to show data in HTML, XML, and JSON

   <img width="381" alt="image" src="https://user-images.githubusercontent.com/112454126/191578569-d69bbf84-98eb-456a-9898-b3967f9a6283.png">

   In views.py, create functions that will extract the data from models.py and return it in HTMl, XML and JSON form. For the HTML form, create a folder called templates and create a HTML file inside the folder containing django syntax to use the data and display it.
   
   <img width="365" alt="image" src="https://user-images.githubusercontent.com/112454126/191579152-12cced3e-b39c-457c-9b84-379bf0aae926.png">
   
6. URL Routing for HTML, XML, and JSON
   
   <img width="326" alt="image" src="https://user-images.githubusercontent.com/112454126/191575136-8caff503-ef9a-4c00-8cea-79e9ca8b2a82.png">
   
   In urls.py, create a path for each HTML, XML, and JSON with each of the path showing the data in HTML form for HTML (show_mywatchlist), JSON form (show_json), and XML form (show_xml).
   
  7. Deploy to Heroku
  
  To deploy to Heroku, firstly, create an app in your Heroku account. Then, copy API Key from your Heroku account and add 2 new repository secrets with your Heroku app name and Heroku API Key. Lastly, re-run the failed workflows. After the deployment status becomes successful, the application can be accessed from the link at the top of this file.
  
  
## Postman
   
   ![messageImage_1663774972583](https://user-images.githubusercontent.com/112454126/191580521-8bd9bbee-01f6-4f3b-80bf-6f749db58051.jpg)

   ![messageImage_1663774905545](https://user-images.githubusercontent.com/112454126/191580580-2940df66-44c4-47ae-8a76-b30017249907.jpg)

   ![messageImage_1663774933859](https://user-images.githubusercontent.com/112454126/191580615-410330c2-7b5d-4fc8-b387-fb73ec780a29.jpg)

## Tests

<img width="375" alt="image" src="https://user-images.githubusercontent.com/112454126/191580896-ee007a0d-4841-465e-9d5b-60def03400a8.png">

   Create tests for each of the url of the HTML, XMl, and JSON to check if they return an HTTP 200 OK response.

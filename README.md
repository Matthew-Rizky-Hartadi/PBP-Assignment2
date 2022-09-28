## Link Heroku App

https://pbp-assignment-2-matthew.herokuapp.com/

To Do List website: https://pbp-assignment-2-matthew.herokuapp.com/todolist/

## CSRF Token

When making a form in a django application, inside the form element there is usually a CSRF token. What is a CSRF Token? It is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources. You can achieve this by using a cryptographic strength pseudo-random number generator (PRNG), seeded with the timestamp when it was created and a static secret. This presents an additional obstacle to a malicious user who attempts to analyze the tokens based on a sample that is issued to him.

If there is no CSRF Token in the form, it allows the possibility of a malicious user or website to make an unsuspecting user perform an action on your site which they didn't want to happen. An example would be an external site could craft a form which POSTs your site and perform unwanted action. If a site has a shopping cart which dousn;t use CSRF tokens, a malicious site could create a form with a button saying register but actually does something else.

## Form as Table

Generally when making a form in a django application, you would use {{ form.as_table }}. This will render the form created in django as a table. However, it is possible to create a form without {{ form.as_table }}. To display the form you have to first make it inside the table tag to render it as a table. If you want to make it manually, you can iterate over the form fields in the html rather than using as_table. Another way of doing it is to refer to the form fields one by one. Manually creating the form will allow the developer to have more freedom in styling the table form. One method is to implement Bootstrap css to the elements of the form.

## Data Flow

<img width="239" alt="image" src="https://user-images.githubusercontent.com/112454126/192823758-1e48cc03-e03e-4c83-b83c-92b697806614.png">

<img width="477" alt="image" src="https://user-images.githubusercontent.com/112454126/192823895-547425f2-bf20-4046-a33b-70afb6e64378.png">

From the form provided in the HTML form, the user would be able to  create a new title and description for the to do list. 

<img width="501" alt="image" src="https://user-images.githubusercontent.com/112454126/192824532-993b970c-ab33-45a9-8ece-9b7a5952f490.png">

After the user clicks Add, the function in views.py to create task would check if the method of the request is POST (which in this case it is). It would then get the content of each inside the title and description input to check. If both of the content exists, it will create an object to the Task database based on the Task model according to the retrieved information and also the date. Then, it will redirect the user to the to do list page. 

<img width="334" alt="image" src="https://user-images.githubusercontent.com/112454126/192826856-83a05f0d-ceb2-4791-bd59-da22ac703445.png">

In the show_todolist function, it will retrieve the items form the Task objects that have been made based on if the user is request.user. It will then return the context of it to the todolist.html.

<img width="285" alt="image" src="https://user-images.githubusercontent.com/112454126/192827279-0d3c67b9-064c-4270-beb4-6e8b63738922.png">

The code in the html file would then iterate the list_item variable that contains the objects that have been retrieved from the show_todolist function in views.py and display the data that have saved in the database to the user.

<img width="470" alt="image" src="https://user-images.githubusercontent.com/112454126/192827566-4cf8d243-42fa-42fd-a293-f1d42a3e2d22.png">



## Implementation

1. Create mywatchlist app
   
   <img width="652" alt="image" src="https://user-images.githubusercontent.com/112454126/192828285-98e18003-bdb8-45a8-94c3-5bf0d3d7d960.png">

   Firstly, inside the directory of the Django project, create a new app called todolist using python manage.py startapp <app-name>.

2. Add todolist URL path

   <img width="488" alt="image" src="https://user-images.githubusercontent.com/112454126/192828531-612497ba-ec4a-41ff-8e75-bb22b5445c75.png">

   From views.py, the function created (show) before is imported. Then, a path is created in the urlpatterns so that the user can access. http://localhost:8000/todolist/
   
3. Create Task model

   <img width="349" alt="image" src="https://user-images.githubusercontent.com/112454126/192828835-be758aed-973d-4f43-824b-1b1b17b8f303.png">

   In models.py inside the todolist app, create Task model that has attributes user, date, title, and description. Migrate and deploy the model schema into the local Django database for views.py to use.

4. Implement the registration, login, and logout forms
   
   <img width="425" alt="image" src="https://user-images.githubusercontent.com/112454126/192829222-b4f3a691-c933-44a0-931c-01b17a5e0885.png">
   
   <img width="299" alt="image" src="https://user-images.githubusercontent.com/112454126/192829291-fcb6fea5-6e63-46a2-901d-72ed9a27350d.png">

   In views.py, create functions to handle registration, login and logout forms so that the users can use the To Do List app properly. Create the html files for the registration and login forms as well.
   
   <img width="605" alt="image" src="https://user-images.githubusercontent.com/112454126/192830322-be2a8e40-a55f-4319-99ef-1760140d2cd2.png">

   <img width="588" alt="image" src="https://user-images.githubusercontent.com/112454126/192830445-5df5d025-27b3-4213-adf9-8bcb90ac1198.png">


5. Create a main page

   <img width="468" alt="image" src="https://user-images.githubusercontent.com/112454126/192830734-a3ee9897-37ef-4460-a40c-de5bd49a104c.png">
   
   <img width="648" alt="image" src="https://user-images.githubusercontent.com/112454126/192830832-ea6a5bbd-0625-4133-bcd3-ac624993cdc8.png">

<img width="621" alt="image" src="https://user-images.githubusercontent.com/112454126/192830887-2f6b5370-9fe7-40ad-9034-cd2746b2ec3e.png">

   Create a html file to display the main page containing the user's username, a table containing the task creation date, task title, and task description, and also an Add New Task button. 
   
   
6. Form to add task
   
   <img width="220" alt="image" src="https://user-images.githubusercontent.com/112454126/192832333-91eb9364-857b-49c9-8184-41a0af188d5a.png">
   
   <img width="686" alt="image" src="https://user-images.githubusercontent.com/112454126/192832544-da17d6a7-334e-44cd-a2e0-079b792e1867.png">
   
   Create a new page where the users can input a form containing the title and description of a new task that is being added.

7. Routing
   
   <img width="498" alt="image" src="https://user-images.githubusercontent.com/112454126/192833276-57787fbd-ccd9-4f52-b086-dedb33b18c22.png">

   In urls.py, create routing to each of the todolist, register, login, logout, and create-task. The todolist would be the main page containing the to do list table, the login would have the login form. the register would contain the account registration form. THe create-task would go to the task creation form page. And lastlyb the logout would log the user out and redirect to the login page.   

8. Deploy to Heroku
  
  To deploy to Heroku, firstly, create an app in your Heroku account. Then, copy API Key from your Heroku account and add 2 new repository secrets with your Heroku app name and Heroku API Key. Lastly, re-run the failed workflows. After the deployment status becomes successful, the application can be accessed from the link at the top of this file.
  
9. Creating user accounts and date
   
   <img width="541" alt="image" src="https://user-images.githubusercontent.com/112454126/192835685-38f327f4-a9c3-43f5-bc53-55d92526c2a5.png">

   <img width="504" alt="image" src="https://user-images.githubusercontent.com/112454126/192835888-3fd2a705-e978-4387-8b7a-c319c9f82fc2.png">

   
   <img width="508" alt="image" src="https://user-images.githubusercontent.com/112454126/192835597-fb9ddd7b-d4d0-4cf3-b633-2df01e6deb61.png">

   <img width="461" alt="image" src="https://user-images.githubusercontent.com/112454126/192835439-38a11c92-c7c0-4a16-b5ae-9840f1b22cfd.png">

   Register and create two accounts and add three datas to each account.
  

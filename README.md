## Link Heroku App

https://pbp-assignment-2-matthew.herokuapp.com/

To Do List website: https://pbp-assignment-2-matthew.herokuapp.com/todolist/

## CSS

CSS can be divided into three types, namely inline, internalA, and external CSS. These types are differentiated based on the position of the CSS code. Inline CSS would have the CSS code inside of the HTML tag. Internal CSS would have the CSS code in a style tag in the HTML file (<style></style>). Lastly, external CSS would create a new CSS file, and then linked to the HTML file from the link tag. Each type has its pros and cons. You can easily and quickly insert CSS rules to an HTML page with inline CSS. That’s why this method is useful for testing or previewing the changes, and performing quick-fixes to your website, but, Adding CSS rules to every HTML element is time-consuming and makes your HTML structure messy. With internal CSS, since you’ll only add the code within the same HTML file, you don’t need to upload multiple files, however, it would increase the page's size and loading time. For external CSS, since the CSS code is in a separate document, your HTML files will have a cleaner structure and are smaller in size. But, Your pages may not be rendered correctly until the external CSS is loaded.

## HTML5 Tag

a = defines a hyperlink

b = displays text in bold style

body = defines the document's body

br = produces single line break

button = creates a clickable button

div = specifies a division or section

footer = represents the footer of the document

form = defines an HTML form for user input

header = represents the header of a document

h1 - h6 = defines HTML headings

html = efines the root of an HTML document

img = represents an image

input = defines an input control

li = defines a list item

link = defines the relationship between the current document and an external resource

and many more.

## CSS selectors

:active = selects an active link

::after = insert something after the content of each <p> element
  
::before = insert something before the content of each <p> element

:checked = selects every checked input element

:focus = selects the input element which has focus
   
:hover = selects links on mouse over
 
:link = selects all unvisited links

:nth-child(n) = selects every <p> element that is the second child of its parent

:valid = selects all input elements with a valid value
   
and many more. 

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
  

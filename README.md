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

1. Customizing the pages using CSS
  
  In the main page, cards are created for each of the task. In the HMTL file, the information of the tasks are iterated inside a card class to make the information inside the card.
  
  <img width="308" alt="image" src="https://user-images.githubusercontent.com/112454126/194201161-036c8d91-a7da-43ee-a611-8b4eafd0f1f9.png">

  Add the css to make the card and the effects
  
  <img width="292" alt="image" src="https://user-images.githubusercontent.com/112454126/194201368-3d2f3b4d-7d4a-4418-84fe-9f683bbbb758.png">

  <img width="240" alt="image" src="https://user-images.githubusercontent.com/112454126/194201570-50c32eaa-ecc2-4a43-90fb-6237390d316a.png">

  Add CSS to the login, register and create-task pages as well with the added corresponding classes.
  
  <img width="390" alt="image" src="https://user-images.githubusercontent.com/112454126/194204109-689aa73d-2249-483a-9072-fec5e7edbd74.png">

  <img width="395" alt="image" src="https://user-images.githubusercontent.com/112454126/194204156-619d21d0-edd8-478f-854b-a6afdfb07f92.png">
  
  <img width="383" alt="image" src="https://user-images.githubusercontent.com/112454126/194204233-d4e5f128-bc7a-4b3e-bd31-04307675c007.png">

  

2. Deploy to Heroku
  
  To deploy to Heroku, firstly, create an app in your Heroku account. Then, copy API Key from your Heroku account and add 2 new repository secrets with your Heroku app name and Heroku API Key. Lastly, re-run the failed workflows. After the deployment status becomes successful, the application can be accessed from the link at the top of this file.
  

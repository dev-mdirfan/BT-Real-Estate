# BT Real Estate project

- The project is for a client called BT Real Estate who wants a website with an admin area.
- The project resources include a folder called "btre resources" with an app requirements document, logo files, and various images.
- The logo is a simple design with a white version and a dark version available.
- There are images for the site, including a showcase image, a building image for the background, and an about images.
- The app requirements document outlines front-end pages, design specifications, and required functionality such as managing listings, realtors, contact inquiries, and website users through the admin area. Pagination, search functionality, and displaying realtors on the about page are also mentioned.

All [resources]() can be found in Release Section.

**BT Meaning:**

The meaning of "BT" in the project title "BT Real Estate" could have multiple interpretations.

1. Acronym: "BT" could potentially represent "Best Transaction" indicating that the platform aims to provide a superior and efficient property buying/selling experience.

2. Branding: "BT" could be a unique branding element chosen by the project's creators. It might not have a specific meaning but serves as a distinct and memorable name for the real estate web application.

Ultimately, it's essential to clarify this during an interview by explaining that the meaning of "BT" may vary depending on the project's context and purpose.

## TABLE OF CONTENT

<!-- TOC -->
- [BT Real Estate project](#bt-real-estate-project)
  - [TABLE OF CONTENT](#table-of-content)
  - [Project Overview](#project-overview)
    - [Theme](#theme)
  - [Virtual Environment](#virtual-environment)
    - [Commands](#commands)
  - [Django Install](#django-install)
  - [Initial Files running server](#initial-files-running-server)
  - [5.1. Creating Pages App](#51-creating-pages-app)
  - [5.2. Page Templates Base Layout](#52-page-templates-base-layout)
  - [5.3. Static Files Path](#53-static-files-path)
  - [5.4. Bootstrap Layout Markup](#54-bootstrap-layout-markup)
  - [5.5 Index About Linking](#55-index-about-linking)
  - [5.6. Listing URLs templates](#56-listing-urls-templates)
  - [6.1. Install Postgres PgAdmin](#61-install-postgres-pgadmin)
  - [6.2. Django Postgres Setup Migrate](#62-django-postgres-setup-migrate)
  - [6.3. Planning Our Schemas](#63-planning-our-schemas)
  - [6.4. Create Listing Model](#64-create-listing-model)
  - [6.5. Realtor Model Run Migrations](#65-realtor-model-run-migrations)
  - [Create Super User Register Models With Admin](#create-super-user-register-models-with-admin)
  - [6.6. Media Folder Adding Data](#66-media-folder-adding-data)
  - [6.7. Admin Logo CSS](#67-admin-logo-css)
  - [6.8. Customize Admin Display Data](#68-customize-admin-display-data)
  - [7.1. Pull Data From Listings Model](#71-pull-data-from-listings-model)
  - [7.2. Display Listings In Template](#72-display-listings-in-template)
  - [7.3. Pagination Order Filter](#73-pagination-order-filter)
  - [7.4. Home About Page Dynamic Content](#74-home-about-page-dynamic-content)
  - [7.5. Single Listing Page](#75-single-listing-page)
  - [7.6. Search Form Choices](#76-search-form-choices)
  - [7.7. Search Form Filtering](#77-search-form-filtering)
  - [7.8. Preserving Form Input](#78-preserving-form-input)
  - [8.1. Accounts App URLs](#81-accounts-app-urls)
  - [8.2. Register Login Templates](#82-register-login-templates)
  - [8.3. Message Alerts](#83-message-alerts)
  - [8.4. User Registration](#84-user-registration)
  - [8.5. User Login](#85-user-login)
  - [8.6. Logout Navbar Auth Links](#86-logout-navbar-auth-links)
  - [8.7. Dynamic Page Titles](#87-dynamic-page-titles)
  - [9.1. Contacts App Model](#91-contacts-app-model)
  - [9.2. Contacts Admin Customization](#92-contacts-admin-customization)
  - [9.3. Contact Form Prep](#93-contact-form-prep)
  - [9.4. Contact Form Submission](#94-contact-form-submission)
  - [9.5. Inquiry Check Send Email](#95-inquiry-check-send-email)
  - [9.6. Dashboard Functionality](#96-dashboard-functionality)
  - [10.1. Pushing To Github](#101-pushing-to-github)
  - [10.1. Droplet Setup SSH Keys](#101-droplet-setup-ssh-keys)
  - [10.1.](#101)
  - [10.1.](#101-1)
  - [10.1.](#101-2)
  - [10.1.](#101-3)
  - [10.1.](#101-4)
  - [10.1.](#101-5)
  - [10.1.](#101-6)
  - [10.1.](#101-7)

<!-- TOC -->

## Project Overview

- App Requirements
- Images ( main home page, background, about page)
- Logos (white and dark version - photoShop)
- Realtor (Team members)
- Themes

### Theme

- Branding color
- css
- html
- js
- jquery
- sass
- lightbox - (image slider)

About Bootstrap Theme -

- The speaker discusses a Bootstrap theme that will be used in the course.
- They mention the possibility of creating the theme from scratch in a tutorial on their YouTube channel.
- The theme includes HTML pages, compiled assets, and customized Bootstrap colors using SASS.
- The theme also includes Font Awesome, jQuery, and a lightbox solution called Lightbox 2.
- The speaker describes the structure and components of the theme, including the homepage, inner pages, listings page, search page, register page, login page, and dashboard.

## Virtual Environment

- The transcript discusses the importance of creating a virtual environment in Python to isolate packages and dependencies within a project.
- For Python 3.6 and newer versions, the built-in `venv` package can be used to create the virtual environment by running `python3 -m venv <path>`.
- The user's text editor of choice is Visual Studio Code (VS Code), and they create a project directory named "btre_project" within the "Dev" folder.
- To activate the virtual environment on macOS, the command is `source ./venv/bin/activate`. On Windows, the command is `.\venv\Scripts\activate.bat`.
- When activated, the Python version changes to the one specified in the virtual environment (Python 3 in this case), and packages installed will be confined to the virtual environment.

Note: Some parts of the transcript may not be directly relevant to setting up the virtual environment but rather explain the user's actions and setup for the tutorial/course they are following. The summary focuses on the essential points related to virtual environment creation and activation.

### Commands

Open VS Code:
```shell
code .
```

Check installed modules/packages-
```shell
pip freeze
```

Create env file
```shell
python -m venv ./venv
```

activate
```shell
.\venv\Scripts\activate
```

deactivate
```shell
deactivate
```

## Django Install

- Created virtual environment with folder named "btre project" and virtual environment named "venv" for Mac (source bin/activate) and Windows (venv\Scripts\activate.bat).
- Installed Django inside the virtual environment using "pip install Django".
- Explained Django's project and app structure; used "Django-admin startproject btre ." to create a project called "btre" with necessary files.
- Addressed VS Code setup issues with virtual environment by selecting the correct interpreter.
- Initialized Git repository using "git init" and created a ".gitignore" file to exclude certain files and directories, including the virtual environment folder "venv".

Install django
```shell
pip install django
```

update pip version
```shell
python.exe -m pip install --upgrade pip
```

django special CLI command
```shell
django-admin help
```

Create project
```shell
django-admin startproject btre .
```

`manage.py` commands
```shell
python manage.py help
```

create `.gitignore` 
```gitignore
*.log
*.pot
*.pyc
___pycache__/
local_settings.py
db.sqlite3
/media
venv
/static
```

## Initial Files running server

- The video introduces the concept of running the Django server locally using the Dev server, which is included with Django for local development purposes.

- During the process of running the server, certain files are generated. One of them is the "DB.sqlite3" file, which serves as the storage location for data when using the SQLite database. It is mentioned that SQLite is not recommended for production applications. Additionally, the "pi cache" folder is created by the server to improve program startup time by recompiling scripts when changes are made.

- The "init.py" file is discussed briefly, stating that it is typically empty and doesn't require any modifications. It is used to enable the usage of files as packages and prevent conflicts with common directory names.

- The importance of the "settings.py" file is emphasized. It contains various configurations and imports the OS module to determine the project's base directory. Key aspects covered in the settings file include the security key (used to protect sensitive information), debug mode (set to true for development and false for production), allowed hosts (domains that the website can serve), installed apps (default and custom apps), middleware (functions that handle HTTP requests and responses), templates (location and options for HTML templates), and database settings.

- The "urls.py" file, responsible for routing within the Django application, is discussed. It contains a list of URL patterns and their associated view methods or links to other URL files. It is highlighted that individual apps can have their own "urls.py" files, which can be included in the main "urls.py" file to organize the routing structure.

- The "wsgi.py" file is briefly mentioned as part of the web server Gateway interface. Its purpose is to enable communication between the web server and web applications, allowing for the processing of requests. Hosting the site and making it accessible to others relies on this file.

- Finally, it is mentioned that the next step in the video tutorial is to create the first app called the "Pages" app. This app will handle static pages such as the home page and about page.

Runserver
```shell
python manage.py runserver
```
port: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

before deployment:
- hide secret_key
- change debug to false

wsgi: web server gateway interface

## 5.1. Creating Pages App

Step 1: Create the "Pages" app
- Open a terminal and make sure you are in your virtual environment.
- Run the following command to create the "pages" app: `python manage.py startapp pages`
- This command will generate a new folder called "pages" with several files inside it.

Step 2: Add the "Pages" app to settings
- Open the "btre/settings.py" file.
- Find the "INSTALLED_APPS" list and add the following line: `'pages.apps.PagesConfig',`
- This configuration tells Django to recognize the "pages" app as part of the project.

Step 3: Create a "urls.py" file for the "Pages" app
- Inside the "pages" folder, create a new file called "urls.py".
- Import the necessary modules:
```python
from django.urls import path
from . import views
```
- Define the URL patterns for the app:
```python
urlpatterns = [
    path('', views.index, name='index'),
]
```
- This code sets up a URL pattern for the root path ('') and connects it to the "index" view.

Step 4: Implement the "index" view
- Open the "views.py" file inside the "pages" folder.
- Remove any existing code and define the "index" method:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello, world!</h1>')
```
- This method takes a request object as a parameter and returns an HTTP response with the "Hello, world!" message.

Step 5: Include the "Pages" URLs in the main URLs file
- Open the "btre/urls.py" file.
- Import the necessary module:
```python
from django.urls import path, include
```
- Add the "pages" app's URLs to the URL patterns:
```python
urlpatterns = [
    # ...
    path('', include('pages.urls')),
    # ...
]
```
- The `include` function allows you to include the URLs defined in the "pages" app's "urls.py" file.

That's it! By following these steps, you should have successfully created the "Pages" app, defined its URL patterns, and connected them to the "index" view, which displays a "Hello, world!" message.

## 5.2. Page Templates Base Layout

1. Configuring Template Directories:
   - Open the `settings.py` file in your Django project.
   - Locate the `TEMPLATES` list and find the `DIRS` key-value pair.
   - Add the following code to specify the template directory:
     ```python
     import os
     
     # ...
     
     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     
     # ...
     
     TEMPLATES = [
         {
             # ...
             'DIRS': [os.path.join(BASE_DIR, 'templates')],
             # ...
         },
     ]
     ```

2. Creating Template Folders and Files:
   - In the root directory of your project, create a folder called `templates`.
   - Inside the `templates` folder, create a folder called `pages`.
   - Within the `pages` folder, create two files: `index.html` and `about.html`.
   - Add the following content to `index.html`:
     ```html
     <h1>Home</h1>
     ```
   - Add the following content to `about.html`:
     ```html
     <h1>About</h1>
     ```

3. URL Configuration in `urls.py`:
   - Open the `urls.py` file of your Pages app.
   - Add a new import statement at the top:
     ```python
     from django.urls import path
     ```
   - Add the following code to the URL patterns:
     ```python
     from . import views
     
     urlpatterns = [
         path('', views.index, name='index'),
         path('about/', views.about, name='about'),
     ]
     ```

4. Creating Views:
   - Open the `views.py` file of your Pages app.
   - Add the following import statement at the top:
     ```python
     from django.shortcuts import render
     ```
   - Define the `index` and `about` view functions:
     ```python
     def index(request):
         return render(request, 'pages/index.html')
     
     def about(request):
         return render(request, 'pages/about.html')
     ```

5. Creating the Base Layout:
   - Inside the `templates` folder (not within `pages`), create a file called `base.html`.
   - Add the following content to `base.html`:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <title>BT Real Estate</title>
         <!-- Add any CSS or JavaScript references here -->
     </head>
     <body>
         {% block content %}{% endblock %}
     </body>
     </html>
     ```

6. Extending the Base Layout:
   - Open the `index.html` file within the `pages` folder.
   - Add the following code at the top of the file:
     ```html
     {% extends 'base.html' %}
     ```
   - Wrap the existing content with the following tags:
     ```html
     {% block content %}
     <!-- Existing content goes here -->
     {% endblock %}
     ```
   - Repeat the same steps for the `about.html` file.

Remember to save all your changes and ensure that your Django server is running. Accessing the URLs should now render the corresponding templates with the base layout applied.

## 5.3. Static Files Path

Step-by-step code explanations:

1. Create a 'static' folder within the 'btre' project folder:
```bash
cd /path/to/btre
mkdir static
```

2. Copy the CSS, JS, and web fonts folders from the 'assets' folder to the newly created 'static' folder:
```bash
cp -r /path/to/btre_theme/assets/css /path/to/btre/static/
cp -r /path/to/btre_theme/assets/js /path/to/btre/static/
cp -r /path/to/btre_theme/assets/webfonts /path/to/btre/static/
```

3. Create an 'IMG' folder within the 'static' folder and copy the required images:
```bash
cd /path/to/btre/static
mkdir IMG
cp -r /path/to/btre_theme/assets/img/lightbox /path/to/btre/static/IMG/
cp -r /path/to/btre_theme/assets/img/image1.jpg /path/to/btre/static/IMG/
cp -r /path/to/btre_theme/assets/img/image2.jpg /path/to/btre/static/IMG/
# Repeat the above line for other required images if needed
```

4. Open the 'settings.py' file located at '/path/to/btre/btre/settings.py'.

5. Add the following lines to the 'settings.py' file to configure the static root and static files directories:
```python
import os

# ... other configurations ...

STATIC_URL = '/static/'

# Define the location where 'collectstatic' will put all static files during deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Add the location of the static folder we just created to 'STATICFILES_DIRS'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static'),
]

# ... other configurations ...
```

6. Add 'static/' and 'media/' to the '.gitignore' file (if not already present) to prevent pushing these folders to the repository:
```
/static
/media
```

7. Save the 'settings.py' and '.gitignore' files.

8. Now, you can run the 'collectstatic' command to gather all static files from your apps and place them in the 'STATIC_ROOT' directory:
```bash
cd /path/to/btre
python manage.py collectstatic
```

9. Finally, you can proceed to bring in the bootstrap theme and markup into your Django application, which is not covered in this specific transcript.

## 5.4. Bootstrap Layout Markup

Sure! Here are the step-by-step codes for implementing a Bootstrap theme in a Django project:

1. Organizing static files:
   - Create a folder called "btre" in your project's root directory.
   - Inside the "btre" folder, create another folder called "static".
   - Move all the necessary static files (such as CSS, JavaScript, fonts) related to the theme into the "static" folder.
   - Additionally, keep the "admin" static files in the root "static" folder.

2. Editing base HTML layout:
   - Open the base HTML layout file, located in the "templates" folder.
   - Add the necessary CSS and JavaScript file references from the Bootstrap theme into the head section of the HTML file.
      ```html
      <!-- Font Awesome -->
      <link rel="stylesheet" href="{% static 'css/all.css' %}">
      <!-- Bootstrap -->
      <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
      <!-- Custom -->
      <link rel="stylesheet" href="{% static 'css/style.css' %}">
      <!-- Lightbox -->
      <link rel="stylesheet" href="{% static 'css/lightbox.min.css' %}">
      ```
   - Copy the JavaScript script tags from the theme's index.html file and paste them above the closing body tag in the base HTML file.
      ```html
      <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
      <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
      <script src="{% static 'js/main.js' %}"></script>
      <script src="{% static 'js/lightbox.min.js' %}"></script>
      ```

3. Referencing static files using template tags:
   - Replace the static file references in the HTML file with template tags that point to the correct static files.
      ```html
      <link rel="stylesheet" href="{% static 'CSS/all.css' %}">
      <link rel="stylesheet" href="{% static 'CSS/bootstrap.css' %}">
      <link rel="stylesheet" href="{% static 'CSS/style.css' %}">
      <link rel="stylesheet" href="{% static 'CSS/lightbox.min.css' %}">
      ```
      Note: Make sure to remove any incorrect file paths or unnecessary "assets" folders from the references.

4. Adding common elements to base HTML layout:
   - Copy the necessary HTML markup for the top bar and nav bar from the theme's index.html file.
   - Paste the markup above the "block content" section in the base HTML file.
      ```html
      <!-- Top Bar -->
      <div class="top-bar">
        <!-- Top Bar HTML markup goes here -->
      </div>

      <!-- Nav Bar -->
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <!-- Nav Bar HTML markup goes here -->
      </nav>
      ```

5. Creating partials:
   - Create a new folder called "partials" inside the "templates" folder.
   - Inside the "partials" folder, create separate HTML files for the top bar, nav bar, and footer.
   - Prefix the filenames with an underscore to indicate that they are partials (e.g., "_topbar.html", "_navbar.html", "_footer.html").
   - Copy the respective HTML markup from the base HTML file and paste it into the corresponding partial files.

6. Including partials in base HTML layout:
   - Replace the copied HTML markup in the base HTML file with template tags that include the partials.
     ```html
     <!-- Top Bar -->
     {% include 'partials/_topbar.html' %}
     <!-- Navbar -->
     {% include 'partials/_navbar.html' %}
     <!-- Main Content -->
     {% block content %} {% endblock %}
     <!-- Footer -->
     {% include 'partials/_footer.html' %}
     ```

## 5.5 Index About Linking

Apologies for the previous incomplete response. Here's the complete step-by-step breakdown:

Step 1: Working on Layout and Base HTML
- The video begins by explaining that the layout is being handled using Bootstrap.
- The top bar, nav bar, and footer are essential components that should be present on every page, so they are added to the base HTML file.
- Static assets, such as CSS files, JavaScript files, and images, are linked using the `load static` function. This ensures that the project can access and display these static files.

Step 2: Working on the Index Page
- Open the Sublime Text editor with the theme that contains the HTML code.
- Copy the code starting from the bottom (above the footer) and going up until just below the nav bar.
- Paste the copied code into the `index.html` file in your Django app.
- It's important to note that the current content is static and won't have full functionality until further development is done, including creating models and connecting to a database.
- Save the `index.html` file and reload the page in the browser. This should display a basic shell of the application.

Step 3: Working on the About Page
- Open the `about.html` file in your theme in the Sublime Text editor.
- Select and copy the code between the nav bar and the footer.
- Paste the copied code into the `about.html` file in your Django app.
- Note that there is a static image on the page that needs to be included.
- Modify the code that loads the image (`about.jpeg`) to use the `load static` function.
- Save the modified `about.html` file and reload the page in the browser to see the image.

Step 4: Implementing Linking
- Links need to be added to the project, such as in the breadcrumbs and the navigation bar.
- Open the `index.html` file and locate the section where the breadcrumb link is specified.
- Replace the existing URL with a URL template using the syntax `{% url 'index' %}` to generate the URL for the index page.
- Repeat the same process for the home and about links in the navigation bar.
- Open the `about.html` file and modify the code to include the URL template for the about page using `{% url 'about' %}`.
- Save the modified files and reload the pages in the browser to verify that the links function correctly.

Step 5: Handling Link Highlighting
- Address the issue of active link highlighting in the navigation bar.
- The `active` class is responsible for highlighting the active link.
- Conditional statements are used to dynamically apply the `active` class based on the current page.
- Open the `index.html` file and locate the code for the home link in the navigation bar.
- Modify the code to include a conditional statement that checks if the current page is the home page using the syntax `{% if request.path == '/' %}`.
- If the condition is met, add the `active` class to the link using `class="nav-link active"`, otherwise, omit the `active` class.
- Repeat the same modification for the about link.
- Save the modified `index.html` file and reload the page in the browser to observe the active link highlighting.

Note: The video concludes by mentioning that the focus is on building the front-end UI before diving into database-related tasks, such as creating models and setting up the admin area.

Conditionals in jinja:
```html
<li
        {% if '/' == request.path %}
class="nav-item active mr-3"
{% else %}
class="nav-item mr-3"
{% endif %}
>
```
x`

## 5.6. Listing URLs templates

Sure! Here are the step-by-step codes for the process described in the transcript:

1. Create the "listings" and "Realtors" apps:
   ```
   python manage.py startapp listings
   python manage.py startapp Realtors
   ```

2. Create templates for the "listings" app:
   - Create a folder called "listings" inside the "templates" directory.
   - Inside the "listings" folder, create three HTML templates: "listing.html," "listings.html," and "search.html."

3. Create the URLs file for the "listings" app:
   - Create a file called "urls.py" inside the "listings" app folder.
   - Copy the following code into the "urls.py" file:
     ```python
     from django.urls import path
     from . import views
     
     app_name = 'listings'
     
     urlpatterns = [
         path('', views.index, name='index'),
         path('<int:listing_id>/', views.listing, name='listing'),
         path('search/', views.search, name='search'),
     ]
     ```

4. Add the "listings" and "Realtors" apps to the settings file:
   - Open the "settings.py" file in your project's directory.
   - Find the `INSTALLED_APPS` list and add the following lines:
     ```python
     'listings',
     'Realtors',
     ```

5. Create view methods for the "listings" app:
   - Inside the "views.py" file of the "listings" app, add the following code:
     ```python
     from django.shortcuts import render
     
     def index(request):
         return render(request, 'listings/listings.html')
     
     def listing(request, listing_id):
         return render(request, 'listings/listing.html')
     
     def search(request):
         return render(request, 'listings/search.html')
     ```

6. Update the base HTML template:
   - In the base HTML template file (e.g., "base.html"), add the following code inside the `<body>` tag:
     ```html
     {% block content %}
     {% endblock %}
     ```

7. Update the "listings.html" template:
   - Extend the base HTML template by adding the following code at the top of the "listings.html" file:
     ```html
     {% extends 'base.html' %}
     ```
   - Replace the existing content of the "listings.html" file with the desired content, such as headers, images, and listings information.

That's it! You have now created the "listings" app with templates, URLs, and view methods. Repeat similar steps for the "Realtors" app if necessary.

## 6.1. Install Postgres PgAdmin

Step 1: Database Setup

- The speaker recommends using PostgreSQL as the database for the Django project.
- For Windows users, they suggest going to postgresql.org, clicking on "Download," and selecting the graphical installer. The specific version mentioned is 10, but you can choose a different version if desired.
- For Mac users, they recommend using the PostgreSQL app, which can be downloaded from postgresapp.com.
- Additionally, they mention a tool called PGAdmin, which provides a graphical interface for managing databases. It is available for both Windows and Mac.

Step 2: PostgreSQL Installation on Mac

- Download the PostgreSQL app from postgresapp.com.
- Open the downloaded file and drag the PostgreSQL app to the Applications folder.
- Double-click the PostgreSQL app to open it. If prompted, click "Open" to proceed.
- If it's your first time installing PostgreSQL, you will see an "Initialize" button. Click it to initialize the server.
- The server settings will be displayed, including the port number, data directory, and config file. You can edit these settings if needed.
- Double-click on "postgres" to open a terminal with the PostgreSQL shell.

Step 3: Creating a Database and User

- In the PostgreSQL shell, use the following command to set a password for the "postgres" user:
  ```
  \password postgres
  ```
- Enter a password when prompted.
- Create a new database named "btreDB" with the owner set as the "postgres" user. Run the following command:
  ```sql
  create database btreDB owner postgres;
  ```

Step 4: Installing PGAdmin

- Download PGAdmin from the official website based on your operating system (Windows or Mac).
- Install PGAdmin by moving the downloaded file to the Applications folder (for Mac users) or running the executable file (for Windows users).

Step 5: Configuring PGAdmin

- Open PGAdmin. You may need to agree to the terms and conditions.
- If you installed PGAdmin using the PostgreSQL app, move the application to the Applications folder (for Mac users).
- Run PGAdmin 4, and when prompted, click "Open" to start the program.
- PGAdmin runs in the browser. Under the "Servers" section on the left, there might be no servers listed initially.
- To create a server manually, click "Create Server" and give it a name (e.g., "DB Server").
- In the "Connection" section, specify that it's a local host connection. Use the username "postgres" and the password set earlier in the PostgreSQL shell.
- Click "Save" to create the server.
- Under the "Databases" section, you should see the "btreDB" database, along with other default databases.

In the next video, the speaker plans to configure Django to use PostgreSQL instead of SQLite and proceed with migrations and working with models.

## 6.2. Django Postgres Setup Migrate

Sure! Here's a step-by-step guide with codes to summarize the process described in the transcript:

Step 1: Install Postgres and required packages
- Install Postgres on your system.
- Activate your virtual environment.
- Install the required packages, "Psycopg2" and "Dash binary," using pip.

```shell
pip install psycopg2
pip install psycopg2-binary
```

Step 2: Update Django app settings
- Open the `settings.py` file in your Django project.
- Locate the section related to the database settings.
- Change the database engine from `sqlite3` to `django.db.backends.postgresql`.
- Update the `NAME` parameter with your desired database name (e.g., "btre_db").
- Add the `USER`, `PASSWORD`, and `HOST` parameters specific to your Postgres configuration.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btre_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Step 3: Apply existing migrations
- Stop the Django development server if it is running.
- Apply the existing migrations to update the database schema.

```shell
python manage.py migrate
```

Step 4: Verify the database changes
- You can check the updated tables either through the terminal or a PostgreSQL administration tool like pgAdmin.
- Restart the Django development server.

```shell
python manage.py runserver
```

That's it! Your Django application should now be connected to a Postgres database, and the necessary tables for Django functionalities will be created. You can proceed to create your own models and migrations for custom tables in the next steps.

## 6.3. Planning Our Schemas

Certainly! Here's a detailed breakdown of the points:

1. Before starting to write code, it's important to map out the database schema. This helps in understanding the required fields for the models.
2. Start by examining the project requirements to identify the data that needs to be displayed on the application and website.
3. Create a text file, such as "schemas.txt," to document the schema. In this case, three separate tables are needed: "listing," "realtor," and "contact."
4. Begin mapping out the fields for the "listing" table. The fields identified include:
   - ID: A unique identifier for each listing (data type: int).
   - Realtor: A foreign key field connecting the realtor table/model to associate a realtor with each listing (data type: integer).
   - Title: The title or name of the listing (data type: string).
   - Address: The street address of the listing (data type: string).
   - City: The city of the listing's location (data type: string).
   - State: The state of the listing's location (data type: string).
   - Zip Code: The ZIP code of the listing's location (data type: string).
   - Description: A text field to provide additional details about the listing (data type: text).
   - Price: The price of the listing (data type: int).
   - Bedrooms: The number of bedrooms in the listing (data type: int).
   - Bathrooms: The number of bathrooms in the listing (data type: int).
   - Garage: The number of garage spaces available (data type: int, default: 0).
   - List Date: The date the listing was added (data type: date).
   - Square Feet: The area of the listing in square feet (data type: int).
   - Lot Size: The size of the lot in acres (data type: float).
   - Is Published: A boolean field indicating if the realtor's listings are published (data type: boolean, default: true).
   - Images: Six image fields for storing image locations (data type: string).

5. Move on to mapping the fields for the "realtor" table:
   - ID: A unique identifier for each realtor (data type: int).
   - Name: The name of the realtor (data type: string).
   - Photo: The photo of the realtor (data type: string).
   - Description: A short description of the realtor (data type: text).
   - Email: The email address of the realtor (data type: string).
   - Phone: The phone number of the realtor (data type: string).
   - Is MVP: A boolean field indicating if the realtor is the "seller of the month" (data type: boolean).
   - Hire Date: The date the realtor was hired (data type: date).

6. Finally, map the fields for the "contact" table:
   - ID: A unique identifier for each contact inquiry (data type: int).
   - User ID: The ID of the user who sent the inquiry (data type: int).
   - Listing: The ID of the listing for containing homes (data type: int).
   - Listing ID: The ID of the listing associated with the inquiry (data type: int).
   - Name: The name of the person sending the inquiry (data type: string).
   - Email: The email address of the person sending the inquiry (data type: string).
   - Phone: The phone number of the person sending the inquiry (data type: string).
   - Message: The message content of the inquiry (data type: string).
   - Contact Date: The date the inquiry was made (data type: date).

By following this schema Requirements

- [BTRE REQUIREMENTS](btre-requirements.md)

## 6.4. Create Listing Model

In the video, the process of creating models in Django for listings is explained. Here are the details and code snippets:

1. Open the `models.py` file in the listings app.
2. Create a class for the Listing model by extending the `models.Model` class, and also Import the necessary modules:
    ```python
    from django.db import models
    ```
3. Create a model for the Listing:
    ```python
    from django.db import models
    from datetime import datetime
    from realtors.models import Realtor
    
    class Listing(models.Model):
        realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
        title = models.CharField(max_length=200)
        address = models.CharField(max_length=200)
        city = models.CharField(max_length=100)
        state = models.CharField(max_length=100)
        zip_code = models.CharField(max_length=20)
        description = models.TextField(blank=True)
        price = models.IntegerField()
        bedrooms = models.IntegerField()
        bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
        garage = models.IntegerField(default=0)
        sq_ft = models.IntegerField()
        lot_size = models.DecimalField(max_digits=5, decimal_places=1)
        photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
        photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
        photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
        photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
        photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
        photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
        photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
        is_published = models.BooleanField(default=True)
        list_date = models.DateTimeField(default=datetime.now, blank=True)
        def __str__(self):
            return self.title
    ```
4. Create a model for the Realtor:
    ```python
    class Realtor(models.Model):
        # Add the necessary fields for the Realtor model
        # ...
    ```

5. Create a migration to apply the models to the database:
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

By running the migration commands, Django will create the necessary tables in the database based on the defined models. The `makemigrations` command generates the migration files, and the `migrate` command applies those migrations to the database.

## 6.5. Realtor Model Run Migrations

Sure! Here are the details along with relevant code snippets:

1. The video focuses on creating a Realtor model that is linked to the Listing model. Both models will go hand in hand, with a foreign key relationship.

2. The Realtor model is created in the models.py file within the Realtors folder. The code snippet for creating the Realtor model is as follows:

    ```python
    from django.db import models
    
    class Realtor(models.Model):
        name = models.CharField(max_length=200)
        photo = models.ImageField(upload_to='photos/%Y/%m/%d')
        description = models.TextField(blank=True)
        phone = models.CharField(max_length=20)
        email = models.EmailField(max_length=50)
        is_mvp = models.BooleanField(default=False)
        hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
        def __str__(self):
            return self.name
    ```

3. Various fields are added to the Realtor model:
   - `name`: CharField with a maximum length of 200 characters.
   - `photo`: ImageField for storing the photo of the Realtor.
   - `description`: TextField for an optional description.
   - `phone`: CharField for the phone number (maximum length of 20 characters).
   - `email`: EmailField for the email address (maximum length of 50 characters).
   - `is_mvp`: BooleanField indicating whether the Realtor is the seller of the month (default is False).
   - `hire_date`: DateTimeField representing the date of hiring the Realtor. It has a default value of the current date and time.

4. To update the database with the new models, migrations need to be created and run using the following commands:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
   
    - These commands generate migration files based on the models and apply those migrations to the database, creating the necessary tables.

5. The migration files are generated and stored in the migrations folders of the respective models (e.g., `listings/migrations` and `realtors/migrations`). The migration files contain information about the operations to be performed on the database.

After running the migrations, the database tables for the Listing and Realtor models are created. You can verify the presence of these tables in the database management system (e.g., PGAdmin) or by querying the tables programmatically.

Note: Make sure to have the necessary dependencies installed, such as "Pillow" for handling image fields, by running `pip install Pillow` before running the migrations.

## Create Super User Register Models With Admin

Step 1: Creating a Superuser
- Open the terminal (VS Code terminal in this case) and ensure your server is running.
- Run the command `python manage.py createsuperuser`.
- Provide a username, email address, and password when prompted. For example:
  - Username: Brad
  - Email address: brad@gmail.com
  - Password: 123456
- When asked if you want to bypass the password validation, enter 'yes' to proceed.

Step 2: Accessing the Admin Area
- Open your web browser and go to `localhost:8000/admin`.
- You should see the Django admin login page.
- Enter the username and password you provided while creating the superuser (e.g., Brad/123456) and click "Log in".
- Now you will have access to the administrator area.

Step 3: Managing Users and Groups
- In the admin area, you can manage users and groups.
- Users can be assigned different groups and permissions.
- You can add, edit, and delete users and groups.

Step 4: Registering Models in the Admin Area
- Open the file `admin.py` inside the "listings" app folder.
- Import the model you want to register. In this case, it's the "Listing" model.
- Add the registration code using `admin.site.register(ModelName)` for each model you want to register. For example:
  ```python
  from .models import Listing
  
  admin.site.register(Listing)
  ```

Step 5: Customizing the Admin Area (optional)
- The admin area can be customized to match your requirements and branding.
- You can change the logo, colors, and how data is displayed.
- Further customization can be done to enhance the user interface and user experience.

Note: The transcript also mentions adding the "Realtors" model to the admin area using similar steps as registering the "Listing" model. However, the specific code for the "Realtors" model is not provided in the transcript.

## 6.6. Media Folder Adding Data

Sure! Here's a step-by-step breakdown of the transcript with relevant code snippets:

1. Define media folder settings:
   - Open the `settings.py` file in VS Code.
   - Add the following code at the very bottom of the file:
     ```python
     # Media folder settings
     media_root = os.path.join(BASE_DIR, 'media')
     media_url = '/media/'
     ```
   - Save the changes.

2. Update the URLs file to handle media files:
   - Open the `urls.py` file in the core BTRE folder.
   - Import the necessary modules at the top of the file:
     ```python
     from django.conf import settings
     from django.conf.urls.static import static
     ```
   - Modify the URL patterns by adding the following code at the end:
     ```python
     urlpatterns = [
         # Your existing URL patterns...
     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     ```
   - Save the changes.

3. Import required modules:
   - Add the following import statements at the top of the file:
     ```python
     from django.conf import settings
     from django.conf.urls.static import static
     ```

4. Add Realtors:
   - Access the admin area and navigate to the "Realtors" section.
   - Click on the "Add Realtor" button.
   - Enter the details for Kyle Brown, such as name, description, phone number, email, and hire date.
   - Save the changes.
   - Repeat the process to add additional Realtors, such as Mark Hudson and Jenny Johnson.

5. Add listings:
   - Go to the "Listings" section in the admin area.
   - Click on the "Add" button to add a new listing.
   - Enter the details for the listing, including title, address, description, price, bedrooms, bathrooms, garage, square feet, lot size, and main photo.
   - Save the changes.
   - Repeat the process to add more listings, providing the necessary details for each listing.

Please note that the code provided in the transcript is incomplete, and it assumes that you have an existing Django project set up with appropriate models and admin configurations. The provided code snippets are intended to be inserted into the relevant files at the appropriate locations based on the given instructions. Make sure to adjust the code as per your project's specific requirements and structure.

## 6.7. Admin Logo CSS

Sure! Here is a step-by-step breakdown with the relevant code snippets:

1. In the video, the presenter wants to customize the admin area of a Django project.

2. They start by creating a new folder called "admin" inside the "templates" directory of the project.

   Code:
   ```
   templates/
   └── admin/
   ```

3. Inside the "admin" folder, they create a new file called "base_site.html". This file will serve as the customized admin template.

   Code:
   ```
   templates/
   └── admin/
       └── base_site.html
   ```

4. In the "base_site.html" file, they extend the existing admin template using the "extends" keyword.

   Code:
   ```html
   {% extends "admin/base.html" %}
   ```

5. The presenter wants to replace the default "Django Administration" text with a company name or logo. They define a new block called "block branding" and add it inside the "extends" statement.

   Code:
   ```html
   {% block branding %}
   <h1 id="head"><img class="brand_img" src="{% static 'img/logo.png' %}" alt="BT Real Estate">Admin Area</h1>
   {% endblock %}
   ```

   Note: In the code snippet above, the presenter assumes that the logo image is stored in the "static/img/logo.png" path. Make sure to adjust the path based on your project's structure.

6. Next, they want to customize the CSS for the admin area. They create another block called "block extra_style" where they can add custom stylesheets.

   Code:
   ```html
   {% block extra_style %}
   <link rel="stylesheet" href="{% static 'css/admin.css' %}">
   {% endblock %}
   ```

   Similar to the previous step, the presenter assumes that the custom CSS file is located in the "static/css/admin.css" path. Adjust it accordingly.

7. Now, they create the "admin.css" file in the "static/css" directory of the project.

   Code:
   ```
   static/
   └── css/
       └── admin.css
   ```

8. Inside the "admin.css" file, they start making CSS modifications. For example, changing the header height, background color, and text colors.

   Code:
   ```css
   #header {
       height: 50px;
       background: #10284e;
       color: #ffffff;
   }

   #header h1 {
       color: #ffffff;
   }

   /* Additional CSS modifications based on the presenter's requirements */
   ```

   The code above represents a snippet from the CSS file. It changes the header height to 50 pixels, sets the background color to a dark blue (#10284e), and the text color to white (#ffffff).

9. Finally, the presenter demonstrates further customization by modifying the CSS for specific elements such as breadcrumbs, links, and buttons.

   Code:
   ```css
   #header{
   height: 50px;
   background: #10284e;
   color: #fff;
   }
   
   #branding h1{
       color: #fff;
   }
    
   a:link,
   a:visited {
       color: #10284e;
   }
    
   div.breadcrumbs{
       background: #30caa0;
       color: #10284e;
   }
    
   div.breadcrumbs a{
       color: #333;
   }
    
   .module h2, .module caption, .inline-group h2 {
       background: #30caa0;
   }
   
   .button, input[type=submit], input[type=button], .submit-row input, a.button {
       background: #10284e;
       color: #fff;
   }
   ```

   The code above is just an example of modifying the breadcrumbs' background color and the color of the associated links.

Please note that the provided code snippets are based on the presenter's explanations in the video. Make sure to adapt them to fit your project's structure and specific customization needs.

## 6.8. Customize Admin Display Data

Certainly! Here's a step-by-step summary of the video, including the relevant code snippets:

1. The speaker starts by explaining that they want to customize the display data in the admin area. They mention that they have already added the company logo and adjusted the colors to match the branding in the previous video.

2. To begin the customization, they open the `admin.py` file in the listings app using Visual Studio Code (VS Code).

3. In the `admin.py` file, they create a class called `ListingAdmin` that inherits from `admin.ModelAdmin`. This class will define how the listing model is displayed in the admin area.

   ```python
   class ListingAdmin(admin.ModelAdmin):
       list_display = ('id', 'title', 'published', 'price', 'list_date', 'realtor')
   ```

4. Inside the `list_display` attribute, they specify the fields they want to display in the table for each listing. They include the ID, title, published status, price, list date, and realtor.

5. After defining the `ListingAdmin` class, they need to register it in the admin site. They do this by passing it as the second argument when registering the model.

   ```python
   admin.site.register(Listing, ListingAdmin)
   ```

6. The speaker reloads the admin area to show the changes. The table now displays the specified fields for each listing, including a checkbox for the published status.

7. Next, they want to make the title field clickable to navigate to the listing's page. To enable this, they add the `list_display_links` attribute to the `ListingAdmin` class and specify the fields they want to link.

   ```python
   list_display_links = ('id', 'title')
   ```

8. They save the changes, reload the admin area, and now both the ID and title fields are clickable, allowing easy navigation to the respective pages.

9. The speaker demonstrates how to add filtering functionality. They want to filter the listings by realtor. To do this, they add the `list_filter` attribute to the `ListingAdmin` class and specify the desired field(s).

   ```python
   list_filter = ('realtor',)
   ```

10. After saving the changes and reloading the admin area, a filter box appears that allows filtering the listings based on the selected realtor.

11. They proceed to show how to make the "published" checkbox editable directly from the list view. To achieve this, they add the `list_editable` attribute to the `ListingAdmin` class and specify the field(s) to make editable.

   ```python
   list_editable = ('published',)
   ```

12. After saving and reloading, the checkboxes for the "published" status are editable. Clicking on them will toggle the publication status of the listings.

13. The speaker then demonstrates how to enable searching by specific fields. They add the `search_fields` attribute to the `ListingAdmin` class and specify the fields to include in the search.

   ```python
   search_fields = ('title', 'description', 'address', 'city', 'state', 'zip_code', 'price')
   ```

14. After saving and reloading, a search field appears at the top of the admin area. The user can now search for listings based on the specified fields.

15. The last customization shown is setting the number of listings displayed per page using pagination. They add the `list_per_page` attribute to the `ListingAdmin` class and set it to the desired value.

   ```python
   list_per_page = 25
   ```

16. After saving and reloading, the admin area now displays 25 listings per page with pagination.

17.

For the second part of the video, the speaker moves on to customizing the admin display for the "Realtor" model. Here's a summary of the steps:

1. They open the `admin.py` file for the Realtor app in VS Code.

2. In the `admin.py` file, they create a class called `RealtorAdmin` that inherits from `admin.ModelAdmin`. This class will define how the realtor model is displayed in the admin area.

   ```python
   class RealtorAdmin(admin.ModelAdmin):
       list_display = ('id', 'name', 'email', 'hire_date')
   ```

3. Inside the `list_display` attribute, they specify the fields they want to display in the table for each realtor. They include the ID, name, email, and hire date.

4. Similar to the previous step, they need to register the `RealtorAdmin` class in the admin site by passing it as the second argument when registering the model.

   ```python
   admin.site.register(Realtor, RealtorAdmin)
   ```

5. After saving the changes and reloading the admin area, the Realtor table now displays the specified fields for each realtor.

6. The speaker adds the `list_display_links` attribute to the `RealtorAdmin` class to make the ID field clickable as a link to the realtor's page.

   ```python
   list_display_links = ('id', 'name')
   ```

7. After saving and reloading, both the ID and name fields in the Realtor table become clickable links.

8. They demonstrate how to enable searching by name for the realtors. They add the `search_fields` attribute to the `RealtorAdmin` class and specify the name field.

   ```python
   search_fields = ('name',)
   ```

9. After saving and reloading, a search field appears at the top of the Realtor table, allowing users to search for realtors by name.

10. Finally, they set the number of realtors displayed per page using pagination by adding the `list_per_page` attribute to the `RealtorAdmin` class.

    ```python
    list_per_page = 25
    ```

11. After saving and reloading, the admin area now displays 25 realtors per page with pagination.

12. The speaker concludes the video by mentioning that the admin area customization is complete, and they will move on to working on the front-end website in the next video.

Please note that the code snippets provided are excerpts from the video and may not include all the necessary import statements or the full context of the `admin.py` file.

## 7.1. Pull Data From Listings Model

Step-by-step explanation with code:

1. The speaker mentions that fetching data from the database and displaying it on the website is an exciting part of the project.
2. The listings added in the admin area are stored in the database. The speaker navigates to PG admin, accesses the database, and views the "listings" table, confirming that the data is present.
3. The speaker opens the "views.py" file in VS Code. This file is located in the "listings" app or folder.
4. The current file being viewed is "index.html" which displays the listings. This is achieved by setting the URL to "/listings" and calling the "index" method in the views file.
5. To fetch the listings from the database and display them on the website, the speaker needs to import the "listing" model. They add the following code at the beginning of the file:

```python
from .models import Listing
```

6. The speaker demonstrates passing values to a template by creating a dictionary with a value. They add the following code:

```python
context = {'name': 'Brad'}
```

7. In the "listings.html" file, the speaker demonstrates how to output the value passed from the view by using double curly braces:

```html
<h1>{{ name }}</h1>
```

8. Instead of directly passing the dictionary as the second parameter, it is common to assign it to a variable and then pass that variable. The speaker updates the code as follows:

```python
context = {'listings': listings}
```

9. Now, the speaker focuses on fetching the listings from the database. They create a variable called "listings" and set it to the model "Listing" followed by ".objects.all()" to retrieve all the listings. The code looks like this:

```python
listings = Listing.objects.all()
```

10. The speaker encounters an error regarding the "objects" member of the "Listing" model. This is due to the linter not recognizing Django's special functions. They install "pylint-django" and add the necessary configuration to the VS Code settings to resolve the error.

11. With the listings fetched from the database, the speaker proceeds to pass them into the template context. They update the code as follows:

```python
context = {'listings': listings}
```

12. In the "listings.html" file, the speaker sets up a conditional statement to check if there are any listings. If there are no listings, a message stating "No listings available" will be displayed. They add the following code:

```html
{% if listings %}
  <!-- Code for displaying listings -->
{% else %}
  <div class="col-md-12">
    <p>No listings available</p>
  </div>
{% endif %}
```

13. To iterate through the listings and output them dynamically, the speaker uses a for loop in the template. They add the following code:

```html
{% for listing in listings %}
  <!-- Code for displaying each listing -->
{% endfor %}
```

14. The speaker copies the HTML code for displaying a single listing (from "listing1" div to "listing5" div) and pastes it within the for loop. They remove the unnecessary listing divs so that only one loop with dynamic values remains.

15. After saving the changes, the speaker reloads the browser and visits the listings page. They can see that all six listings are displayed, but they have the same static markup since dynamic values haven't been added yet.

This step-by-step explanation provides a detailed overview of the transcript and includes the relevant code snippets to illustrate each point.


## 7.2. Display Listings In Template

Step 1: In the previous video, the speaker took the listings model and passed the objects from the database into a template. They looped through the listings but only outputted static HTML for each listing.

Step 2: To make the output dynamic, they accessed the template syntax by using double curly braces. Within the for loop, they accessed the title of each listing by using `listing.title`.

```html
{% for listing in listings %}
  {{ listing.title }}
{% endfor %}
```

Step 3: They proceeded to display the image for each listing using the `photo_main` field of the listing model. The image URL was obtained by using `listing.photo_main.url`.

```html
{% for listing in listings %}
  <img src="{{ listing.photo_main.url }}">
{% endfor %}
```

Step 4: The speaker then worked on displaying the price field. They used the `intcomma` function from the Django contrib humanize app to add commas to the price for a more professional appearance. First, they added `'django.contrib.humanize'` to the `INSTALLED_APPS` list in the `settings.py` file. Then, they loaded the humanize template tags by adding `{% load humanize %}` at the top of the template. Finally, they applied the `intcomma` filter to the price field by using `listing.price|intcomma`.

```html
{% load humanize %}

{% for listing in listings %}
  Price: ${{ listing.price|intcomma }}
{% endfor %}
```

Step 5: The speaker continued to display other fields such as the address, square feet, garage, bedrooms, bathrooms, realtor, and listing date. They utilized the respective fields of the listing model to access the data for each field.

```html
{% for listing in listings %}
  Address: {{ listing.city }}, {{ listing.state }}, {{ listing.zip }}
  Square Feet: {{ listing.sq_ft }}
  Garage: {{ listing.garage }}
  Bedrooms: {{ listing.bedrooms }}
  Bathrooms: {{ listing.bathrooms }}
  Realtor: {{ listing.realtor.name }}
  Listing Date: {{ listing.list_date|time_since }}
{% endfor %}
```

Step 6: The speaker realized that the current link in the template did not lead to the individual listing page. They modified the link by using the `url` template tag and passing the `listing.id` parameter to direct to the correct listing.

```html
{% for listing in listings %}
  <a href="{% url 'listing' listing.id %}">View Details</a>
{% endfor %}
```

Step 7: However, an error occurred when trying to access the individual listing page. The error message indicated that the `listing` method received an unexpected keyword argument of `listing_id`. To resolve this, they updated the method in the appropriate file (`views.py`) to accept the `listing_id` parameter.

Step 8: The speaker concluded by mentioning their plans for the next video, which involved implementing pagination to handle a large number of listings and styling it similar to Bootstrap pagination.


## 7.3. Pagination Order Filter

Step-by-step guide to adding pagination to an application for property listings using Django:

1. Addressing squiggly lines related to missing docstrings:
   - Open the settings file (e.g., settings.py) of your Django project.
   - Locate the python linting configuration (python linting dot piags).
   - Add the following line to disable warnings related to missing docstrings: `--arrows-only`.
   - Save the settings file to remove the squiggly lines.

2. Adding pagination functionality to the index method:
   - In your views.py file, locate the index method responsible for displaying property listings.
   - Import the necessary paginator-related classes by adding the following line at the top of the file:
     ```python
     from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
     ```
   - Inside the index method, create a Paginator object by passing in the listings obtained from the database and the desired number of listings per page. For example:
     ```python
     paginator = Paginator(listings, 6)  # Display 6 listings per page
     ```
   - Retrieve the page number from the request URL parameter using the `request.GET.get('page')` method and assign it to a variable called `page`.
   - Get the corresponding page of listings using the `get_page()` method of the paginator. For example:
     ```python
     paged_listings = paginator.get_page(page)
     ```
   - Update the context of your view to use the `paged_listings` instead of `listings`.

3. Displaying pagination links in the template:
   - Open the template file (e.g., listings.html) where the property listings are rendered.
   - Surround the code block responsible for displaying the listings with an if statement to check if there are other pages available. This prevents showing pagination when there's only one page. For example:
     ```django
     {% if paged_listings.has_other_pages %}
       <!-- Existing code to display listings -->
     {% endif %}
     ```
   - To add the previous page link, use an if-else statement inside the previous li element. For example:
     ```django
     {% if paged_listings.has_previous %}
       <li class="page-item">
         <a class="page-link" href="?page={{ paged_listings.previous_page_number }}">Previous</a>
       </li>
     {% else %}
       <li class="page-item disabled">
         <a class="page-link" href="#">Previous</a>
       </li>
     {% endif %}
     ```
   - To add the page links, use a for loop to iterate through the page range. For example:
     ```django
     {% for num in paged_listings.paginator.page_range %}
       {% if paged_listings.number == num %}
         <li class="page-item active">
           <a class="page-link" href="#">{{ num }}</a>
         </li>
       {% else %}
         <li class="page-item">
           <a class="page-link" href="?page={{ num }}">{{ num }}</a>
         </li>
       {% endif %}
     {% endfor %}
     ```
   - Finally, add the next page link using a similar if-else structure as the previous link.

4. Ordering listings by date:
   - In the index method of your views.py file, modify the listings query to order the results by date in descending order. For example:
     ```python
     listings = listings.objects.order_by('-list_date')
     ```

5. Filtering unpublished listings:
   - Add an additional condition to the listings query to filter out unpublished listings. For example:
     ```python
     listings = listings.objects.order_by('-list_date').filter(is_published=True)
     ```

Note: Make sure to adapt the code snippets to fit your specific project structure and naming conventions.

## 7.4. Home About Page Dynamic Content

Step 1: Pagination and Display of Published Listings
- Pagination and display of only published listings were implemented in the previous video.

Step 2: Making Home Page Listings Dynamic
- Open the `views.py` file in the `Pages` app.
- Import the `listing` model from the `listings` app.
- Create a variable called `listings` and set it to the ordered and published listings from the `listing` model.
- Limit the number of listings to three.
- Create a context variable with the `listings` and pass it into the `index.html` template for the home page.

Code:
```python
from listings.models import listing

def index(request):
    listings = listing.objects.order_by('list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)
```

Step 3: Updating Home Page Template
- Open the `index.html` template for the home page.
- Add a for loop to iterate over the `listings`.
- Check if there are any listings using an if statement.
- If there are no listings, display a message indicating that no listings are available.
- If there are listings, display the dynamic data for each listing.

Code:
```html
{% if listings %}
    {% for listing in listings %}
        <!-- Display dynamic data for each listing -->
    {% endfor %}
{% else %}
    <div class="col-md-12">
        <p>No listings available</p>
    </div>
{% endif %}
```

Step 4: Making About Page Dynamic
- Open the `views.py` file in the `Pages` app.
- Import the `realtor` model from the `realtors` app.
- Create variables for `realtors` and `mvp_realtors` to fetch all realtors and the seller of the month (MVP) from the database.
- Create a context variable with the `realtors` and `mvp_realtors` and pass it into the about template.

Code:
```python
from realtors.models import realtor

def about(request):
    realtors = realtor.objects.order_by('hire_date')
    mvp_realtors = realtors.filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
```

Step 5: Updating About Page Template
- Open the `about.html` template.
- Use a for loop to iterate over the `realtors` and display their information.
- Check if there are any realtors and display a message if there are none.
- Use a separate section to display the seller of the month (MVP) if available.

Code:
```html
<!-- Displaying Realtors -->
{% if realtors %}
    {% for realtor in realtors %}
        <!-- Display dynamic data for each realtor -->
    {% endfor %}
{% else %}
    <div class="col-md-12">
        <p>No team members available</p>
    </div>
{% endif %}

<!-- Displaying Seller of the Month -->
{% if mvp_realtors %}
    {% for realtor in mvp_realtors %}
        <!-- Display dynamic data for the MVP realtor -->
    {% endfor %}
{% endif %}
```

Note: Replace the `<!-- Display dynamic data -->` placeholders with the respective HTML and dynamic data for each listing and realtor.

## 7.5. Single Listing Page

Sure! Here's a step-by-step summary of the video along with relevant code snippets:

1. The video begins by explaining the goal of creating a single listings page. It mentions the files that need to be worked on: "listings/views.py" and "templates/listings/listing.html".

2. The static markup from "listing.html" is extracted. Only the necessary section, excluding the head tag, top bar, and nav bar, is copied.

```html
{% extends 'base.html' %}

{% block content %}
   <!-- Static markup from listing.html -->
{% endblock %}
```

3. The markup is pasted into the "listing.html" file within the `block content` section. The "humanize" module is loaded to enable its usage in the template.

```html
{% extends 'base.html' %}

{% block content %}
   {% load humanize %}

   <!-- Pasted static markup from listing.html -->
{% endblock %}
```

4. In the "views.py" file, the `get_object_or_404` function from Django shortcuts is used to handle non-existent listings and display a 404 page. The listing ID is obtained from the URL.

```python
from django.shortcuts import get_object_or_404, render

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)
```

5. The listing data is passed into the template context.

```python
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)
```

6. In the "listing.html" template, dynamic values from the listing model are displayed. The title, city, state, and zip code are accessed using the `listing` object.

```html
<h1>{{ listing.title }}</h1>
<p>Location: {{ listing.city }}, {{ listing.state }}, {{ listing.zip_code }}</p>
```

7. The breadcrumb links are updated to navigate back to the home page and the listings page.

```html
<a href="{% url 'index' %}">Home</a>
<a href="{% url 'listings' %}">Listings</a>
<a href="{% url 'listings' %}">{{ listing.title }}</a>
```

8. The main image URL is displayed using the `photo_main` field of the `listing` object.

```html
<img src="{{ listing.photo_main.url }}" alt="Main Image">
```

9. Additional images are displayed using a loop. If a photo exists, it is displayed along with a link to open it in a lightbox.

```html
{% for photo in listing.photos.all %}
   {% if photo.image %}
      <a href="{{ photo.image.url }}" data-lightbox="listing-photos">
         <img src="{{ photo.image.url }}" alt="Listing Photo">
      </a>
   {% endif %}
{% endfor %}
```

10. Other listing details such as price, bedrooms, bathrooms, garage, square footage, lot size, listing date, realtor name, and description are displayed using the respective fields of the `listing` object.

```html
<p>Price: ${{ listing.price|intcomma }}</p>
<p>Bedrooms: {{ listing.bedrooms }}</p>
<p>Bathrooms: {{ listing.bathrooms }}</p>
<p>Garage: {{ listing.garage }}</p>
<p>Square Feet: {{ listing.square_feet }}</p>
<p>Lot Size: {{ listing.lot_size }}</p>
<p>Listing Date: {{ listing.list_date }}</p>
<p>Realtor: {{ listing.realtor.name }}</p>
<p>Description: {{ listing.description }}</p>
```

11. The video concludes by mentioning the next topic to be covered, which is implementing the search functionality on the home page and creating a search template similar to the listings page.

Note: Please keep in mind that the code provided is a simplified representation of the actual implementation and may require additional adjustments and dependencies based on the specific project setup.





## 7.6. Search Form Choices

Step-by-step summary with code snippets:

1. The speaker starts by explaining the need to shorten the template for select lists in the search functionality.

2. A file named "choices.py" is created in the listings app to store the dictionaries for different choices such as states, bedrooms, and prices. The file structure is as follows:

```python
# choices.py

state_choices = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    ...
}

bedroom_choices = {
    '1': '1',
    '2': '2',
    ...
}

price_choices = {
    '100000': '$100,000',
    '200000': '$200,000',
    ...
}
```

3. The choices from the "choices.py" file are imported into the "index.html" template of the Pages app.

```python
# views.py (Pages app)

from listings.choices import state_choices, bedroom_choices, price_choices

def index(request):
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)
```

4. In the "index.html" template, the speaker demonstrates how to loop through the dictionaries and output the options in the select lists of the HTML form.

```html
<!-- index.html -->

<form>
    <!-- State Select -->
    <select name="state">
        {% for key, value in state_choices.items %}
            <option value="{{ key }}">{{ value }}</option>
        {% endfor %}
    </select>

    <!-- Bedroom Select -->
    <select name="bedrooms">
        {% for key, value in bedroom_choices.items %}
            <option value="{{ key }}">{{ value }}</option>
        {% endfor %}
    </select>

    <!-- Price Select -->
    <select name="price">
        {% for key, value in price_choices.items %}
            <option value="{{ key }}">{{ value }}</option>
        {% endfor %}
    </select>
    
    <button type="submit">Search</button>
</form>
```

5. The speaker mentions that the search functionality is not yet implemented but will be handled in the search view. The search view will process the form submission and perform queries based on the user's input.

Overall, the focus of this section is on shortening the template for select lists by using a separate file to store the choices as dictionaries. The choices are then imported and looped through in the HTML template to generate the select options. The search functionality itself is not implemented at this stage but will be addressed in subsequent videos.

## 7.7. Search Form Filtering

Sure! Here's a detailed step-by-step summary of the transcript along with the relevant code snippets:

Step 1: Setting up the Query Set
- The speaker starts by creating a query set list and setting it to the listing model. They order it by list date.
Code snippet:
```python
query_set_list = Listing.objects.order_by('list_date')
```

Step 2: Rendering the Initial Search Results
- The speaker copies the code from the listings.html template to display the initial search results on the search.html template.
Code snippet (search.html):
```html
{% for listing in listings %}
    <!-- Listing information display code here -->
{% endfor %}
```

Step 3: Filtering by Keywords
- The speaker explains how to filter the query set by keywords provided in the search form. They check if the "keywords" field exists in the request, retrieve its value, and filter the query set to search for matches in the description field.
Code snippet (views.py):
```python
if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
        query_set_list = query_set_list.filter(description__icontains=keywords)
```

Step 4: Filtering by City, State, Bedrooms, and Price
- The speaker demonstrates how to filter the query set based on other search fields like city, state, bedrooms, and price.
- They use similar logic for each field, checking if it exists in the request, retrieving its value, and filtering the query set accordingly.
- For city, they perform an exact match filter on the name field.
- For state, they also perform an exact match filter on the name field.
- For bedrooms, they use the "LTE" (less than or equal to) filter to show listings with up to the specified number of bedrooms.
- For price, they also use the "LTE" filter to display listings with prices up to the specified amount.
Code snippet (views.py):
```python
if 'city' in request.GET:
    city = request.GET['city']
    if city:
        query_set_list = query_set_list.filter(city__iexact=city)

if 'state' in request.GET:
    state = request.GET['state']
    if state:
        query_set_list = query_set_list.filter(state__iexact=state)

if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
        query_set_list = query_set_list.filter(bedrooms__lte=bedrooms)

if 'price' in request.GET:
    price = request.GET['price']
    if price:
        query_set_list = query_set_list.filter(price__lte=price)
```

Step 5: Displaying the Filtered Search Results
- After applying all the filters, the speaker explains that the search results should automatically update on the search.html template.
- They suggest implementing pagination for the search results, but later decide to exclude it for simplicity.
Code snippet (search.html):
```html
{% for listing in listings %}
    <!-- Listing information display code here -->
{% endfor %}
```

And that's the detailed breakdown of the steps and code snippets discussed in the transcript.

## 7.8. Preserving Form Input

Step-by-step details with code:

1. The goal of the video is to preserve form input when displaying search results. This involves editing the search HTML file and the listings views.py file.

2. In the listings views.py file, the values from the search form need to be passed as context. This can be done by modifying the code as follows:
```python
def search_listings(request):
    # Retrieve the search keywords and city from the request
    keywords = request.GET.get('keywords', '')
    city = request.GET.get('city', '')

    # Pass the values as context to the template
    context = {
        'keywords': keywords,
        'city': city
    }

    # Rest of the code...
```

3. In the search HTML file, the values need to be used to populate the form fields. Specifically, the `value` attribute of the keywords and city fields should be set to the corresponding values.

```html
<input type="text" name="keywords" value="{{ keywords }}">
<input type="text" name="city" value="{{ city }}">
```

4. For select fields, such as the state, bedrooms, and price, a conditional statement is required to determine the selected option. This can be achieved by adding an if statement within the option tags.

```html
<select name="state">
    <option value="California" {% if key == values.state %}selected{% endif %}>California</option>
    <option value="New York" {% if key == values.state %}selected{% endif %}>New York</option>
    <!-- Other state options -->
</select>

<select name="bedrooms">
    <option value="1" {% if key == values.bedrooms %}selected{% endif %}>1 Bedroom</option>
    <option value="2" {% if key == values.bedrooms %}selected{% endif %}>2 Bedrooms</option>
    <!-- Other bedroom options -->
</select>

<select name="price">
    <option value="500" {% if key == values.price %}selected{% endif %}>$500</option>
    <option value="1000" {% if key == values.price %}selected{% endif %}>$1000</option>
    <!-- Other price options -->
</select>
```

5. The video concludes by mentioning future topics to be covered, including authentication, registration, login, inquiries, and messaging using Django's default messaging app. These topics will be addressed in subsequent videos.

Please note that the code provided is a simplified example for demonstration purposes and may require additional modifications based on your specific application.

## 8.1. Accounts App URLs

Certainly! Here's a step-by-step breakdown along with the relevant code snippets:

1. The speaker introduces the topic of user accounts and the importance of implementing registration and login functionality.

2. They suggest creating a separate app called "accounts" to handle user-related operations.

Code:
```python
python manage.py startapp accounts
```

3. They mention that Django already provides a user system, so there's no need to create a separate account or user model. The existing "auth_user" table will be used.

4. The speaker creates three HTML templates inside the "accounts" app: "login.html," "register.html," and "dashboard.html." These templates will be used for the respective pages.

Code:
```python
templates/
  accounts/
    login.html
    register.html
    dashboard.html
```

5. Next, they set up URL routes for the login, register, logout, and dashboard functionalities in the "urls.py" file within the "accounts" app.

Code:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
```

6. To use the newly created app and its URLs, the speaker adds the "accounts" app to the project's settings.

Code:
```python
INSTALLED_APPS = [
    ...
    'accounts.apps.AccountsConfig',
]
```

7. The speaker proceeds to define the view methods corresponding to the URLs in the "views.py" file within the "accounts" app.

Code:
```python
from django.shortcuts import render, redirect

def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    # Log out functionality
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
```

8. The speaker updates the main project's "urls.py" file to include the URLs from the "accounts" app.

Code:
```python
from django.urls import include

urlpatterns = [
    ...
    path('accounts/', include('accounts.urls')),
]
```

9. The speaker demonstrates how to modify the navigation bar's HTML template to include links for the register and login pages.

Code:
```html
<a class="nav-link {% if 'register' in request.path %}active{% endif %}" href="{% url 'register' %}">Register</a>
<a class="nav-link {% if 'login' in request.path %}active{% endif %}" href="{% url 'login' %}">Login</a>
```

10. Finally, they add conditional statements to highlight the active page in the navigation bar.

Code:
```html
<a class="nav-link {% if 'register' in request.path %}active{% endif %}" href="{% url 'register' %}">Register</a>
<a class="nav-link {% if 'login' in request.path %}active{% endif %}" href="{% url 'login' %}">Login</a>
```

That covers the detailed step-by-step process along with relevant code snippets for implementing user accounts and authentication in Django.

## 8.2. Register Login Templates

Here is a detailed step-by-step summary of the provided transcript, including relevant code snippets:

1. The speaker begins by discussing the creation of an accounts app and ensuring that the correct views are loaded.
   - They navigate to the `views.py` file within the accounts app.
   - The `register.html` and `login.html` templates are loaded for the respective views.

2. The speaker opens the `login.html` and `register.html` templates and makes modifications.
   - They locate the section in the templates that contains the desired content to be displayed.
   - In the `register.html` template, they find the section with the ID "register" and extract it.
   - Similarly, in the `login.html` template, they find the section and extract it.

   Code:
   ```html
   <!-- In register.html -->
   <div id="register">
     <!-- Content of the register section -->
   </div>

   <!-- In login.html -->
   <div id="login">
     <!-- Content of the login section -->
   </div>
   ```

3. The speaker extends the base layout and adds content blocks to the templates.
   - They include the line `{% extends 'base.html' %}` in both the `register.html` and `login.html` templates.
   - A content block is defined within the templates using the syntax `{% block content %}`.
   - At the end of the content block, they add `{% endblock %}`.

   Code:
   ```html
   <!-- In register.html and login.html -->
   {% extends 'base.html' %}

   {% block content %}
   <!-- Content of the section goes here -->
   {% endblock %}
   ```

4. The speaker modifies the form actions and adds a CSRF token for security.
   - They update the `action` attribute of the form tag in both templates to point to the desired URL.
   - The `action` for the registration form is set to `accounts/register`, and for the login form, it is set to `accounts/login`.
   - To prevent cross-site forgery, a CSRF token is added within the form tag using the template tag `{% csrf_token %}`.

   Code:
   ```html
   <!-- In register.html -->
   <form action="accounts/register" method="POST">
     {% csrf_token %}
     <!-- Form fields and other content -->
   </form>

   <!-- In login.html -->
   <form action="accounts/login" method="POST">
     {% csrf_token %}
     <!-- Form fields and other content -->
   </form>
   ```

5. The speaker demonstrates handling form submissions in the `views.py` file.
   - They check if the request method is a POST request using an `if` statement.
   - If the method is POST, they print a message indicating that the form was submitted and redirect the user to the same page.
   - If the method is not POST (i.e., a GET request), they render the form to display it.

   Code:
   ```python
   # In views.py
   if request.method == 'POST':
       print('Submitted reg')  # Print statement for demonstration purposes
       return redirect('register')  # Redirect to the same page
   else:
       # Render the form
       # ...
   ```

Please note that the provided summary includes explanations and code snippets from the transcript, but it's essential to review the complete code and context to ensure proper implementation and understanding.


## 8.3. Message Alerts

Step 1: Apologizing for missing fields in the form template
- The speaker acknowledges that they forgot to include the first name and last name fields in the form template.
- They advise the audience to add these fields to their version of the template.

Step 2: Configuring message alerts using Django's messaging system
- The speaker mentions that Django comes with a pre-built messages app.
- They instruct the audience to add 'django.contrib.messages' to the 'INSTALLED_APPS' list in the settings file.

Step 3: Adding message tags to the settings file
- The speaker explains that message tags need to be added to the settings file for configuring message alerts.
- They provide code to be added at the bottom of the settings file:
```python
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
```
- This code sets the message tag for errors to 'danger', matching the Bootstrap class.

Step 4: Creating a partial HTML file for alert messages
- The speaker instructs the audience to create a file named 'alerts.html' inside the 'templates/partials' directory (can be named 'underscore_alerts.html').
- They mention that the file will contain the Bootstrap markup for styling the alert messages.

Step 5: Adding Bootstrap markup to the alerts.html file
- The speaker guides the audience on how to structure the alerts.html file using Bootstrap classes.
- They provide code to be added in the alerts.html file:
```html
{% if messages %}
    {% for message in messages %}
        <div id="message" class="container">
            <div class="alert alert-{{ message.tags }} alert-dismissible text-center" role="alert">
                <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span></button>
                <strong>
                    {% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}
                        Error: 
                    {% else %}
                        {{ message.tags|title }}
                    {% endif %}
                </strong>
                {{ message }}
            </div>
        </div>
    {% endfor %}
{% endif %}
```
- This code checks if there are any messages to display, then loops through each message and applies the appropriate Bootstrap classes and markup.

Step 6: Integrating the alerts.html file into templates
- The speaker suggests where to include the alerts.html file in the existing templates, specifically in the register.html and login.html templates.
- They provide code to be added in the appropriate location of both templates:
```html
{% include 'partials/alerts.html' %}
```
- This code includes the alerts.html file and ensures that any alerts will be displayed in the specified location.

Step 7: Testing the message alerts
- The speaker demonstrates how to test the message alerts by redirecting to a specific page and displaying an error message.
- They provide code to be added in the relevant view function:
```python
from django.contrib import messages

def register(request):
    if not passwords_match:
        messages.error(request, 'Password and confirm password do not match.')
        return redirect('register')
```
- This code shows an example where an error message is displayed if the passwords do not match.
- The `messages.error()` function is used to set an error message, and `redirect()` is used to redirect to the register page.

Step 8: Optional JavaScript code for auto-fading messages
- The speaker introduces an optional JavaScript code snippet for automatically fading out error messages after a certain period.
- They provide code to be added in the main.js file:
```javascript
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);
```
- This code uses jQuery to select the message element by ID and fade it out after 3 seconds (3000 milliseconds).

Please note that the code provided is a summary and may require adjustments and integration into the existing project structure for it to work properly.

## 8.4. User Registration

Step 1: Form Validation and Storing Field Values
- The video begins by discussing the process of user registration and form validation.
- The speaker mentions the need to put submitted form field values into variables.
- Using the request object, the speaker demonstrates how to retrieve form values using the POST method.
- The form fields that are retrieved include first name, last name, username, email, password, and password confirmation.

```python
# Retrieving form values
first_name = request.POST['first_name']
last_name = request.POST['last_name']
username = request.POST['username']
email = request.POST['email']
password = request.POST['password']
password2 = request.POST['password2']
```

Step 2: Password Matching Validation
- The speaker proceeds to implement password matching validation.
- If the passwords entered by the user do not match, an error message is displayed using the `messages.error()` function.
- The user is then redirected back to the registration page.

```python
# Password matching validation
if password != password2:
    messages.error(request, "Passwords do not match.")
    return redirect('register')
```

Step 3: Checking Username and Email Uniqueness
- The speaker moves on to checking the uniqueness of the username and email entered by the user.
- The default Django user model is imported to work with user-related operations.
- The `filter()` function is used to check if the username already exists in the database.
- If the username is found, an error message is displayed and the user is redirected back to the registration page.
- The same process is followed for checking the uniqueness of the email.

```python
# Checking username uniqueness
if User.objects.filter(username=username).exists():
    messages.error(request, "Username is already taken.")
    return redirect('register')

# Checking email uniqueness
if User.objects.filter(email=email).exists():
    messages.error(request, "Email is already being used.")
    return redirect('register')
```

Step 4: User Registration
- After successful validation and uniqueness checks, the user is ready to be registered.
- The `create_user()` function is used to create a new user using the Django user model.
- The form field values are assigned to the corresponding attributes of the user object.
- The user is then saved to the database.

```python
# User registration
user = User.objects.create_user(
    username=username,
    password=password,
    email=email,
    first_name=first_name,
    last_name=last_name
)
user.save()
```

Step 5: Success Message and Redirect
- Upon successful user registration, a success message is displayed to the user.
- The user is redirected to the login page to manually log in after registration.

```python
messages.success(request, "You are now registered and can log in.")
return redirect('login')
```

Note: Throughout the process, the `messages.success()` and `messages.error()` functions are used to display appropriate success and error messages to the user.

## 8.5. User Login

Step-by-step breakdown of the transcript with code snippets:

1. The previous video covered user registration, including form validation.
2. The current focus is on implementing user login functionality.
3. Open the `accounts/views.py` file in Visual Studio Code (VS Code) or any preferred text editor.
4. Locate the `login` method within the file.

```python
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
```

5. Ensure that the method is a POST request to indicate that the login form has been submitted.
6. Retrieve the `username` and `password` variables from the form data.

```python
        user = None
        user = authenticate(username=username, password=password)
```

7. Create a variable named `user` and set it to `None`.
8. Use the `authenticate` method, which comes from Django's contrib module, to verify the provided `username` and `password` against the database.

```python
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
```

9. Check if the `user` variable is not `None`, indicating that the user has been found in the database with the provided credentials.
10. If the user is found, log them in using the `auth.login()` method.
11. Display a success message using Django's messaging framework.
12. Redirect the user to the dashboard page.

```python
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
```

13. If the user is not found, display an error message using Django's messaging framework.
14. Redirect the user back to the login page.

15. Save the changes and refresh the page to see the login form.
16. Test the login functionality by entering valid credentials (e.g., "Kathy") and the corresponding password.
17. Upon successful login, the user will be redirected to the dashboard.
18. Note that logging in as a regular user will automatically log the user out from the admin area, as both users share the same table in the database.

The provided code snippets demonstrate the steps involved in implementing user login functionality. However, it is essential to consider the overall structure of your project and ensure that all necessary imports, URLs, and templates are correctly configured to support the login functionality.

## 8.6. Logout Navbar Auth Links

Certainly! Here is a step-by-step breakdown with relevant code snippets:

1. The speaker starts by mentioning that in the previous video, they successfully implemented login authentication and were redirected to the dashboard. However, the dashboard page only contains an H1 element, so they need to make some changes.

2. They navigate to their Sublime Text editor where they have the bootstrap theme and open the "dashboard.html" file. They locate the section where they want to add content, right below the navbar.

Code:
```html
<!-- dashboard.html -->
{% extends 'base.html' %}

{% block content %}
    <!-- Add content here -->
{% endblock %}
```

3. Next, they switch back to VS Code and open the "accounts/dashboard.html" template. They paste the content from the Sublime Text editor into the template. However, they need to extend the base template and wrap the content in a block.

Code:
```html
<!-- dashboard.html -->
{% extends 'base.html' %}

{% block content %}
    <!-- Paste content here -->
{% endblock %}
```

4. The speaker focuses on modifying the navbar links based on user authentication. They open the "partials/_navbar.html" template and locate the `<ul>` element where the navbar links are present.

Code:
```html
<!-- _navbar.html -->
<ul class="navbar-nav ml-auto">
    {% if user.is_authenticated %}
        <!-- Links for authenticated users -->
    {% else %}
        <!-- Links for non-authenticated users -->
    {% endif %}
</ul>
```

5. Within the conditional statement, they add code for authenticated users. In this case, they simply add a "Hello" message to test if the conditional is working.

Code:
```html
<!-- _navbar.html -->
{% if user.is_authenticated %}
    <li class="nav-item">
        <a class="nav-link" href="#">
            Hello
        </a>
    </li>
{% else %}
    <!-- Non-authenticated links -->
{% endif %}
```

6. The speaker proceeds to create a logout link. However, they mention that a simple anchor tag won't suffice as the logout functionality requires a POST request. Instead, they create a form that resembles a link and triggers a POST request when clicked.

Code:
```html
<!-- _navbar.html -->
{% if user.is_authenticated %}
    <!-- Existing code -->
{% else %}
    <li class="nav-item">
        <a class="nav-link" href="#">
            Log out
        </a>
    </li>
{% endif %}
```

7. They add a JavaScript snippet within the logout link to submit the form when clicked.

Code:
```html
<!-- _navbar.html -->
{% if user.is_authenticated %}
    <!-- Existing code -->
{% else %}
    <li class="nav-item">
        <a class="nav-link" href="javascript:{}" onclick="document.getElementById('logout').submit();">
            Log out
        </a>
    </li>
{% endif %}
```

8. The speaker creates the logout form right below the logout link. The form's action attribute points to the logout URL, and the method is set to "POST". They also include the CSRF token required for security.

Code:
```html
<!-- _navbar.html -->
{% if user.is_authenticated %}
    <!-- Existing code -->
{% else %}
    <li class="nav-item">
        <a class="nav-link" href="javascript:{}" onclick="document.getElementById('logout').submit();">
            Log out
        </a>
    </li>
    <form id="logout" action="{% url 'logout' %}" method="post">
        {% csrf_token %}
    </form>
{% endif %}
```

9. Finally, the speaker goes to the corresponding view function in "views.py" to handle the logout functionality. They check if the request method is POST, log the user out using the `auth.logout` function, display a success message, and redirect to the index page.

Code:
```python
# views.py
from django.contrib import messages
from django.shortcuts import redirect

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('index')
```

That's the detailed step-by-step breakdown with the corresponding code snippets for the discussed transcript section.

## 8.7. Dynamic Page Titles

Step-by-step process to implement custom titles for each page:

1. Open the base HTML file of your application.
2. Add a new block for the title by using the `{% block %}` syntax. Name this block "title".
   ```html
   {% block title %}
   {% endblock %}
   ```
3. Decide where you want to place the subtitle (e.g., "BT Real Estate") in the page title. You can choose to include a pipe character or hyphen to separate the subtitle from the rest of the title. For example, "BT Real Estate | Welcome".
4. Locate the specific HTML pages where you want to add custom titles.
   - For the home page (index.html), add the following code after loading other elements:
     ```html
     {% block title %}Welcome{% endblock %}
     ```
   - For the about page, add the following code:
     ```html
     {% block title %}About Us{% endblock %}
     ```
   - For the listings page, add the following code:
     ```html
     {% block title %}Browse Property Listings{% endblock %}
     ```
   - For the search page, add the following code:
     ```html
     {% block title %}Search Results{% endblock %}
     ```
   - For the listing page, dynamically generate the title based on the specific listing. Use the `listing.title` variable to represent the title.
     ```html
     {% block title %}{{ listing.title }}{% endblock %}
     ```
   - For the register page, add the following code:
     ```html
     {% block title %}Register Account{% endblock %}
     ```
   - For the login page, add the following code:
     ```html
     {% block title %}Account Login{% endblock %}
     ```
   - For the dashboard page, add the following code:
     ```html
     {% block title %}User Dashboard{% endblock %}
     ```
5. Save the changes to the HTML files.
6. Test the custom titles by reloading each page in the front-end of the website.

Next steps related to working with contacts and inquiries:

1. The next section will focus on handling form submissions for contacts or inquiries.
2. Set up a view method that receives the form data and stores it in the database.
3. Ensure that the form includes fields for name, email, and any additional required information.
4. If a user is logged in, automatically populate the name and email fields with their information.
5. Store the user's ID along with the form data in the database to track inquiries made by logged-in users.
6. Implement functionality to display user inquiries in their respective dashboards.

Please note that the code provided in the transcript is not complete and may require further implementation based on the specific framework or technology being used in your application.

## 9.1. Contacts App Model

Sure! Here's a detailed step-by-step summary with relevant code snippets:

1. Open the terminal and make sure you're in the virtual environment.
   ```bash
   $ source venv/bin/activate

   .\venv\Scripts\activate
   ```

2. Create a new Django app called "contacts" using the following command:
   ```bash
   $ python manage.py startapp contacts
   ```

3. Open the file `contacts/models.py` and define the Contact model with its fields:
   ```python
   # contacts/models.py

   from django.db import models
   from datetime import datetime

   class Contact(models.Model):
       listing = models.CharField(max_length=200)
       listing_id = models.IntegerField()
       name = models.CharField(max_length=200)
       email = models.CharField(max_length=100)
       phone = models.CharField(max_length=100)
       message = models.TextField(blank=True)
       contact_date = models.DateTimeField(default=datetime.now, blank=True)
       user_id = models.IntegerField(blank=True)
   
       def __str__(self):
           return self.name
   ```

4. Create a migration file for the contacts app using the following command:
   ```bash
   $ python manage.py makemigrations contacts
   ```

   Note: If you encounter an error stating that the contacts app could not be found, ensure that you have added the app to the `INSTALLED_APPS` list in the `settings.py` file.

5. Apply the migration to create the contacts table in the database:
   ```bash
   $ python manage.py migrate
   ```

6. Verify that the migration was successful by checking the database table (e.g., using pgAdmin or psql shell).

   Additionally, the code snippet for adding the `contacts` app to the `INSTALLED_APPS` list in `settings.py` should look like this:
   ```python
   # settings.py

   INSTALLED_APPS = [
       # Other installed apps...
       'contacts.apps.ContactsConfig',
   ]
   ```

That's it! You have successfully created the `Contact` model, generated the migration, and applied it to create the corresponding database table.

## 9.2. Contacts Admin Customization

Step-by-step summary of the video:

1. The video begins by mentioning that in the previous video, a contacts app was created, including the model and migration. This resulted in the creation of a contacts database table.

2. The focus then shifts to the admin.py file, where the contact model needs to be registered so that it can be accessed and managed in the admin area.

3. To register the contact model, the following code is added to the admin.py file:
   ```python
   from .models import Contact
   
   class ContactAdmin(admin.ModelAdmin):
       list_display = ('ID', 'name', 'email', 'contact_date')
       list_display_links = ('ID', 'name')
       search_fields = ('name', 'email', 'listing')
       list_per_page = 25
   
   admin.site.register(Contact, ContactAdmin)
   ```

4. The code above creates a custom admin class, `ContactAdmin`, which inherits from `admin.ModelAdmin`. This allows for customizations to be made to the way the contact model is displayed and managed in the admin area.

5. The customizations made in the `ContactAdmin` class are as follows:
   - `list_display`: Specifies the fields to be displayed in the list view of the contacts. In this case, the fields are ID, name, email, and contact_date.
   - `list_display_links`: Determines which fields in the list view should be clickable links. Here, ID and name are chosen as the clickable fields.
   - `search_fields`: Defines the fields that can be searched in the admin area. In this case, name, email, and listing are included as searchable fields.
   - `list_per_page`: Sets the number of contacts to be displayed per page in the admin area, which is set to 25.

6. After adding the code to the admin.py file and saving it, the video demonstrates how to access the admin area and navigate to the contacts section. It is mentioned that contacts can be added manually, but the primary purpose of this feature is to store information from the inquiry form on the application.

7. The video concludes by mentioning that the next step will be preparing the inquiry form, which involves making some changes to the existing form to include dynamic content such as the name and email of the logged-in user, as well as hidden fields.

## 9.3. Contact Form Prep

Step 1: Adding the form tag
- In the listing.html template, locate the inquiry modal section.
- Add a form tag with the following attributes:
  - action: "contact"
  - method: "post"
  - Add a CSRF token to secure the form.

Code:
```html
<form action="contact" method="post">
  {% csrf_token %}
  <!-- Rest of the form elements will be added in subsequent steps -->
</form>
```

Step 2: Adding user ID as a hidden input
- Check if the user is authenticated.
- If the user is authenticated, add a hidden input field for the user ID.
- Set the value of the input field as the user's ID.
- If the user is not authenticated, still include the input field with a value of zero.

Code:
```html
{% if user.is_authenticated %}
  <input type="hidden" name="user_id" value="{{ user.id }}">
{% else %}
  <input type="hidden" name="user_id" value="0">
{% endif %}
```

Step 3: Adding realtor email and listing ID as hidden inputs
- Add two more hidden input fields for the realtor email and listing ID.
- Set the value of the realtor email input field as `listing.realtor.email`.
- Set the value of the listing ID input field as `listing.id`.

Code:
```html
<input type="hidden" name="realtor_email" value="{{ listing.realtor.email }}">
<input type="hidden" name="listing_id" value="{{ listing.id }}">
```

Step 4: Displaying user name and email if authenticated
- Check if the user is authenticated.
- If the user is authenticated, display their name and email as the default values for the name and email fields.

Code:
```html
<input type="text" name="name" value="{% if user.is_authenticated %}{{ user.first_name }} {{ user.last_name }}{% endif %}" required>
<input type="email" name="email" value="{% if user.is_authenticated %}{{ user.email }}{% endif %}" required>
```

Step 5: Handling form submission and setting up URLs
- Create a URL configuration file for the contact app.
- Define a URL pattern for the contact submission.
- Include the contact URLs in the main urls.py file.
- Create a view method to handle the contact form submission.

Code (contact/urls.py):
```python
from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
]
```

Code (btre/urls.py):
```python
from django.urls import include, path

urlpatterns = [
    # Other URL patterns
    path('contacts/', include('contact.urls')),
]
```

Code (contact/views.py):
```python
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        # Handle the form submission here

    return render(request, 'contact.html')
```

Note: The actual form submission handling code is not included in the provided transcript.

## 9.4. Contact Form Submission

Step-by-step breakdown of the transcript with code snippets:

1. Preparation and initial handling of form submission:
- The speaker mentions that they have prepared a contact form and now need to handle the submission.
- They check if the request method is a POST request.
- If it is a POST request, they print a "hello" message to confirm the form submission.

```python
if request.method == 'POST':
    print("hello")
    return
```

2. Capturing form fields:
- The speaker explains that they need to capture various fields from the form.
- They start by capturing the listing ID field using `request.POST.get('listing ID')`.
- They repeat the same process for other fields like listing title, name, email, phone, message, user ID, and realtor email.

```python
listing_id = request.POST.get('listing ID')
listing_title = request.POST.get('listing title')
name = request.POST.get('name')
email = request.POST.get('email')
phone = request.POST.get('phone')
message = request.POST.get('message')
user_id = request.POST.get('user ID')
realtor_email = request.POST.get('realtor email')
```

3. Fixing import and redirect issues:
- The speaker encounters some import issues for the `messages` module and the `redirect` function.
- They resolve the issue by importing `messages` from `django.contrib` and `redirect` from `shortcuts`.

```python
from django.contrib import messages
from django.shortcuts import redirect
```

4. Implementing redirection and error handling:
- The speaker aims to redirect the user to the correct page after form submission.
- They make adjustments in the code to ensure the redirection works properly.
- They plan to implement a feature that notifies users if they have already made an inquiry for a specific property.

```python
# Redirection to the correct listing page
return redirect('listings/' + listing_id)

# Future implementation for duplicate inquiry check
# Show error message if user already made an inquiry for the property
if user_already_made_inquiry:
    messages.error(request, 'You have already made an inquiry for this property.')
```

Please note that the provided code snippets are generalized examples based on the information provided in the transcript. The actual implementation may vary depending on the specific framework or programming language being used.

## 9.5. Inquiry Check Send Email

Step-by-step breakdown with code:

1. Checking if the authenticated user has already sent an inquiry:

```python
if request.user.is_authenticated:
    user_id = request.user.id
    has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id).exists()
    if has_contacted:
        messages.error(request, "You have already made an inquiry for this listing.")
        return redirect('listing', listing_id)
```

2. Sending an email notification to the realtor:

In the `settings.py` file, configure the email settings for Gmail:

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
EMAIL_USE_TLS = True
```

In the `views.py` file, import the necessary modules:

```python
from django.core.mail import send_mail
```

Then, after saving the contact information, add the following code to send the email:

```python
subject = 'Property Listing Inquiry'
message = f'There has been an inquiry for {listing.title}. Sign into the admin panel for more information.'
from_email = 'traversee.brad@gmail.com'
to_email = ['realtor@example.com', 'your-email@gmail.com']

send_mail(subject, message, from_email, to_email, fail_silently=False)
```

Note: Replace `'your-email@gmail.com'` with your actual Gmail email address, and `'your-password'` with your Gmail password.

3. Testing the functionality:

To test the inquiry submission and email sending, you can simulate a form submission. After submitting the form, check your email inbox for the notification.

Additional notes:

- The code assumes the existence of a `Contact` model that stores the contact information and includes fields such as `listing_id` and `user_id`.
- The code provided assumes the use of Django's built-in `messages` framework for displaying error messages.
- Make sure you have the necessary permissions and access to use Gmail's SMTP server.

## 9.6. Dashboard Functionality

Certainly! Here's a step-by-step breakdown of the transcript, including the code snippets:

1. The speaker begins by stating the goal of making the dashboard dynamic instead of static HTML.
2. They open the project in VS Code and navigate to the views.py file in the accounts app.
3. The Contact model needs to be imported, so they add the import statement:

```python
from contacts_app.models import Contact
```

4. They want to retrieve the contacts/inquiries for the logged-in user. To do this, they modify the existing code in views.py. They locate the dashboard view and make the following changes:

```python
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts,
    }
    return render(request, 'dashboard.html', context)
```

In this code snippet:
- The `Contact` model is used to retrieve the contacts.
- The contacts are ordered by the `contact_date` field in descending order.
- The contacts are filtered by the `user_id`, which is obtained from `request.user.id`.
- The resulting contacts are stored in the `user_contacts` variable.
- The contacts are passed to the `dashboard.html` template via the `context` dictionary.

5. Moving to the dashboard.html template, the speaker makes several changes:
- They update the title to "User Dashboard" by modifying the appropriate HTML tag.
- They replace the static welcome message with a dynamic one using the user's first name:

```html
<h3>Welcome, {{ user.first_name }}</h3>
```

- They notice an issue with the breadcrumb navigation and correct it to make the "Dashboard" link active.
- They decide to display the user's contacts/inquiries in a table. They keep the first table row and delete the rest.

```html
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Listing Title</th>
            <th>View Listing</th>
        </tr>
    </thead>
    <tbody>
        {% for contact in contacts %}
        <tr>
            <td>{{ contact.id }}</td>
            <td>{{ contact.listing }}</td>
            <td><a href="{% url 'listing' contact.listing_id %}">View Listing</a></td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="3">You have not made any inquiries.</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

In this code snippet:
- The `{% for %}` loop iterates over each contact in the `contacts` list.
- The contact's ID, listing title, and a link to view the listing are displayed in the table row.
- If there are no contacts, an "empty" section is rendered with a message stating that no inquiries have been made.

6. The speaker mentions testing and potential revisions based on client feedback, but that is not directly relevant to the technical implementation.

Note: The code provided assumes the existence of appropriate Django models, views, templates, and URL configurations. It's important to adapt the code to fit your project's structure and naming conventions.

## 10.1. Pushing To Github

1. Django deployment can be challenging compared to PHP or other languages due to the lack of pre-made scripts. For example, PHP has many pre-built scripts available with shared hosts, making deployment easier. However, with Django, you need to set up various components manually.

2. The speaker recommends using DigitalOcean, a platform that offers virtual private servers called droplets, for deploying the Django app. These droplets are essentially instances of Linux distributions, and in this case, Ubuntu will be used. By utilizing DigitalOcean, you can recreate the necessary setup on a remote machine.

3. Pushing the project to a repository like GitHub is advised for version control and collaboration purposes. The speaker creates a new private repository named "btre_project" for a Django real estate website. This example demonstrates creating a private repository, but choosing a public repository is also an option. However, private repositories usually require a fee, while public repositories are free.

4. The project is pushed to the repository using Git commands. The speaker demonstrates the process by using the terminal. First, the files are added to the staging area using the command `git add .`. Then, a commit is made with a comment, such as "initial commit," using the command `git commit -m "initial commit"`. Finally, GitHub is added as a remote repository using the command `git remote add origin <repository URL>`, and the project is pushed to the master branch with `git push origin master`.

5. A GitHub gist is provided as a detailed deployment guide, covering various steps. This guide explains the entire deployment process, including creating a DigitalOcean droplet, setting up SSH keys, implementing security measures, using PostgreSQL as the database, configuring a virtual environment, uploading files using Git, utilizing Gunicorn as a server, setting up Nginx as a proxy, and configuring the domain. The guide may need updating, but following along with the course will help navigate through the deployment process. Additionally, a link is provided to sign up for DigitalOcean, offering a $10 credit and two months of free hosting on the $5 plan.

By following these steps, the speaker aims to assist learners in successfully deploying their Django applications using DigitalOcean and GitHub.

## 10.1. Droplet Setup SSH Keys
## 10.1.
## 10.1.
## 10.1.
## 10.1.
## 10.1.
## 10.1.
## 10.1.
## 10.1.




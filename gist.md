# Django Cheat Sheet


#### Creating app

```shell
python manage.py startapp pages
```


**Add your app to project:** in installed_apps
```python
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
]
```

**Install:** `autopep8`
```shell
pip install autopep8
```

#### Configuring Template Directories:
```python
TEMPLATES = [
         {
             # ...
             'DIRS': [os.path.join(BASE_DIR, 'templates')],
             # ...
         },
     ]
```


#### To run collectstatic change setting: For static files
```python
# if os not imported
import os

STATIC_ROOT = os.path.join(BASE_DIR, 'static)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]
```

#### command to gather all static files from your apps and place them in the 'STATIC_ROOT' directory
```shell
python manage.py collectstatic
```

#### Changing to Static Links:
```html
<!-- Declaration -->
{% load static %}

<!-- static files -->
<link rel="stylesheet" href="{% static css/style.css %}">

<!-- page links - here index is refer the name declare in views -->
<a href="{% url 'index' %}">Home</a>
```

#### Your Template structure

`base.html` part in separate folder:
```tree
base.html
partials
    | _navbar.html
    | _footer.html
    | _topbar.html
```

#### Conditionals in jinja:

```html
<li
    {% if '/' == request.path %}
        class="nav-item active mr-3"
    {% else %}
        class="nav-item mr-3"
    {% endif %}
    >
```

#### Mac Postgres Setup:

After Installation Postgres

Config postgres: Open postgres
```postgres
postgres=#  \password postgres
Enter new password: 
Enter it again:
postgres=# CREATE DATABASE btredb OWNER postgres;

<!-- list database Check -->
postgres=#  \l

<!-- Exit -->
postgres=# \q
```

#### Windows Postgres setup on Djagno Project: (Connect Django with Postgres Database) - Run Migrate

Create server from right click on `Server`:


Configure postgres with django:
```shell
pip install psycopg2

pip install psycopg2-binary
```

Change `setting.py`: 
```py
DATABASE = {
    'ENGINE': 'django.db.backends.postgres',
    'NAME': 'btredb',
    'USER': 'postgres',
    'PASSWORD': '123456',
    'HOST': 'localhost',
}
```

Run migration:  with this postgres database can access the django tables
```shell
python manage.py migrate
```

#### Make Migrations

make migration: after creating models
```shell
python manage.py makemigrations
```

##### Before make Migrations

Install Pillow: required for ImageField
```shell
pip install Pillow
```

#### To use ImageField Install

Install Pillow: required for ImageField
```shell
pip install Pillow
```

#### list out actual sql created fields after makemigrations:
```shell
python manage.py sqlmigrate listings 0001
```

- Do again migrate command
```shell
python manage.py migrate
```
It reflects the model changes into database

#### To active admin area

Creating superuser:
```shell
python manage.py createsuperuser
```

#### Upload Media

Change Setting:
```python
import os

# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

Change `project/urls.py`:
```py
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### Change view list in `listing/admin.py`
```python
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
```

#### Install Pylint for no-error shows in vs code:
```shell
pip install pylint-django
```

Humanize

set settings
```python
INSTALLED_APPS = [
    'django.contrib.humanize',
]
```

Include:
```html
{% load humanize %}
```

#### Delete Migrations

Delete migrations:
```shell
python manage.py migrate your_app zero

# This will drop all tables from your_app

# If you want, since you said you want to start over, you can delete your migrations folder, or maybe rename the folder, create a new migrations folder and run

python manage.py makemigrations your_app
python manage.py migrate your_app
```

#### How to drop all the tables in a PostgresSQL database:
```sql
-- 1. By dropping the schema
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
```

#### In this method, we get all the tables in a schema and delete the tables individually using the DROP TABLE command. This method is suitable for the production environment, as other objects in the schema are retained.

PostgresSQL stores all the tables and the table metadata on its record table called pg_table.

We select all the tables from pg_tables whose schemaName is public. Using subquery, we delete the tables from the schema.
```sql
-- 2. By dropping individual tables
SELECT
  'DROP TABLE IF EXISTS "' || tablename || '" CASCADE;' 
from
  pg_tables WHERE schemaname = 'public';
```





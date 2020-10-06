# McMaster GEEKS Website

The McMaster Geeks official website,

---
## First Stage Objectives
 - [X] A main CSS file for all pages
 - [X] Home page with basic information
   - [X] Should contain information about incoming events
 - [X] A navigation menu
 - [ ] A template for community pages

 Should host basic information about the community, will not be changing frequently.

 - [X] An events page with link to each event(?)
 - [ ] Links to our sponsors

 Maybe a brief bio for each, provided by each?

 - [X] A newsletters page with links to each newsletter/article
 - [X] Ability to use markdown when posting.
 
## Second Stage

 - [X] Member sign ups

   Member will sign up to the mailing list. More details can be added later. Can be integrated with discord bot registration.

## Required Packages

 - docker
 - docker-compose

## Install instructions

 
1. Install the required packages.
1. Change the postgres password in the `docker-compose.yml` file. This is the password for the postgres database user.
3. Start the service using `docker-compose up -d` while in the same directory as `docker-compose.yml`
4. Create the database in Postgress:
    1. Connect to the database: `docker exec -ti website_db_1 psql -U postgres`.
    2. Create the database: `CREATE DATABASE NAME;` where NAME is the name of the database.
    3. Create the user: `CREATE USER myprojectuser WITH PASSWORD 'password';`
    4. Set the default encoding to UTF-8 for django.
    5. Give permission to the user for the database: `GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;`
    6. Change the postgres credentials for django.
      * Edit `NAME`, `USUER`, and `PASSWORD` in the `DATABASES` dictionary in `django/geeks_website/settings.py`. Where
      * `NAME` is the database name,
      * `USER` is the user name,
      * `PASSWORD` is the password. All set earlier in the databse setup.
5. Change the django secret key:
  1. Start the docker-compose project immediately and use docker to generate the secret key.
      - Use 
      ```
      docker exec django_container python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
      ```
      - Copy the output and replace `SECRET_KEY` with it.
      
6. Run `docker exec -ti geeks-website_django_1 python manage.py makemigrations`
7. Run `docker exec -ti geeks-website_django_1 python manage.py migrate`
8. Run `docker-compose restart django`
9. Edit the nginx config file to suite the project.
10. Enjoy the website!

---

More to be added!

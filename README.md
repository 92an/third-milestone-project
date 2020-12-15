## Table of Content

- [Deployment:](#Deployment)
    - [Preperation:](#Preperation)
    - [Deployment with Heroku CLI:](#Deployment-with-Heroku-CLI)
    - [Deployment with Github Automatic Deployment:](#Deployment-with-Github-Automatic-Deployment)
    - [More Information:](#More-Information)
- [Technologies Used:](#technologies-used)
    - [Languages:](#languages)
    - [Libraries and Frameworks:](#libraries-and-frameworks)
    - [Tools](#tools)
- [Project Purpose:](#project-purpose)
- [User Stories:](#user-stories)
- [Admin functionality:](#Admin-functionality)
- [Bugs:](#Bugs)
    - [username responsive profile in navigation:](#username-responsive-profile-in-navigation)
    - [categories stopped functioning after first filter:](#categories-stopped-functioning-after-first-filter)
- [References:](#References)
    - [Images:](#Images)
    - [Logo:](#Logo)

# Deployment:

The deployment of this project is done on heroku and 
the code is written using gitpod.

Assuming that you have created a MongoDB account with corresponding
shema to be used in the project. 

Assuming that the critical key value pairs that are confidential 
are stored in a env.py file that is not pushed to github.

## Preperation:

1. Log in to Heroku and create a "New App" with a unique name

2. Before deployment we have to inform heroku what dependencies 
our project has in a txt file called requirements. To do this use the
line of code below. 

```
pip3 freeze --local > requirements.txt
```
3. The next step is to create a Procfile using the following command.
```
echo web: python run.py > Procfile
```
4. Push these files to github.

5. The key value pairs that are hidden in the "env.py" file 
need to be specified in the settings field. In Heroku go to
settings and reveal "config vars" then specify the keys there.

## Deployment with Heroku CLI: 

1. Install Heroku CLI.

2. log in to Heroku using the following command.

```
$ heroku login
```
3. (if working on a computer locally) clone repository. 
```
$ heroku git:clone -a econhub
$ cd econhub
```
4. To implement changes to the code and pushing them to Heroku
use the following lines of code.
```
$ git add .
$ git commit -m "Commit comments here!"
$ git push heroku master
```


## Deployment with Github Automatic Deployment:

1. Go to the GitHub tab in the deploy section on Heroku.

2. Type in you GitHub username and the corresponding repository that you want to deploy.

3. Enable automatic deployment.

4. Select the Branch you want to deploy, and click on the deploy branch button.

## More Information:

For any additional information please refer to the deployment 
documentation which can be found [here](https://devcenter.heroku.com/categories/deployment)

How to clone git reposirtories can be found [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

# Technologies Used:

## Languages:
* HTML5
* CSS3 
* Javascript
* Python
    * For dependencies I refer to the requirements.txt file
* Jinja Templating language

## Libraries and Frameworks:
* Materialize
* Jquery
* Flask
* Font Awesome

## Tools
* Gitpod
* Git
* Github
* Heroku
* Chrome Dev Tools
* Mongo DB

# Project Purpose:

To create a platform to spread, share, and discuss economic ideas. 
A place where academics and other people with interest in economics can look up terms, 
such as models and theories, using a community-built dictionary. Enable discussion in various chatrooms dedicated to specific topics.

# Target Audience:

* Academics
* Economics, Finance, and Business students
* Other people interested in economics

# User stories:

* As a user I should be able to register and account with a username, email, and password.
* As a user I should be able to log in using a registered account.
* As a user I should be able to add a term to the dictionary, with a category, name, definition, and source link.
* As a user I should be able to edit the terms I have submitted.
* As a user I should be able to delete the terms I have submitted.
* As a user I should be able to update the terms I have submitted.
* As a user I should be able to join a chatroom.
* As a user I should be able to use chat functionality to communicate in the room with other logged in users currently in the chatroom.

# Admin functionality:

* As an admin I should be able to alter the categories available in the dictionary.
* As an admin I should be able to edit and delete terms by all users.
* As an admin I should be able to enter chatrooms to moderate debates.
* As an admin I should be able to contact registered users.

# Testing

## Validation

#### HTML
Validated with https://validator.w3.org/
* [x] homepage.html
* [] terms.html
* [] chattrooms.html
* [] micro_chatt.html
* [] macro_chatt.html
* [] political_chatt.html
* [] student_chatt.html
* [] register.html
* [] login.html
* [] profile.html
* [] add_terms.html
* [] categories.html
* [] add_categories.html

#### CSS
Validated with https://jigsaw.w3.org/css-validator/
* [x] style.css
#### JS
Validated with https://jshint.com/
* [x] script.js
* [x] chatt_refresh.js

# Bugs

## username responsive profile in navigation

Bug when create username profile button in nav responsive to the user logged in. 
Complained about not having access to session cookie when logged out.
Solved using a global variable g package

[Found solution here](https://www.youtube.com/watch?v=PrsmxWdthg0)

```
@app.before_request
def before_request():
    g.user = None

    if "user" in session:
        g.user = session["user"]
```

## missing source information in adding terms

I forgott to include a key value pairs

```
        term = {
            "term_name": request.form.get("term_name"),
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
        }
```
fixed it by adding the last line:

```
        term = {
            "term_name": request.form.get("term_name"),
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
            "source_url": request.form.get("source_url"),
            "created_by": session["user"]
        }
```

## categories stopped functioning after first filter

after using the categories filter selection in the search function, the categories dissapeared.
This was solved as I forgott to add the categories section to each of the render template in the search sections
in the app.py file

# References:

## Images
Image by <a href="https://pixabay.com/users/geralt-9301/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2365538">Gerd Altmann</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2365538">Pixabay</a>

Image by <a href="https://pixabay.com/users/stevepb-282134/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1726618">Steve Buissinne</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1726618">Pixabay</a>

Image by <a href="https://pixabay.com/users/pix1861-468748/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1905225">Csaba Nagy</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1905225">Pixabay</a>

Image by <a href="https://pixabay.com/users/ahmadardity-3112014/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1730089">Ahmad Ardity</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1730089">Pixabay</a>

Image by <a href="https://pixabay.com/users/geralt-9301/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=499481">Gerd Altmann</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=499481">Pixabay</a>

Image by <a href="https://pixabay.com/users/satyaprem-6578610/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4174613">SatyaPrem</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4174613">Pixabay</a>

Image by <a href="https://pixabay.com/users/tama66-1032521/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3466906">Peter H</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3466906">Pixabay</a>

Image by <a href="https://pixabay.com/users/quincecreative-1031690/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2891828">3D Animation Production Company</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2891828">Pixabay</a>

Image by <a href="https://pixabay.com/users/startupstockphotos-690514/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=849825">StartupStockPhotos</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=849825">Pixabay</a>

Keynes image comes from Wikipedia common library [here:](https://commons.wikimedia.org/wiki/File:John_Maynard_Keynes.jpg)

Rothbard image comes from Wikipedia common library [here:](https://commons.wikimedia.org/wiki/File:Murray_Rothbard.jpg)

Adam Smith image comes from Wikipedia common library [here:](https://commons.wikimedia.org/wiki/File:Adam_Smith_D8.jpg)

Marx image comes from Wikipedia common library [here:](https://commons.wikimedia.org/wiki/File:Adam_Smith_D8.jpg)


## Logo:

Created using an online platform:
https://howtostartanllc.com/logo-maker?trugdlgg1&gclid=Cj0KCQiAwf39BRCCARIsALXWETyYp7IHpeyaZ6fTY8V6deaA-XzK0N1Dz-VB9KUrkg_MKkxOGINyFzgaAkR0EALw_wcB 


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
- [Testing:](#Testing)
    - [Validation:](#Validation)
        - [HTML:](#HTML)
        - [CSS:](#CSS)
        - [CSS:](#JS)
    - [Responsive Testing:](#Responsive-Testing)
    - [Functionality:](#Functionality)
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
However it does not like jinja templating language
* [x] homepage.html
* [x] terms.html
* [x] chattrooms.html
* [x] micro_chatt.html
* [x] macro_chatt.html
* [x] political_chatt.html
* [x] student_chatt.html
* [x] register.html
* [x] login.html
* [x] profile.html
* [x] add_terms.html
* [x] categories.html
* [x] add_categories.html

#### CSS
Validated with https://jigsaw.w3.org/css-validator/
* [x] style.css
#### JS
Validated with https://jshint.com/
* [x] script.js
* [x] chatt_refresh.js

## Responsive Testing
Done on google chrome only and is the recomended browser

* Mobile S 320px
* Mobile M 375px
* Mobile L 425px
* Tablet 768px
* Laptop 1024px
* Laptop L 1440px


|Design Test|Mobile S|Mobile M|Mobile L|
|-----------|:--------:|:--------:|:--------:|
|homepage.html|poor|ok|ok|
|terms.html|poor|ok|ok|
|chattrooms.html|poor|ok|ok|
|micro_chatt.html|poor|ok|ok|
|macro_chatt.html|poor|ok|ok|
|political_chatt.html|poor|ok|ok|
|student_chatt.html|poor|ok|ok|
|register.html|poor|ok|ok|
|login.html|poor|ok|ok|
|profile.html|poor|ok|ok|
|add_terms.html|poor|ok|ok|
|categories.html|poor|ok|ok|
|add_categories.html|poor|ok|ok|

<p>&nbsp;</p>

|Design Test|Tablet|Laptop|Laptop L|
|-----------|:------:|:------:|:--------:|
|homepage.html|ok|ok|ok|
|terms.html|ok|ok|ok|
|chattrooms.html|ok|ok|ok|
|micro_chatt.html|ok|ok|ok|
|macro_chatt.html|ok|ok|ok|
|political_chatt.html|ok|ok|ok|
|student_chatt.html|ok|ok|ok|
|register.html|ok|ok|ok|
|login.html|ok|ok|ok|
|profile.html|ok|ok|ok|
|add_terms.html|ok|ok|ok|
|categories.html|ok|ok|ok|
|add_categories.ok|ok|ok|ok|

<p>&nbsp;</p>

Tested device formats:

* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pro
* Surface Duo
* Galaxy Fold

**NOTE that is is not ideal to operate on the smalest screen.
Though functional the is some overflow issue and is rather impractical
on smaller screens. Though since it is expeted that the user is someone
working on a laptop, or studying mobile devices are not the main device
that the use might use.

## Functionality

|Function|status|
|-----------|:------:|
|Menubar is dynamically changing based on who is logged in|ok|
|Only admin can see category section|ok|
|Only admin can see all tasks in profile section to delete or edit|ok|
|Users can only see their own terms in their profile to delete or edit|ok|
|Register user function works|ok|
|Login function works|ok|
|Log out works|ok|
|Forms have a cancel button to return|ok|
|Terms can be added to the dictionary in the profile section|ok|
|Terms can be updated in the dictionary in the profile section|ok|
|Terms can be deleted from the dictionary in the profile section|ok|
|Terms can read in the dictionary|ok|
|User can enter chattrooms|ok|
|User can leave chattrooms|ok|
|User can communicate in chattrooms|ok|
|Admin can alter all terms|ok|
|Admin can add categories|ok|
|Admin can delete categories|ok|

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


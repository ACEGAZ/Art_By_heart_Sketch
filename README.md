# Art By Heart Sketch

Art By Heart Sketch is a website designed for users to view artwork made by the website owner and commisson the owner to draw custom pieces for themselves.

# Motivation

I decided to build this website for my sister who sells her artwork through Instagram, Facebook and Twitter but does not have an easy way to demonstrate her artwork and get buyers specification. The Website fulfils this need and allows her to easily upload her work and find new potential contacts and buyers.   

# Table of contents
1. [Project Description](#project-description)
    1. [Navigation](#navigation)
    2. [Landing Page](#landing-page)
    3. [Gallery](#gallery)
    4. [Commissions](#commissions)
    5. [Responsive Design](#responsive-design)
2. [Technologies Used](#technologies-used)
3. [Development](#development)
4. [Deployment](#deployment)
5. [Tests](#tests)
6. [Validators](#validators)
7. [Bugs & Solutions](#bugs-&-solutions)
8. [Updates](#updates)
9. [Credits](#credits)


## Project Description <a name="project-description"></a>
Art By Heart Sketch is desigend to give the user an example of what kinds of art they can commission from the artist and easily send the artist an email to commission the type of drawing they want. The website uses Python, Django Full Stack Framework, Bootstraps and Cloudinary for static files and image storage.  

<hr>

- Navigation <a name="navigation"></a>

    The website can be navigated via the horizontal top nav-bar which displayes the Home, Gallery, commissions, sign up and log in links. if the User is logged in then     the sign in link is removed from the nav-bar and log out is displayed. also, the Users name they used when signing up will be displayed.
    when the website is displayed on a mobile device the nav-bar will become a burger symbol which expands to reveal all links, that are now displayed vertically. 

    <img src = 'static/images/Navbar.png'>

<hr>

- Landing Page <a name="landing-page"></a>

    The landing page is a read only page that demostrates what the user will get and the prices that the artist will charge. 

    <img src = 'static/images/landing-page.png'>
    <img src = 'static/images/landing-page-2.png'>
    <img src = 'static/images/landing-page-3.png'>
    <img src = 'static/images/landing-page-4.png'>
    <img src = 'static/images/landing-page-5.png'>
    <img src = 'static/images/landing-page-6.png'>
    <img src = 'static/images/landing-page-7.png'>
    <img src = 'static/images/landing-page-8.png'>
    <img src = 'static/images/landing-page-9.png'>
    <img src = 'static/images/landing-page-10.png'>
    <img src = 'static/images/landing-page-11.png'>
    <img src = 'static/images/landing-page-12.png'>
    <img src = 'static/images/landing-page-13.png'>
    <img src = 'static/images/landing-page-14.png'>
    <img src = 'static/images/landing-page-15.png'>

<hr>

- Gallery <a name="gallery"></a>

    The gallery page displayes any art that the admin/artist uploads and allows users to comment on the indivisual pieces.
    Any artwork uploaded via the upload artwork link will appear on this page.

    <img src = 'static/images/gallery.png'>
    <img src = 'static/images/gallery-2.png'>

<hr>

- Commissions <a name="commissions"></a>

    The commissions page contains three forms (normal commissions, reference sheets and customs) that can be filled in by the user. Once a form is filled in and submited an email is sent to the artist that contains all the relevant information the artists needs to contact the user and begin drawing a commission. 

    One of the three forms can be filled in and then submitted. Once submitted an email will be sent to huemann49@gmail.com and 
    all information will be easily understandable.  

    <img src = 'static/images/commissions-page-1.png'>
    <img src = 'static/images/commissions-page-2.png'>
    <img src = 'static/images/commissions-page-3.png'>
    <img src = 'static/images/commissions-page-4.png'>
    <img src = 'static/images/commissions-page-5.png'>
    <img src = 'static/images/commissions-page-6.png'>

<hr>

- Responsive Design <a name="responsive-design"></a>

    The website responds to large, medium and small screen sizes by shrinking the navbar to a burger button and displaying the 
    comment section in a single column. All elements are sized accordingly using bootstraps containers, rows and column. 

    Below are images of the responsive design as Heroku will not allow the app to connect to a "am I responsive website."

    <p float="left">
  <img src="static/images/responsive-design-1.png" width="300" />
  <img src="static/images/responsive-design-2.png" width="300" /> 
  <img src="static/images/responsive-design-3.png" width="300" />
  <img src="static/images/responsive-design-4.png" width="300" />
  <img src="static/images/responsive-design-5.png" width="300" />
  <img src="static/images/responsive-design-6.png" width="300" />
  <img src="static/images/responsive-design-7.png" width="300" />
  <img src="static/images/responsive-design-8.png" width="300" />
  <img src="static/images/responsive-design-9.png" width="300" />
</p>

<hr>

## Technologies Used <a name="technologies-used"></a>
  For this project the main technologies used were Python, Django, Bootstraps and Cloudinary. 
  Python was used as it is required for Django and Django was used to save time when creating databases, authorization, tests, ect. 
  Cloudinary was used to store static files and images when the website is deployed on Heroku, as Heroku will delete images when the dynos are reset. 
  Bootstraps was used to enable easy editing of html and css elements so the wesite could be developed faster. 
  
  Along with the above technologies many python modules were installed, the full list can be seen below:
  - asgiref==3.5.2
  - boto3==1.24.41
  - botocore==1.27.41
  - cloudinary==1.29.0
  - dj-database-url==0.5.0
  - dj3-cloudinary-storage==0.0.6
  - Django==3.2.14
  - django-allauth==0.51.0
  - django-ses==3.1.0
  - fontawesomefree==6.1.1
  - gunicorn==20.1.0
  - jmespath==1.0.1
  - oauthlib==3.2.0
  - psycopg2==2.9.3
  - PyJWT==2.4.0
  - pylint-django==2.5.3
  - pylint-plugin-utils==0.7
  - python3-openid==3.2.0
  - pytz==2022.1
  - requests-oauthlib==1.3.1
  - s3transfer==0.6.0
  - sqlparse==0.4.2
  - whitenoise==6.2.0

<hr>

## Development <a name="development"></a>

  The Art By Heart Sketch website was developed with the agile method. A Kanban board was used with user stories added to it, each detailing a different function of the website. All User stories were completed in 1 iteration. All phases of Agile development can be seen in the images below.

  <img src = 'static/images/agile-development-1.png'>
  <img src = 'static/images/agile-development-2.png'>
  <img src = 'static/images/agile-development-3.png'>
  <img src = 'static/images/agile-development-4.png'>
  <img src = 'static/images/agile-development-5.png'>
  <img src = 'static/images/agile-development-6.png'>

<hr>

## Deployment <a name="deployment"></a>
  
  The Art By Heart Sketch website was deployed on Heroku using the following steps:
  
  1.  I prepared Procfile
  2.  I created the app art-by-heart-sketch on Heroku 
  3.  I navigated to the resources tab and added the Heroku postgres add on pack 
  4.  Then I connected the postgres data base url in my repository
  5.  On the Heroku website I then navigated to the deployment tab and connect my Github repository to Heroku 
  6.  I allowed automatic commits so that Heroku would always have the current version of my app 
  7.  I set up the config vars on the setting tab
  8.  Then I successfully deployed my app using the deploy branch button. 

<hr>

## Tests <a name="tests"></a>

- Unit Testing 

  Both automated and manual testing has been performed on this projects. 
  
  All automated tests can be found in the tests.py file.
  
  unittest tests simple things like urls being resolved.

  <hr> 

- Functional testing 

  Authentication

  Description: 

  Makes sure a user can sign up to the website

  Steps:

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the sign up link.
  2. Enter email(optional), username and password.
  3. Click Sign up.
  
  Expected:

  The users username is displayed in the navbar and they can comment on the gallery page.

  Actual: 

  The users username is displayed in the navbar.

  <hr>

  Description: 

  Makes sure a user can log in once they are signed up

  Steps:

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Enter username and password.
  3. Click log in.
  
  Expected:

  The user to be taken to the home page and their username to be displayed on the navbar.

  Actual: 

  The user to be taken to the home page and their username to be displayed on the navbar.

  <hr>

Description: 

  Makes sure a user can log out once they are logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log out link.
  2. The user is presented with a question asking if they are sure they wish to log out.
  3. Click the log out button. 

  Expected: 

  User is redirected to the home page and username no longer visible.

  Actual:

  User is redirected to the home page and username no longer visible.

  <hr>

  Description: 

  Upload Artwork link displayed when logged in as superuser.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in as a superuser.
  3. The superuser can now see the upload artwork link in the navbar.

  Expected: 

  Superuser is now able to see the upload artwork link in the navbar.

  Actual:

  Superuser is now able to see the upload artwork link in the navbar.

  <hr> 

   Description: 

   Upload Artwork link allows a superuser to upload new artwork with a title.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in as a superuser.
  3. The superuser can now see the upload artwork link in the navbar.
  4. Click the upload artwork link. 
  5. The superuser is taken to a new page with the title charfield and images selection field.
  6. The superuser types a title and selcts an image from thier files.
  7. Click the upload button.
  8. The superuser is then taken to the gallery page.

  Expected: 

  The title and image that the superuser has selected is displyed on the Gallery page.

  Actual:

  The title and image that the superuser has selected is displyed on the Gallery page.

  <hr>

  Description: 

  Able to see add comment link only when logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in.
  3. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/gallery/)
  4. The user is now able to see the add comment button on the gallery page. 

  Expected: 

  User is able to see add comment link.

  Actual:

  User is able to see add comment link.

  <hr>

  Description: 

  User is able to add a comment when logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in.
  3. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/gallery/)
  4. The user is now able to add a comment to a piece of uploaded artwork.  

  Expected: 

  User is able to add a comment.

  Actual:

  User is able to add a comment.

  <hr>

  Description: 

  User is able to update only their own comments when logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in.
  3. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/gallery/)
  4. The user can now only update comments that they have added.   

  Expected: 

  User is able to update only their own comments.

  Actual:

  User is able to update only their own comments.

  <hr>

   Description: 

  User is able to delete only their own comments when logged in.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/) and click on the log in link.
  2. Log in.
  3. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/gallery/)
  4. The user can now only delete comments that they have added.   

  Expected: 

  User is able to delete only their own comments.

  Actual:

  User is able to delete only their own comments.

  <hr>

   Description: 

  User is able to fill in normal commssion form and see success message.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/commissions/).
  2. Fill in the normal commissions form.
  3. Click submit.
  4. The user is shown a success message.

  Expected: 

  User is able to fill in normal commissions form and see success message.

  Actual:

  User is able to fill in normal commissions form and see success message.

  <hr>

  Description: 

  User is able to fill in reference sheet form and see success message.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/commissions/).
  2. Fill in the reference sheet form.
  3. Click submit.
  4. The user is shown a success message.

  Expected: 

  User is able to fill in reference sheet form and see success message.

  Actual:

  User is able to fill in reference sheet form and see success message.

  <hr>

  Description: 

  User is able to fill in the custom form and see success message.

  Steps: 

  1. Navigate to [art-by-heart-sketch](https://art-by-heart-sketch.herokuapp.com/commissions/).
  2. Fill in the custom form.
  3. Click submit.
  4. The user is shown a success message.

  Expected: 

  User is able to fill in the custom form and see success message.

  Actual:

  User is able to fill in the custom form and see success message.

  <hr>

  Description: 

  The normal commissions form information is received and read through a gmail account.

  Steps: 

  1. Go to [www.gmail.com](https://mail.google.com/mail/).
  2. Log into account 
  3. View new email to see if the information has been received.

  Expected: 

  All information filled in on normal commissions form appears in email inbox.

  Actual:

  All information filled in on normal commissions form appears in email inbox.

  <hr>

  Description: 

  The normal reference sheet form information is received and read through a gmail account.

  Steps: 

  1. Go to [www.gmail.com](https://mail.google.com/mail/).
  2. Log into account 
  3. View new email to see if the information has been received.

  Expected: 

  All information filled in on reference sheet form appears in email inbox.

  Actual:

  All information filled in on reference sheet form appears in email inbox.

  <hr>

  Description: 

  The normal custom form information is received and read through a gmail account.

  Steps: 

  1. Go to [www.gmail.com](https://mail.google.com/mail/).
  2. Log into account 
  3. View new email to see if the information has been received.

  Expected: 

  All information filled in on custom form appears in email inbox.

  Actual:

  All information filled in on custom form appears in email inbox.

<hr>

## Validators <a name="validators"></a>

Art by heart sketch has been run through Lighthouse, W3C CSS validator, W3C HTML validator and pep8 Python validator.

All results can be seen below:

<hr>

### Lighthouse

<img src = 'static/images/lighthouse-test.png'>

<hr>

### WC3 CSS

<img src = 'static/images/WC3 CSS validator.png'>

This validator throws a Java lang error but unfortunatly I could not find the cause of this error.

The White space warnings have been fixed. 

All other warnings are caused by Bootstraps and can be ignored.

<hr>

### WC3 HTML

<img src = 'static/images/WC3 HTML validator.png'>

<hr>

### PEP8

Art by heart sketch was going to be tested with pep8 compliance using pep8 online (http://pep8online.com/) but this website no longer exists. The app was instead tested using gitpods built in pep8 module. 

There are a few issues I couldn't fix but these are because of the Pylint not understanding Django. I tried to fix the issues using django-pylint but I clould not get it to work. 

I have supplied images of the remaining issues below. 

<p float="left">
  <img src="static/images/pep8-test-1.png" width="300" />
  <img src="static/images/pep8-test-2.png" width="300" /> 
  <img src="static/images/pep8-test-3.png" width="300" />
  <img src="static/images/pep8-test-4.png" width="300" />
  <img src="static/images/pep8-test-5.png" width="300" />
</p>



## Bugs & Solutions <a name="bugs-&-solutions"></a> 

During this project I only encountered one major bug. Whenever artwork is uploaded from the local environment to cloudinary
a timestamp error occurs. I believe this is due to Gitpods time being an hour behind, as when I comment in local on a piece of artwork the comment time stamp is also exactly one hour behind. 

This only happens in the local environment and all functions work completely fine when running on Heroku.  

Unfortunately, I was unable ti fix this error.

<img src = 'static/images/timestamp error.png'>

<hr>

## Updates <a name="updates"></a>

In the future I would like to include a secure payment method for art to be directly purchased from the website.

I would also like to add a system for comments to be authorised by an admin before being posted but I Unfortunately ran out of time for this project. 

<hr>

## Credits <a name="credits"></a>

Special thanks to Daisy McGirr for mentoring me throughout this project.
and Emily Melham who owns all the artwork used in this project.

Thanks to Codemy videos for a easy to follow tutorial which you can find here: https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi
# GARNISH B&B

> Garnish B&b is small lovely guesthouse,website allow guests to book the room and also contact the hotel admin, Admin can create room number and checking contact request and delete user by their requirement . Created as a final Individual Project for Code Institute.

### [Deployed Link to the live site](https://my-final-project-2e49722f6d1b.herokuapp.com/)

#### - By Tuguldur Batsaikhan

---

## Table of contents 

 1. [ User Experience ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)  
 4. [ Features Left to Implement ](#features-left-to-implement)  
 5. [ Technology used ](#technology-used) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#known-bugs)  
 8. [ Deployment](#deployment)
 9. [ Resources ](#resources)  
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)

---

# User Experience


<a name="ux"></a>

## Database Design 

#### Database Relational Table

![Db relation](docs/wireframe_images/wireframe_images_relationaldb.png)



- One day, a sophisticated woman approached me, requesting a small hotel booking website.(this product is not for commercial purpose and it is only for my experience)Despite the complexity of the task, I embraced the challenge, determined to create a minimal viable product (MVP). 
- I crafted the booking table and integrated a form model into the 'Contact Me' page, ensuring a seamless user experience."

#### Data models


![Db relation](docs/wireframe_images/relation_db.png)


---

> Models.py 

![Db relation](docs/wireframe_images/model_db.png)


---

## UX design


### Overview

#### Design

> Design Home Page


<img src="docs/readme_images/home_de.png" alt="Homepage prototype" width="520">


i wanted front page with some nice description and beautiful image of hotel, color wise i did not
want to mix too many color because it is hotel booking website, in my opinion light blue and white contrast work very well and gives user very welcoming feeling.

#### Site User

- user who logged into site can book and contact the hotel admin
- user can be localist or traveller or tourist
- site user can do crud function and easily sign in and out

#### Goals for the website

- To guest read hotel info on main page and log in and book room
- To allow guest to book room and contact
- keep all user from CSRF attacks,
- give user easy navigation link
- give user easy sign up and sign out option
- give user some pop up message informing that form is validated

### Wireframes

Ux Design and sketch used BALSAMIQ tool [Balsamiq](https://balsamiq.com/).
The original sketch and planning of my website design closely aligned with the final MVP, resulting in a seamless transition from concept to execution.
> Wireframe of Home, Booking,Contact,Sign in,Sign up

![Home page](docs/wireframe_images/wireframe_images_home.png)

![Room page](docs/wireframe_images/wireframe_images_roompage.png)

![Contact page](docs/wireframe_images/wireframe_images_contact.png)

![Sign in page](docs/wireframe_images/wireframe_images_signin.png)

![Registration page](docs/wireframe_images/wireframe_images_registration.png)



##### [ Back to Top ](#table-of-contents)

---

# Agile Development

## Github kanban board

![Sign up page](docs/readme_images/kanban_imag.png)


beginning of project i have created epics and user stories and then tried to map them but there was 
some error, and it did not allow me to do,so mostly i have created task on daily basis and working indvidually it makes very clear sense like what need to be done on that day.
 Github Kandan board [here](https://github.com/users/tugii21/projects/5/views/1)

## User Stories

Initial stage of the project included stepping into the shoes of the future User. I thought about the features and functionality I would expect from the first use of the website and based on that I created a set of 12 User Stories. I labelled 10 of them as mandatory, as they provide the core functionality and source of important informations for the User. The remaining 2 Stories are labelled as NINTH- Nice To Have, Not Important, as they provide some improvements, but are not necessary for the User to enjoy the website's base functionality. 

The User Stories include the acceptance criteria and are broken down into smaller, bite- size tasks that I would tick on completion, so I could easily track my progress. During the coding session I would record the encountered bugs, issues and solutions related to the Story in the comments below. Once all of the tasks in the Issue are completed I would move the User Story form "In progress" to "Completed" card im my project's Kanban.

> List of Mandatory User Stories

1. [USER STORY: DEPLOYMENT](https://github.com/TulaUnogi/cat-beans-cafe/issues/16)
2. [USER STORY: ADMIN PANEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/17)
3. [USER STORY: CREATE AN ACCOUNT](https://github.com/TulaUnogi/cat-beans-cafe/issues/18)
4. [USER STORY: EDITING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/22)
5. [USER STORY: DELETING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/23)
6. [USER STORY: TABLE BOOKING](https://github.com/TulaUnogi/cat-beans-cafe/issues/21)
7. [USER STORY: NAVBAR AND FOOTER](https://github.com/TulaUnogi/cat-beans-cafe/issues/20)
8. [USER STORY: ABOUT US](https://github.com/TulaUnogi/cat-beans-cafe/issues/19)
9. [USER STORY: MENU](https://github.com/TulaUnogi/cat-beans-cafe/issues/26)
10. [USER STORY: GOOGLE MAPS](https://github.com/TulaUnogi/cat-beans-cafe/issues/25)


##### [ Back to Top ](#table-of-contents)

---

# Features implemented

- [USER STORY: DEPLOYMENT](https://github.com/TulaUnogi/cat-beans-cafe/issues/16)
- [USER STORY: ADMIN PANEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/17)
- [USER STORY: NAVBAR AND FOOTER](https://github.com/TulaUnogi/cat-beans-cafe/issues/20)
- [USER STORY: ABOUT US](https://github.com/TulaUnogi/cat-beans-cafe/issues/19)
- [USER STORY: MENU](https://github.com/TulaUnogi/cat-beans-cafe/issues/26)
- [USER STORY: GOOGLE MAPS](https://github.com/TulaUnogi/cat-beans-cafe/issues/25)
- [USER STORY: CREATE AN ACCOUNT](https://github.com/TulaUnogi/cat-beans-cafe/issues/18)
- [USER STORY: EDITING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/22)
- [USER STORY: DELETING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/23)
- [USER STORY: TABLE BOOKING](https://github.com/TulaUnogi/cat-beans-cafe/issues/21)
- [USER STORY: CAT CAROUSEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/24)


### Footer&Navigation Link:

- All pages are inherittated from base.html
- Navbar's is available for all user and home page can displayed without login but other pages need login access
- Footer includes social icons and find us on message

### Index page:

- home page displays information about hotel and history and nearby sighseeing

### Book a room page:

- Book a room page includes a information about the room type and set of 3 pictures and description and booking button.
- Each room single,double, ensuite room has booking button
- book a room page offere user to book a room and read booked room list and update booking and cancel booking.

### User Authentication and authorization:

- user can sign in securily and protected from crsf attack
- user can do crud function and notified after crud or authenticated

### Contact page:

- Guest can send request on contact page using form.
- Guest can easily adjust or change previous request on contact page.

### Responsiveness:

- website responsiveness google chrome developer tool and all page responsiveness was good form
samsung galaxy fold to largest screen size.

##### [ Back to Top ](#table-of-contents)

---

# Features Left to Implement

- i would more work on design of website and improve functionality.
- also improve user booking experience on booking page when user update booking then user can see pre-populated data, at this stage user only do it manualy to update the booking
- i might also work on admin page
- slideshow image on front page

##### [ Back to Top ](#table-of-contents)

---

# Technology used 

- html, css, js, python
- deployment heroku 
- database deployed on elephantSQL
- style and responsiveness and layout bootstrap
- balsamiq for wireframe
- github kanban project board for managing work 
- AI photo generator for website images
- gitpod for workspace
- github for keeping code remote, git add .,commit, push

##### [ Back to Top ](#table-of-contents)

---

# Testing

### Responsiveness

Testing for responsiveness done on Google pixel 7, Iphone14 Pro Max, Apple IPAD AIR, Macbook pro

> Index page:

![Index page](docs/responsive_images/home_image.png)


> Room & Contact page before Sign In:

![Room&Contact page](docs/responsive_images/room_image.png)

> Room Book page After Sign In:

![Room&Contact page](docs/responsive_images/room_book_image_mobile.png)
![Room&Contact page](docs/responsive_images/room_book_image.png)
![Room&Contact page](docs/responsive_images/room_book_image_laptop.png)


> Contact page After Sign In:

![Room&Contact page](docs/responsive_images/contact_image_mobile.png)
![Room&Contact page](docs/responsive_images/contact_image_tablet.png)
![Room&Contact page](docs/responsive_images/contact_image_laptop.png)


> Sign Up page:

![Sign up page](docs/responsive_images/signup_image.png)

> Admin In page:

![Admin page](docs/responsive_images/admin_image.png)


### Validator Testing 

- HTML
  - No errors were returned when passing through the official and one trailing slash warning occurred![W3C html validator](docs/readme_images/htmltest.png)
- CSS
  - No errors were found when passing through the official 
  ![W3C css validator](docs/readme_images/csstest.png)
- JS
  - No errors were found when passing through the official and one warning of 80 more character in line
  ![W3C js validator](docs/readme_images/jstest.png)
- Python
  - No errors were found when passing through the official https://infoheap.com/python-lint-online/
  ![W3C python validator](docs/readme_images/pythontest.png)
  ![W3C python validator](docs/readme_images/python1test.png)




### Manual Testing

#### User Registration Tests
| Test |Result  |
|--|--|
| User can create account | Pass |
| User can log into account | Pass |
| User can log out from account | Pass |
| Pop up messages comes up when user signed in and out | Pass |
|user can not leave some field blank| Pass|




---

#### User Navigation from one link to other link Tests

| Test | Result  |
|--|--|
| User can easily navigate to Book room | Pass |
| User can access Home page without login| Pass|
| User access their booking details on book room page|Pass|
| User can access the sent request in contact page|Pass|
| SuperUser can access admin page going to staff link|Pass|



---

#### User Authorisation Tests

| Test | Result  |
|--|--|
| Super user can login to admin page |Pass|
| User not logged in can't go in to book room page| Pass |
| Non authorised user won't access to contact page| Pass|
|user can not leave some field blank| Pass|




---

#### Contact request Tests

| Test |Result  |
|--|--|
|User can send a request | Pass |
|User can list their previous request in contact page | Pass |
|User can delete or cancel their previous request  | Pass |
|User can update or add more request in contact page | Pass |
|User can book make another request | Pass |
|User can send request in contact page and pop up message display  | Pass |
|User can see the list of the previous request| Pass |



---

#### Booking Room Tests

| Test |Result  |
|--|--|
|User can choose room no and make a booking | Pass |
|User can list their room bookings list | Pass |
|User can delete or cancel their booked room | Pass |
|User can update room booking | Pass |
|User can book another booking if there is availibility | Pass |
|User can send request in contact page  | Pass |
|User can edit booked room | Pass |
|User can see the list of booked room information | Pass |



---

#### Admin Tests

| Test |Result  |
|--|--|
|Items display correctly on front-end when updated / added |Pass|
|Admin can view booked rooms and confirm and delete specific user and booking |Pass|
|Admin can create new rooms with number pof people and bed and capacity |Pass|



##### [ Back to Top ](#table-of-contents)

---
 
# Known bugs 

- from admin panel, my idea was give admin more priority to customise room ava option for
guest but function is not displaying what supposed to display


##### [ Back to Top ](#table-of-contents)

---

# Deployment

#### The deployment stage of the website should follow the steps below:
>Create Github account

- Visit GitHub: Go to the GitHub website by typing "github.com" 
- Sign Up: On the GitHub homepage,
- Enter Your Information:
- Complete Verification: 
- the free plan (GitHub Free) is sufficient.
- Confirm Your Email:
- Set Up Your Profile: 
- explore  repositories, [use code institue template](https://github.com/Code-Institute-Org/ci-full-template)
- use this template button and get url link from your github.

>set up gitpod
- Create a GitHub Account (if you don't have one):
- Go to the GitHub website (github.com).
- Once you have a GitHub account, go to the Gitpod website (gitpod.io).
- Click on the "Sign in with GitHub" button.
- Follow the prompts to authorize Gitpod to access your GitHub account.
- Start a New Workspace:
- After signing in to Gitpod, you can start a new workspace by clicking on the "New Workspace" button.
- You'll be prompted to provide a repository URL or select a GitHub repository from your account.(remember you have created using codeinstitute template)
- Choose the repository you want to work on and customize any additional settings.
- Accessing Gitpod from GitHub:


> Create the Heroku app

- Create a Heroku Account:
- Go to the Heroku website (heroku.com) and sign up for an account if you don't already have one.
- Add and commit your code changes to the Git repository using the commands git add . and git commit -m "Initial commit". Push Your Code to Heroku:
- Deploy your app to Heroku by pushing your code to the Heroku remote using the command git push heroku main (replace main with your branch name if different).
Open Your App:

> Set up enviroment variables

- Log in to Heroku:
- Go to the Heroku website and log in to your account.
- Select Your App:(previously created)
- From the Heroku dashboard, select the app for which you want to set up environment variables.
- Go to Settings:
- Once you've selected the app, navigate to the "Settings" tab.
- Click on "Reveal Config Vars":
- Scroll down to the "Config Vars" section and click on the "Reveal Config Vars" button.
- Add Environment Variables:
- In the "Key" field, enter the name of your environment variable.(like  SECRET_KEY,DATABASE_URL,CLOUDINARY)
- In the "Value" field, enter the value for your environment variable.(secret key IN GITPOD IN ENV.PY)
- Click on the "Add" button to add the environment variable.
- Save Changes:


#### FORK this repository follow steps

- Navigate to https://github.com/tugii21/Garnish the Repository:
- Go to the GitHub website and log in to your account.
- Locate the repository you want to fork by searching or browsing through your repositories.
- Fork the Repository:
- Once you've found the repository, click on the "Fork" button in the top-right corner of the repository page.
- This action will create a copy of the repository in your GitHub account.
- Wait for the Fork to Complete:
- GitHub will create the forked repository in your account. This process usually takes only a few seconds.
- Clone the Forked Repository:
- After the forking process is complete, navigate to the forked repository on your GitHub account.
- Click on the "Code" button and copy the HTTPS or SSH URL of the repository and paste to your worksation gitpid or codeanywhere.


##### [ Back to Top ](#table-of-contents)

---

# Resources used for these project and some of them are:


- [Django documentation material](https://learn.codeinstitute.net/)
- [Crispy forms installation from code institute](https://learn.codeinstitute.net/)
- [Stack overflow website](https://stackoverflow.com/)
- [Slack channel](https://slack.com/)

##### [ Back to Top ](#table-of-contents)

---

# Credits and acknowledgements

> Images

- [hotel booking](https://gencraft.com/generate) by <b>Gencraft</b>AI-powered art and video generation platform




> Code

- <b>[django allauth](https://learn.codeinstitute.net/)</b> Built in Django Allauth and followed on set up [Allauth templates]
- <b>[Code Insitute learning material](https://learn.codeinstitute.net/)</b> setting up django 
- <b>[Code Insitute learning material](https://learn.codeinstitute.net/)</b> setting up heroku
- <b>[Readme file template ideas from](https://github.com/TulaUnogi/cat-beans-cafe/blob/main/README.md)</b> setting up basic structure of readme
- <b>[Code Insitute learning material](https://learn.codeinstitute.net/)</b> setting up elephantSQL 
- <b>[Code Insitute learning material](https://learn.codeinstitute.net/)</b> setting up Django project and app and basic set up 
- <b>[Code Insitute CODING COACH](https://app.slack.com/client/T0L30B202/C066S26EDQX)</b> fix and debug code issue, Great help from Martin and Kevin code institute coding coach,and My menthor Gareth, facilitator David for motivation.
- <b>[Code Insitute SLACK CHANNEL](https://app.slack.com/)</b> exchange ideas with fellow students
- <b>[rich resource of internet](https://stackoverflow.com/)</b> thanks to search engine google,youtube,w3school,






##### [ Back to Top ](#table-of-contents)















# Blog-app

## Description
##This is a personal blogging website where you can create and share your opinions. For users to do anything with the app, they need to register first. 

## By [Frankline Kiplangat](https://github.com/Frankline-Kiplangat)


## User Stories
Users can do the following with the app:
* View the different blogs.
* See the blogs other people have posted.
* Comment on the different blogs and leave feedback.
* Submit a blog in any category.
* Vote on the blog they liked and give it a delete or close.

## BDD
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Various Blogs  | N/A | Various blogs  |
|Display Blogs | **Click** on a Category| A page with a list of blogs |
|Add new blog | **Click** New post | User Should register/sign in to add new blog |
|View Blogs | **Click** on a post | View a blog and comments |
|Comment on a blog | **Click** Comment | Registered User displays a form where a user can comment on a certain blog |
|Delete a blog | **Click** glyphicon upvote | Vote for a specific blog increases |
|Close a blog | **Click** glyphicon downvote | Vote for a specific blog decreases |

## Technologies used
* Python3.6
* Flask framework
* HTML & CSS
* POSTGRESS

## Setup/Installation Requirements
* internet access
* $ git clone 
* $ cd blog-app (project-name)
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt ( to install all the dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh
* The app runs and you can make changes.


# Support and Contacts

In case You have any query, kindly reach out via [kipfrankline@gmail.com]


## Known Bugs
User image avartar does not function properly.


### License


## LICENSE
* Copyright (c) || 2020 [Frankline-Kiplangat](https://github.com/Frankline-Kiplangat)
* MIT License

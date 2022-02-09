# pitch-FUN
## Author

[Linus langat](https://github.com/Lenus254)

# Description
This  is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. every section of the program require login.

## Live Link
[View Site](https://pitch-fun.herokuapp.com/)

## Screenshot


## User Story

* Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Vote on s pitch they have viwed by giving it a upvote or a downvote.
* Register to be allowed to log in to the application
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all pitches, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository:
  ```
https://github.com/Lenus254/minute_pitch 
 ```
2. Move to the folder and install requirements
  ```
  cd pitch-world
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```
  python3.9 manage.py server
  ```
5. Testing the application
  ```
  python3.9 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.9](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* No known bugs but you are allowed to improve app


## License
* *MIT License:*
* Copyright (c) 2019 **Cheruiyot Langat**
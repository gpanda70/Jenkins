# Jenkins

Jenkins is a Heroku cloud-enabled bot capable of multiple commands.

  - Type your commands on the groupme
  - Jenkins will return some POST request
  - Magic

## Commands
##### -wiki


    -wiki {arg}

-wiki uses the Wikipedia Api and returns the summary article of your arg.


#### -img

    -img {arg}

-img returns the first google image search result of your arg.

#### -gif

    -gif {arg}
    -gif -random {arg}
-gif returns a gif or a random gif from giphy

#### -help

    -help

-help sends you to this github.

## Installation
You need to install [Heroku Client](https://devcenter.heroku.com/articles/getting-started-with-python)

* Now clone this repository


        git clone <url>


* Login to heroku and create a Heroku application


        heroku login  


        heroku create {name of app}


* Now link your heroku app to your local repository


        git remote add heroku git@heroku.com:{app name}.git


* Set up Env Variables


        heroku config:set bot_id={your groupme bot id}
        heroku config:set giphy_api_key={your giphy api key}


* Now you should be able push your repo to Heroku


        git add .
        git commit -m {message}
        git push heroku master

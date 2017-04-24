# University Explorer

## Introduction
For my final project in Advanced Web Apps at the University of Florida I decided to build my own skill for the Amazon’s Alexa service. 

My skill, called University Explorer, allows users to learn more about any university in the United States by speaking to their Alexa-enabled devices. The initial set of information that users can ask University Explorer is the location, the graduation rate, the median income after graduation and the average yearly tuition to the university. 

I built the skill using John Wheeler’s Flask-ASK library, and I recommend everyone to check it out. Wheeler has made it super simple to learn how to build Alexa skills. 

## The Data
All of the data for University Explorer comes from the U.S. Department of Education’s [College Scorecard Dataset](https://collegescorecard.ed.gov/data/). I came across the data while I was poking around [data.gov](https://www.data.gov), an invaluable resource for anyone learning how to build web apps who needs some data to practice with. 

After downloading a CSV file with all of the [latest data from data.gov](https://catalog.data.gov/dataset/college-scorecard), I filtered out all of the extraneous data that I didn’t need and then threw what I needed into [Mr. Data Converter](https://shancarter.github.io/mr-data-converter/) to convert it into a python dictionary.

While building the skill, I ran into a few issues that required me to clean up the data. This included “é” in Puerto Rican schools, hyphenated university names as in the University of Wisconsin-Madison as well as “&”’s like Texas A&M University. Turns out Alexa, just like humans, doesn’t completely listen for punctuation. 

## Making the Alexa Skill
The skill is almost completely powered by one for-loop that was inspired from a previous project. It loops through the over 7,000 schools in the python dictionary looking for the requested university and returns the desired information. 

I found out pretty early on that I would need to find a way around capitalized university names so that the university requested and the university in the python dictionary matched. Luckily, there’s a tool built into python called `.lower()` that forces all text to be lowercased. 

I’m not going to go through how Alexa works here, but I will say that once you stare at Alexa’s documentation and Flask-ASK tutorials long enough, you realize that Alexa does two things: it makes statements and asks questions. That’s it. And when it does speak, it does through string formatting, with little gaps for the retrieved information to be read. 

I created an intent that greets the user and asks him or her what university they want to learn about. If they don’t say anything, I have added `.reprompt` to repeat the question. I also have the skill writing cards to send back to the main Alexa app on user’s phones so that they can read what Alexa said to them. 

## Other resources. 
All of the libraries and the like that I used in my project are located in my requirements.txt file, but here are some of the resources that I used in making my very first Alexa skill. 

* [AlexaTutorial.com | Master the Alexa Skills Kit with Python](https://alexatutorial.com)
* [Intro and Skill Logic - Alexa Skills w/ Python and Flask-Ask Part 1](https://pythonprogramming.net/intro-alexa-skill-flask-ask-python-tutorial/)
* [ngrok](https://ngrok.com) (You need this if you want to test your skill with an actual Alexa-enabled device)

## Next steps. 
The next step for University Explorer is obviously to have it certified by Amazon so that anyone with an Alexa-enabled device can use my skill. I’m going to be using [John Wheeler’s tutorial](https://www.youtube.com/watch?v=mjWV4R2P4ks) of deploying skills to Amazon’s Lambda service. 
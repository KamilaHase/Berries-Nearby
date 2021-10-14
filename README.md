![Mockup](wireframes-mockups/main_mockup.png)

# Berries Nearby

A website dedicated to a community of people who want to help each other out with consumation of fruits and vegetables. There are two main groups of users of this page: people - "farmers" - who own gardens where there has grown too many fruits and vegetables (for short I will be using "fruits" only but it is meant both) and the farmers want to offer these fruits to anyone who is interested. The fruits would otherwise just stay on trees left for birds or just to rott. Second group of website users are people who are interested in self picking these fruits. Together they create a community of people who help each other out - one with offers, other with taking care of the offer. 
The website is closed for public, everybody who wants to join in has to provide basic data and log into the page. The area of gardens and self picking is limited to a specific location, in our case it is the town of Gothenburg in Sweden and its surrounding areas. 
When logged in, every user has the chance to see other people offers and at the same time post an advertisement - offer himself. There is no need to post an advertisement to see the offers.
The website community owners take no responsibility for the physical interaction between the people, although bad behaviour may be reported and some users can be kicked out by the web admin.

This project is fictional only. The idea came from seeing actual people putting small papers of invitation for picking berries and fruits, or simply leaving baskets full of fruits in front of their gardens.

## UX

### User stories:

### Design of the website:
#### Typography
#### Colors
#### Imagery
#### Wireframes
#### Mockups

## Features

### Existing Features

- **Main page - Index.html** 
- **Get ready** 
- **Game** 
 - **Computer version**
   1. **Check answers**

- **Touch screens version**

### Features Left to Implement
There is a very large number of features that are left to be implemented. The whole app can be much more interactive for all participants.

 - uploading own images of offers - would serve to other users as marketing and real presentation what the actual offer is 
 - expiration date of offers - currently the offers stay there until the user or admin deletes them. There would be a nice option to expire offers if the date has already passed. 
 - time picker - currently the user can pick any time he/she wants no matter what the start and end times are. It would be more user friendly if there is a control function correcting if the time for end is not earlier than time of start of the pick up. 
 - it would be very nice to have a list of already presented offers that has expired or has been "muted" instead of deleted. That way the user can "reactivate" old offers and he/she would´t need to add all offer information again. 
- option to be added as "interested" in this offer, therefore added into a group of interested users and be informed on time and clearly about any additional changes of this specific offer 
 
 - chat functions: 
    - chat functions directly among the users could help immensely the entire interaction among them. The input of adding contact and letting people contact themselves is not a perfect solution but serves the current purposes. Good option would be if each farmer who is posting and offer could create a group of people "interested" in his offer and moderate this group such providing information about the amount of fruits left, or adjusting time of pick up. 
    - chat functions among admin and farmer - can moderate if a report has been reported, admin can directly inform farmer what has happened

- notifications: 
    - when a new offer is published
    - when my offer has been reported
    - when I received a new message (after chat functions has been implemented)

- rating of offers
- save (for myself) as favourite offer

## Technologies Used
(adapted accordingly by: https://github.com/Code-Institute-Solutions/SampleREADME)
- **Bootstrap v5.0** - Bootstrap was used to assist with the responsiveness and styling of the website.
- **Google Fonts** - Google fonts were used to import all fonts into the style.css file which is used on all pages throughout the project.
- **jQuery** - to provide support with javascript codes
- **Git** - used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- **GitHub** - used to store the projects code after being pushed from Git.

- technologies to adapt the images (crop, adding the number circles for touch screen version, removing background etc.): 
  - **Media Bang Paint Pro**
  - **Photoshop Editor**
  - **Painting**
- **Animate.css** - for animation of lamp on index.html
- **MS Office Power Point** - used for creating wireframes
- **techsini.com** and **ami.responsivedesign.is** for mockups


## Testing

#### Website has been tested and corrected by: 
- https://www.freeformatter.com/html-formatter.html 
- https://validator.w3.org/ 

#### Testing of features:
**Index.html**
 - **Get-ready.html**

#### Bugs and problems in development:
- **Sign for "Free price" at offers.html**
    - The button that is attached to card with offers partly disappears when the card is open. It is not too good user experience but unfortunately that is seen as one of downsides of using a css library such Materialize. It would be a suggestion for further development to correct.

- **Teal default color**
    - Materialize provides teal color as default for many of their features. They also provide a guide how to change the defualt colors but unfortunately it doesn't apply to all of their features such date and time picker, switch button, label for at price/number input field. I changed the colors according to Materialize instructions, some of the features unfortunately still appear in teal (those mentioned above) and it would be good to change them to fit the overall colors of the page. 

- **Footer**
    - It was difficult for me to provide a footer that would always stick to the bottom while not covering some of the content. If there is not enough content on page that would push footer down, on some devices the footer may be floating on the page. To correct that I was adding a css class "push-down-footer" (height: 42vh) and  "push-down-footer-sm" (height: 15vh) although it is still seen as a bug as it is not sufficient for all types of devices. Also a mistake can easily appear if the programmer wouldn't remember to add the css class in further development. 


#### Testing User Stories from User Experience (UX): 
## Game walkthrough

##### First Time Visitor Goals
First time visitor would most likely go through the all stages and would not skip anything forward. The goal is to learn about the game and give a try of playing it.

##### Second Time Visitor Goals
Visitors who return to page would most likely skip the index.html and its introduction (in case they understood well during the previous visit). They would either spend time on memorizing words again, or possibly just skip directly to the game.html page where they can test their progress in knowledge and memory.

## Deployment
The website was developed on hosting page GitHub with a help of GitPod. Therefore the deployed page is hosted on Github Pages.
Now the website is published on: https://kamilahase.github.io/MS2-Vocab-Memorize/

### GitHub Pages
(credit: https://github.com/Code-Institute-Solutions/SampleREADME)
The project was deployed to GitHub Pages using the following steps:
1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
4. Scroll down on the left list of options to find "Pages" section, alternatively scroll down the Settings page until you locate the "GitHub Pages" Section. 
5. Under "Source", click the dropdown called "None" and select "Master Branch".
6. The page will automatically refresh.
7. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

### Forking the GitHub Repository
1. By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:
2. Log in to GitHub and locate the GitHub Repository
3. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
4. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.
7. $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
8. Press Enter. Your local clone will be created.

## Credits


### Acknowledgements
Many thanks to mentor Marcel who provided me with inspirational feedback, valuable tips and boosted my motivation.
Many thanks to tutors of Code Institue who´s help was highly appreciated and saved my nerves.





Media
Navbar Main Image - https://www.shutterstock.com/editor/image/berries-variety-background-strawberries-currants-blueberries-514087786





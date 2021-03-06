Last updated 24/10/2017

# The Ice Hockey Site

## Overview

### What is this site for?
The aim of the site is to eventually be the first website UK ice hockey fans visit when online. The aim is to get fans
interacting with the site through the fantasy league, blog and forum. 

### What does it do?
The main point of the website is the fantasy ice hockey league, here users compete by creating their own rosters and earning 
(and losing) points through their players actions. The idea is to give users one free entry and then further entries if 
 they subscribe, with a cash prize for the league winner at the end of the season. There is a blog from the site creators
 which would update users on how the fixing of bugs, implementing of features and fantasy ice hockey is coming along. 
 There is also a forum for users to interact with each other, this is split into different subjects. Finally, there is an 
 issue tracker for users to report bugs they discover whilst using the site and to request features they would like adding.
  The idea here is to have everything free to users apart from the upvoting of features, for which they will have to 
  subscribe.


### Features
- Fantasy Ice Hockey league
- Blog
- Forum
- Issue Tracker
- Subscriptions using Stripe

### Tech Used
- **Django** - The site is a Django project and makes use of multiple reusable apps.
- **Javascript** - Used to handle Stripe payments.
- **Stripe** - For to take users subscription payment.
- **Bootstrap** - For a responsive layout.
- **Django** - Used to create the apps.
- **SQLite** - The database used to store the models and data.
- **Python** - Programming language.

### Testing
- The site has been tested using built in Django testing.
- The site has been tested using Chrome, Firefox, Opera, Safari and Edge browsers.
- The site has been tested using multiple iOS and android devices, both tablets and mobile phones. 
- The site has been tested using http://mobiletest.me/ for other devices.
- In manual tests all forms have been submitted with correct and incorrect information to ensure the site responds correctly. 
- All links have been clicked to ensure they go to where the user expects to be taken. During testing various links have been
found to be broken along with minor form issues, such as an invalid form simply reloading empty without giving the user
any information. Messages have been added to alert users to the fact incorrect data has been entered on the form.

### Future Additions
- The creation of a database to store player information for the fantasy ice hockey.
- The creation of a database to store a users roster and keep track of their points in order to update the league table.
- The creation of charts which track how many bugs and features are dealt with. 
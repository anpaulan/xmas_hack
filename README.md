# Secret Santa Randomizer with Flask and SQLAlchemy
​
## Overview
​
This project implements a Secret Santa randomizer using Flask, SQLAlchemy, and Python's object-oriented programming (OOP) principles. Participants can input their names through a web interface, and the application assigns each participant a Secret Santa recipient. The final assignments are displayed on a separate page.

## Front End:

# 1. Static Files: 
    - Wanted to create snow falling in the background of each page, so created a js folder to hold that code
    - snowflakes.css: would style the js code
    - stylesheet.css: would style the rest of the html pages
    - snowflakes.js: holds the code to display falling snowflakes on each page

# 2. layout.html
    - This would be set the base code for all of the other HTML files we would create
    - For any css, or js files we created, we would be able to load them into this file
    - This way, we would not have to manually link each html file to the css/js files
    - Also set the y-axis to be able to scroll in the event the host was really popular and had a long guest list
    - Added home button to make it easier for the user to navigate the site
    - Tried adding audio a number of ways, but could not get it to work, left the code in the layout page though
        - If we had to guess is because the site is not hosted, so there were permissions I was not able to look into
        - Added both using local files, and through soundcloud integration, neither worked haha, but looks cool

# 3. index.html: 
    - This is where we decided to put most of the content
    - Created buttons so it would be easier for the user to navigate to the different parts of the site
    - Made a list of instructions that clearly laid out how the website works
    - Added a function to display a countdown timer

# 4. reveal, reveal2, and not_yet: 
    - All straight forward html pages, did not add much to them
    - These would be the pages that would be referenced later depending on how the interactions played out
    - reveal: would be where the user would input the names, which that data was fed into the backend db
    - reveal2: laid out who was the secret santa for each participant once the current time exceeded the set time by the user
        - The set time would be when the user would hold the secret santa event, so this page would not show until that date/time was exceeded
        - Changed the text color 1. Grinch Green 2. The lighter color shows up at the top of the list,
    - not_yet: Easter egg! in case anyone uses this, and while inspecting the site, they see there is an additional page with no reference throughout the site
        - The game does some sort of data validation through a guessing game, have fun!
    - Used if statements to handle any possible senario to guide the user on how to navigate the site

# 5. timer.html:
    - Reference page for redirects when the user tried to view the secret santa list before the set date
        - Integrated an if statement to handle redirects based on user inputs (set date/time, current date/time)
    - This page will also revert to the reveal2 page once the timer triggers and allows the user to view the secret santa list

​
## Backend:

# 1.  Python Concepts and Tools Used
​
- **Object-Oriented Programming (OOP):** The project utilizes OOP principles with a `Participant` class to model participants and manage their assignments.
​
- **Flask:** Flask is used as the web framework to handle HTTP requests and responses, creating routes for different pages.
​
- **SQLAlchemy:** SQLAlchemy is employed as an Object-Relational Mapping (ORM) tool to interact with a SQLite database, storing participant information and assignments.
​
- **Sorting Algorithm:** The project uses a shuffling algorithm (Fisher-Yates shuffle) to randomize the list of participants.
​
# 1. Project Structure
​
- **app.py:** The main file containing Flask routes, participant assignment logic, and interaction with the database.
​
- **participant_class.py:** The file containing the `Participant` class with methods for assignment and display.
​
- **templates:** The folder containing HTML templates for different pages (`index.html`, `reveal.html`, `timer.html`, `reveal2.html`).
​
- **static:** The folder for static assets such as CSS files.
​
# 2. Additional Features
​
- **Preventing Self-Assignment:** The application prevents participants from being assigned as their own Secret Santa.
​
- **Handling Edge Cases:** The code handles odd numbers of participants by ensuring each participant has a recipient.
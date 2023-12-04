# xmas_hack
Front End:

1. Static Files: 
    - Wanted to create snow falling in the background of each page, so created a js folder to hold that code
    - snowflakes.css: would style the js code
    - stylesheet.css: would style the rest of the html pages
    - snowflakes.js: holds the code to display falling snowflakes on each page

2. Created a layout.html
    - This would be set the base code for all of the other HTML files we would create
    - For any css, or js files we created, we would be able to load them into this file
    - This way, we would not have to manually link each html file to the css/js files
    - Also set the y-axis to be able to scroll in the event the host was really popular and had a long guest list
    - Added home button to make it easier for the user to navigate the site
    - Tried adding audio a number of ways, but could not get it to work, left the code in the layout page though
        - If we had to guess is because the site is not hosted, so there were permissions I was not able to look into

3. index.html: 
    - This is where we decided to put most of the content
    - Created buttons so it would be easier for the user to navigate to the different parts of the site
    - Made a list of instructions that clearly laid out how the website works
    - Added a function to display a countdown timer

4. reveal, reveal2, and not_yet
    - All straight forward html pages, did not add much to them
    - These would be the pages that would be referenced later depending on how the interactions played out
    - reveal: would be where the user would input the names, which that data was fed into the backend db
    - reveal2: laid out who was the secret santa for each participant once the current time exceeded the set time by the user
        - The set time would be when the user would hold the secret santa event, so this page would not show until that date/time was exceeded
    - Used if statements to handle any possible senario to guide the user on how to navigate the site
    - not_yet:  WHY DO WE NEED THIS? 

5. timer.html:
    - Reference page for redirects when the user tried to view the secret santa list before the set date
        - Integrated an if statement to handle redirects based on user inputs (set date/time, current date/time)
    - This page will also revert to the reveal2 page once the timer triggers and allows the user to view the secret santa list


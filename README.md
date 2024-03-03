# Carbon Chronicles

## Inspiration
When we were looking at census data for carbon dioxide, we realized that we had trouble understanding exactly how much 1 ton of CO2 was.


## What it does
Home Page:
Our home page uses parallax for better UI.
Our map is interactive, and shows CO2 data for multiple countries around the globe.
If you clock on a country, it shows more detailed data.
Predicts a linear regression model for CO2 emissions based on year.

## How we built it
We used flask for the server, and used html, css, and javascript to make the websites.
We used a svg file for the map of the world.
Link for map - [link](https://commons.wikimedia.org/wiki/File:BlankMap-World.svg)

## Challenges we ran into
Working With SVG Files - Integration of javascript with a format we've never used before
Using Bootstrap - Elements were too big and were overflowing, messing up with the navbar
Working With LiveShare - When we tried using LiveShare to collaborate
CSS Hierarchy - Was lost with how elements and their children interacted with each other.

## Accomplishments that we're proud of
Interactive Map - Map that live updates with the cursor, it also contains all countries.
Parallax Scrolling - Parallax scrolling looks very aesthetically pleasing, and improves user experience.

## What we learned
Parallax Scrolling - How to make a parallax scrolling website
GitHub - How to use GitHub more effectively
Bootstrap - How to use bootstrap to help run a server

## How to run app
1. First clone the repository and install all dependencies and requirements from the requirements.txt.
2. Create a virtual environment and start it.
3. Run the server by doing "python main.py" (might be different based on installation, e.g. python3 or py)
4. Click on the link, 127.0.0.1:5000 by default.
5. Explore website.

## What's next for SmathHacks 2024 
Keep working so we can iron out all the bugs, and improve UI for all aspects of the site. Also potentially find some place to host the site.

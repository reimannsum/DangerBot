# DangerBot
these file are the start of three scripts, one bot that will crawl the game and push info to the wiki.

- First is a script that checks one type of building page each day to see which building haven't been updated in the past 6 months.

 - Second is a script that checks the Mobile Phone Masts pages to see if they need to be updates current, old, unknown.

- Third is a script that walks three accounts through the city and records what they see to push updates to the wiki.


# Requirements
These scripts require the Python packages 
- selenium
- requests
- web-driver

the Web-Driver I'm using is [GeckoDriver](https://github.com/mozilla/geckodriver/releases) as it works best as the driver for selenium on a Raspberry Pi, the Intended home of these scripts.

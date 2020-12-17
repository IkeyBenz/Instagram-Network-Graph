# Instagram Network Grapher
A python CLI that allows you to scrape your follower data from instagram.com and graph your social network

## Getting the data
Uses a Selenium chrome bot that logs into instagram, and loads your followers data.

## Graphing the data
Using the data that the web scraper pulls, the index.html has code from D3.js that will graph all your connections and their interconnections

# Usage
1. Clone this repository `git clone git@github.com:IkeyBenz/Instagram-Network-Graph.git`
2. Install the dependencies `pip install pipenv && pipenv install`
3. Activate the virtual env `pipenv shell`
4. Run the module `python3 .`
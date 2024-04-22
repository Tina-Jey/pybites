from collections import namedtuple

import feedparser

import requests
import xml.etree.ElementTree as ET



# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')

response = requests.get(FEED_URL)

root = ET.fromstring(response.content)

def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    games = []
    for item in root.findall('.//item'):
        name = item.find('title').text.strip()
        url = item.find('link').text.strip()
        games.append(Game(name, url))
    
    return games



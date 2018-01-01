import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
    url = "http://google.ca/"
    headers = {'User-Agent': 'Mozilla/5.0'}
from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost:8000')

assert 'Django' in browser.title

# 2017.7.30

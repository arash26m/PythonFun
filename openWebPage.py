'''
a python code to open edge, go to google website, search for "USA", click on the first result
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Microsoft Edge driver
driver = webdriver.Edge()

# Navigate to the Google website
driver.get("https://www.google.com")

# Find the search input box and enter the search query "USA"
search_box = driver.find_element("name", "q")
search_box.send_keys("USA")
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)

# Click on the first search result
first_result = driver.find_element("css selector", "div.g:first-child div.yuRUbf a")
first_result.click()

# Wait for a few seconds to see the result
time.sleep(15)

# Close the browser
driver.quit()

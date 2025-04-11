from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver (make sure the path is correct if chromedriver isn't in PATH)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait for page to load
time.sleep(2)

# Find the search box and type in "Selenium"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(2)

# Print the title of the page
print("Page Title:", driver.title)

# Close the browser
driver.quit()
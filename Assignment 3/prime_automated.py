# Importing required libraries

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setting up the web driver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.primevideo.com")
driver.maximize_window()
time.sleep(1)

# Finding the Categories dropdown menu which shows options when mouse is hovered.
categories_menu = driver.find_element("xpath",
                                      "/html/body/div[1]/div[1]/header/div[1]/div/div/div/div[1]/div/ol/li[4]/label/a")

# Creating an instance of the ActionChains class to use in hover effect.
actions = ActionChains(driver)

# Performing the hover action on Categories tab.
actions.move_to_element(categories_menu).perform()
time.sleep(1)

# Moving the cursor to Kids tab and clicking on it.
kids_option = driver.find_element("xpath",
                                  "/html/body/div[1]/div[1]/header/div[1]/div/div/div/div[1]/div/ol/li[4]/div/div["
                                  "1]/ul/li[9]/a")
actions.move_to_element(kids_option)
time.sleep(2)
kids_option.click()
time.sleep(1)

# Again instantiated action chains object otherwise the ActionChain uses a stale DOM.
actions = ActionChains(driver)

# On Kids section, navigate the second slider to find show.
slider_hover = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div/div[3]/div/section/div/ul")
actions.move_to_element(slider_hover).perform()
time.sleep(2)

browse_arrow = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div/div[3]/div/section/div/button[2]/div")
actions.move_to_element(browse_arrow)
browse_arrow.click()
time.sleep(2)

# Select a movie
select_movie = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div/div[3]/div/section/div/ul/li[8]/article")
actions.move_to_element(select_movie).perform()
time.sleep(1)
select_movie.click()
time.sleep(2)

# Choose to watch trailer of that movie.
watch_trailer = driver.find_element("xpath", "/html/body/div[1]/div[1]/main/div[1]/div/div/div[2]/div[3]/div/div["
                                             "2]/div[5]/div/div/div/div/div/div[2]/div/div[2]/div/label")
actions.move_to_element(watch_trailer).perform()
time.sleep(1)
watch_trailer.click()
time.sleep(4)

# Now close the movie after playing it for few seconds by hovering over close button.
close_trailer = driver.find_element("xpath", "/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div["
                                             "5]/div[1]/div[2]/div[2]/div")

# Again instantiated action chains object otherwise the ActionChain uses a stale DOM.
actions = ActionChains(driver)
actions.move_to_element(close_trailer).perform()
time.sleep(2)

# Now after hovering over the options, click on close player button.
close_button = driver.find_element("xpath", "/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/div["
                                            "5]/div[1]/div[2]/div[2]/div/div[2]/button")
actions.move_to_element(close_button).perform()
time.sleep(1)
close_button.click()

# Share the movie on social media platform.
share_movie = driver.find_element("xpath", "/html/body/div[1]/div[1]/main/div[1]/div/div/div[2]/div[3]/div/div["
                                           "2]/div[5]/div/div/div/div/div/div[2]/div/div[2]/span[2]/div/label")
actions.move_to_element(share_movie).perform()
time.sleep(3)
share_movie.click()

# Share movie on Pinterest.
time.sleep(3)
social_media_pinterest = driver.find_element("id", "share-widget-Pinterest")
social_media_pinterest.click()
time.sleep(3)

# Closing the web driver
driver.close()

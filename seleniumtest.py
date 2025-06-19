# 1) open web browser
# 2)Open URL https://oopensource-demo.orangehrmLive.com/
# 3)Enter username (Admin)
# 4)Enter Password (admin123)
# 5)Click on login
# 6)Capture title of the homepage
# 7)Verigy title of the page
# 8)Close Browser


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")
time.sleep(5)

driver.get("http://www.youtube.com")
time.sleep(5)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(10)

driver.quit()





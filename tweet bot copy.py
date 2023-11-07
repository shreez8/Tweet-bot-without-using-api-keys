from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

accounts = []
num_accounts = int(input("Enter the number of accounts: "))

for i in range(num_accounts):
    username = input(f"Enter Twitter username for account {i + 1}: ")
    password = input(f"Enter password for account {i + 1}: ")
    accounts.append((username, password))

c=int(input("Enter no.you wan tweet should be Tweeted: "))
tweet_text=[]

for i in range(c):
    tweet_text.append(input(f"Enter your {i+1} tweets: "))
    i=i+1

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

for username, password in accounts:
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(5)

# Log in
    driver.find_element(By.NAME,"text").send_keys(username)
    driver.find_element(By.XPATH,'//span[text()="Next"]').click()

    time.sleep(5)
    driver.find_element(By.NAME,"password").send_keys(password)

    time.sleep(5)
    driver.find_element(By.XPATH,'//span[text()="Log in"]').click()

# Wait for a few seconds to load the Twitter homepage
    time.sleep(5)


    for tweets in tweet_text:
        tweet_box = driver.find_element(By.CSS_SELECTOR,'div[data-testid="tweetTextarea_0"]')
        tweet_box.send_keys(tweets)
        time.sleep(5)
        tweet_box.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(5)
        i=i+1
        c=c-1

    driver.find_element(By.XPATH, '//div[@data-testid="SideNav_AccountSwitcher_Button"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//span[contains(text(), "Log out")]').click()
    time.sleep(5)
    
# Close the browser
driver.quit()

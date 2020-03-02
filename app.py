from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox(executable_path='geckodriver.exe')


#go to tracker website
driver.get('https://rocketleague.tracker.network')
sleep(2)

#get user id
print('Please enter your steam/ps4/xbox id: ')
user_id = input()

#find search bar and enter user id
driver.find_element_by_id('name').send_keys(user_id)
driver.find_element_by_id('name').send_keys(Keys.ENTER)
sleep(5)

#collect 3v3 rank
user_rank = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[1]/table[2]/tbody/tr[5]/td[2]/small').text.split("Div")
user_mmr = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[1]/table[2]/tbody/tr[5]/td[4]').text.split('(')

#print 3v3 rank
output = "In 3v3 you're {} with an MMR of {}"
print(output.format(user_rank[0].strip(), user_mmr[0].strip()))
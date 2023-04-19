from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito") #open website in incognito window
option.add_experimental_option("excludeSwitches", ['enable-automation']);

browser = webdriver.Chrome(executable_path='/Users/taylorjade/chromedriver', options=option)
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSecyGOVasPIhqMtkQf3MV2XfpLgVvbwejbwayVOsW9-FL0wkA/viewform")

#find correct checkbox, in this case it is the one labelled "Paris, Isnthappening", and click it
checkboxes = browser.find_element("id", "i30").click()

#create and click submit button
submitbutton = browser.find_element("xpath", "/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span").click()

#click button to start a new response
newresponse = browser.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()

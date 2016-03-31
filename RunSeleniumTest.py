
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint
from time import sleep

def alerting(message):    
    driver.execute_script("alert('" + message + "')")
    sleep(3)
    alert = driver.switch_to_alert()
    alert.dismiss()
 
target_miq_from_sprout = 'https://10.8.59.164/'
driver = webdriver.Firefox()
driver.get(target_miq_from_sprout)

alerting("After setting URL, starting from logging in...")

userName = driver.find_element_by_id("user_name")
userName.send_keys("admin")
userPass = driver.find_element_by_id("user_password")
userPass.send_keys("smartvm")
loginButton= driver.find_element_by_id("login")
loginButton.click()
print ("Checkpoint 1")
sleep(10)

alerting('Just logged in, start to navigate by clicking...')

#menu1 = driver.find_elements_by_xpath("//ul[@id='maintab']/li[@class='dropdown']/a[contains(@class,'visible-lg')]")
menu1 = driver.find_elements_by_xpath("//ul[@id='maintab']/li[@class='dropdown']/a[contains(@class,'visible-lg')]")
menu2 = driver.find_elements_by_xpath("//ul[@id='maintab']/li[@class='active']/a[contains(@class,'visible-lg')]")
#print("Size of found: {count}".format(count = len(menu1)+len(menu2)))
items = []
for item in menu1:     
    it = item.get_attribute("innerText")
    items.append(it)    
for item in menu2:     
    it = item.get_attribute("innerText")
    items.append(it)    

for it in items:
    elem = driver.find_element_by_partial_link_text(it)
#   print(it)
    elem.click()
    sleep(5)
    
alerting('And then by mouse hovering, vertically...')
#print("Stop clicking. Hovering...")
# hover0 = ActionChains(driver)
for it in items:    
    dropmenu = driver.find_element_by_partial_link_text(it)
    item_class = dropmenu.get_attribute("class")
#    print(it + "(" + item_class + ")")
    hover = ActionChains(driver)
    hover.move_to_element(dropmenu)
    hover.perform() 
    drops = dropmenu.find_elements_by_xpath("../ul/li/a")  
    if it=="Infrastructure":
          alerting('Mouse hovering horizontally!')
    for drop in drops:
#        print("  > " + drop.get_attribute("innerText"))
        innerHover = ActionChains(driver)
        innerHover.move_to_element(drop)
        innerHover.perform()
        sleep(1)
    sleep(1)


print ("Checkpoint 2")
alerting('That\"s all! Something like this...')
sleep(5)
driver.quit()



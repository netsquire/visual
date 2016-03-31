
from time import sleep

def alerting(driver, message):    
    driver.execute_script("alert('" + message + "')")
    sleep(3)
    alertHandle = driver.switch_to_alert()
    alertHandle.dismiss()
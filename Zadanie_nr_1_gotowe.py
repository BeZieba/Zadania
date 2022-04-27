#---------------------------------------------------------------------------#
#  Napisz program który wejdzie na stronę https://iet.agh.edu.pl/, po czym  #
#  przejdzie do zakładki "Kandydaci"  i kliknie przycisk "Rekrutacja na agh"#
#  Oczekiwaną odpowiedzią świadczącą o wykonaniu zadania jest zrzut ekranu  #
#---------------------------------------------------------------------------#

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 

if __name__ == '__main__':
    
    driver = uc.Chrome()
    driver.get("https://iet.agh.edu.pl/")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"(//a[@href='https://iet.agh.edu.pl/kandydaci/'])[3]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'REKRUTACJA NA AGH')]").click()
    
    input("Naciśnij Enter żeby zamknąć") 
   
    
    
    
    

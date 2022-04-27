#-----------------------------------------------------------------------------------------------#
# W tym ćwiczeniu należy należy napisać program który wejdzie na stronę https://www.ebay.com/,  #
# wyszuka frazę "msi geforce rtx 3090", posortuje produkty od najtańszych do najdroższych, a    #
# nastepnie zaznaczy opcje wyświetlania tylko tych kart graficznych, których stan jest oznaczony#
# jako "nowy".                                                                                  #
# Program powinien wyświetlić cenę najtańszej karty, a następnie wykonać zrzut ekranu,          # 
#                                                                                               #
# Wykorzystaj gotowe fragmenty kodu i podpowiedzi. Oczekiwaną odpowiedzią świadczącą o wykonaniu#  
# zadania jest zrzut ekranu                                                                     #
#-----------------------------------------------------------------------------------------------#

from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 

# Cena jaka zostanie odczytana przez program bedzie zawierała przecinki, kropki, znak dolara
# wszystko to trzeba usunąć. Wykorzystaj do tego tę gotową funkcję
def formatuj_cene(cena):
    dl = len(cena)
    cena = cena[1:dl-3]
    return cena.replace(",","")

# gotowa funkcja robiąca zrzut ekranu
# syntax: execute_script(script, *args)
# Args – script: The JavaScript to execute.
#        *args: Any applicable arguments for your JavaScript

def zrzut_ekranu( driver):
    driver.maximize_window()
    widok = driver.find_element(By.XPATH, "//div[@class='srp-river srp-layout-inner']")
    driver.execute_script("arguments[0].scrollIntoView();",widok)
    driver.save_screenshot("ss.png")

if __name__ == '__main__':
    
    
    driver = uc.Chrome()
    
    driver.get("https://www.ebay.com/")
    driver.implicitly_wait(5)
    
    driver.find_element(By.ID, "gh-ac").send_keys("msi geforce rtx 3090")
    WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Decline All')]")))
    temp = driver.find_element(By.XPATH,"//*[contains(text(),'Decline All')]")
    driver.execute_script("arguments[0].click();", temp)
    driver.find_element(By.ID, "gh-ac").send_keys(Keys.ENTER)
    

    driver.find_element(By.CSS_SELECTOR, 'button[class="expand-btn expand-btn--small fake-menu-button__button"]').click()
    driver.find_element(By.XPATH, '//*[@id="s0-62-10-5-3[0]-36-1-content-menu"]/li[4]/a').click()
    

    driver.find_element(By.CSS_SELECTOR, "span[class='fake-menu-button'] > button[class='expand-btn expand-btn--small fake-menu-button__button']").click()
    driver.find_element(By.XPATH, '//*[@id="s0-62-10-5-3[0]-40-2-content-menu"]/li[1]/a').click()
    

    temp = driver.find_element(By.XPATH,"//span[@class='cbx x-refine__multi-select-cbx' and contains(text(),'New')]" )
    driver.execute_script("arguments[0].click();", temp)
    
    
    cena = driver.find_element(By.XPATH, "(//span[@class='s-item__price'])[2]").text
    cena = formatuj_cene(cena)
    print(cena)
    zrzut_ekranu(driver)
    driver.close()  
        
    
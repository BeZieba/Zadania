#------------------------------------------------------------------------------------------------#
# W tym ćwiczeniu należy napisać program który wejdzie na stronę https://www.ebay.com/,          #
# wyszuka frazę "msi geforce rtx 3090", posortuje produkty od najtańszych do najdroższych, a     #
# nastepnie zaznaczy opcje wyświetlania tylko tych kart graficznych, których stan jest oznaczony #
# jako "nowy".                                                                                   #
# Program powinien wyświetlić cenę najtańszej karty, a następnie wykonać zrzut ekranu,           # 
#                                                                                                #
# Wykorzystaj gotowe fragmenty kodu i podpowiedzi. Oczekiwaną odpowiedzią świadczącą o wykonaniu #  
# zadania jest zrzut ekranu kodu                                                                 #
#------------------------------------------------------------------------------------------------#

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
def zrzut_ekranu(driver):
    driver.maximize_window()
    widok = driver.find_element(By.XPATH, "//div[@class='srp-river srp-layout-inner']")
    driver.execute_script("arguments[0].scrollIntoView();",widok)
    driver.save_screenshot("ss.png")

if __name__ == '__main__':
    
    prod = "msi geforce rtx 3090"
    
    driver = uc.Chrome()
    
    # Chwilę po wejsciu na strone pojawi sie okienko, poczekaj aż będzie się dało kliknac przycisk "Decline all" i go kliknij
    
    # Keys.ENTER jest równoważne klawiszowi enter
    
    # Metody sortowania kart na samym poczatku sa ukryte i nie da sie do nich dotrzec
    # Przed wybraniem metody należy najpierw kliknac w odpowiedni kafelek i rozwinac wszystkie opcje
    
    
    # Odczytanie ceny produkty może sprawic wiecej trudnosci niz możnaby się spodziewać
    # dlatego aby nie marnowac niepotrzebnie czasu dajemy już gotowy Xpath "(//span[@class='s-item__price'])[2]"
    
    # cena = 
    #
    # cena = formatuj_cene(cena)
    # print(cena)
    # zrzut_ekranu(driver)
    input("Naciśnij Enter żeby zamknąć")   
    
    
#---------------------------------------------------------------------------------------------------#
# W tym zadaniu należy wejść na stronę https://allegro.pl/, znaleźć  produkt                        #
# "DROŻDŻE GORZELNICZE COOBRA Mega Pack 100L TURBO", wybrać dowolny wynik jaki się wyświetli,       #                                  
# ustawić liczbe sztuk jaką chcemy kupić na 100, a następnie:                                       #
# 1) Dodać drożdże do koszyka                                                                       #
# 2) Przejść do koszyka                                                                             #
# 3) Kliknąć "Kontynuuj zakupy"                                                                     #
#                                                                                                   #
# Wykorzystaj gotowe fragmenty kodu i podpowiedzi. Oczekiwaną odpowiedzią świadczącą o wykonaniu    # 
# zadania jest srzut ekranu kodu                                                                    #
# --------------------------------------------------------------------------------------------------#



from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 


if __name__ == '__main__':
    
    prod = "DROŻDŻE GORZELNICZE COOBRA Mega Pack 100L TURBO"
    
    driver = uc.Chrome()
    
    # Chwilę po wejsciu na strone pojawi sie popup, zgódź się na wszystkie opcje
    # allegro ma bardzo dlugie nazwy klas, jeśli to możliwe staraj sie trzymac je w zmiennych
    # bardzo poprawi to czytelnosc 
    # Chcąc "wpisac" tekst użyj send_keys("jakis tekst")
    
    
    input("Naciśnij Enter żeby zamknąć")   
    
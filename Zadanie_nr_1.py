#---------------------------------------------------------------------------#
#  Napisz program który wejdzie na stronę https://iet.agh.edu.pl/, po czym  #
#  przejdzie do zakładki "Kandydaci"  i kliknie przycisk "Rekrutacja na agh"#
#  Odpowiedzią świadczącą o wykonaniu zadania jest zrzut ekranu kodu        #
#---------------------------------------------------------------------------#

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 

if __name__ == '__main__':
    

    input("Naciśnij Enter żeby zamknąć") 
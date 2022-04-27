# ---------------------------------------------------------------------------#
#  Napisz program który wyszuka ostatni mecz pomiędzy 2 zespołami, po czym   #
#  wypisze date spotkania, nazwe rozgrywek w jakich rywalizowali oraz poda   #
#  końcowy wynik spotkania. Możesz zastosować pętlę. Oczekiwaną odpowiedzią  #
#  świadczącą o wykonaniu zadania jest zrzut ekran działającego kodu.        #
#                                                                            #
#  Wykorzystaj gotowe fragmenty kodu i podpowiedzi. Oczekiwaną odpowiedzią   #
#  świadczącą o wykonaniu zadania jest zrzut ekranu                          #
# ---------------------------------------------------------------------------#
import selenium
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get("https://google.pl/")
    element = driver.find_element(By.ID, "L2AGLb")
    driver.execute_script("arguments[0].click()", element)
    klub1 = input("Podaj pierwszą drużynę: ")
    klub2 = input("Podaj drugą drużynę: ")
    wyszukiwanie = klub1 + " " + klub2 + " ostatni mecz"
#---------------------------------------------------------------------------------------------------#
# W tym zadaniu należy napisać program, który wejdzie na stronę https://allegro.pl/, znajdzie       #
# produkt "DROŻDŻE GORZELNICZE COOBRA Mega Pack 100L TURBO", wybierze dowolny wynik jaki się        #                                  
# wyświetli, ustawi liczbe sztuk jaką chcemy kupić na 100, a następnie:                             #
# 1) Doda  drożdże do koszyka                                                                       #
# 2) Przejdzie do koszyka                                                                           #
# 3) Kliknie "Kontynuuj zakupy"                                                                     #
#                                                                                                   #
# Wykorzystaj gotowe fragmenty kodu i podpowiedzi. Oczekiwaną odpowiedzią świadczącą o wykonaniu    # 
# zadania jest plik z kodem                                                                         #
# --------------------------------------------------------------------------------------------------#



from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 


if __name__ == '__main__':
    
    driver = uc.Chrome()
    driver.get('https://allegro.pl/')
    driver.implicitly_wait(10)
    

    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Ok, zgadzam się')]"))).click()
    temp = "//input[@class='mr3m_1 mli2_1 mjyo_6x mse2_40 mqu1_40 mp4t_0 m3h2_0 mryx_0 munh_0 mg9e_0 mj7a_0 mh36_0 mvrt_8 mlkp_ag mefy_5r mldj_0 mm2b_0 _14uqc mgmw_q3 mh85_0 _535b5_1gH6X']"
    prod = "DROŻDŻE GORZELNICZE COOBRA Mega Pack 100L TURBO"
    
    
    driver.find_element(By.XPATH, temp).send_keys(prod)
    driver.find_element(By.XPATH, temp).send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//div[@class='mpof_ki mqen_m6 mp7g_oh mh36_0 mvrt_0 mg9e_8 mj7a_8 m7er_k4 _1y62o _6a66d_snEkI ']").click()
    
    ilosc = driver.find_element(By.XPATH, "//input[@class='mjyo_6x mqu1_21 mli8_k4 mse2_40 mp4t_0 m3h2_0 mryx_0 munh_0 mg9e_8 mvrt_8 mj7a_8 mh36_8 m911_5r mefy_5r mnyp_5r mdwl_5r mgmw_wo msts_pt mgn2_14 mp0t_0a m9tr_5r o1w0t o16al msbw_0 mldj_0 mtag_0 mm2b_0 mzmg_6m']")
    driver.execute_script("arguments[0].setAttribute('value','100')", ilosc)
    driver.find_element(By.ID, "add-to-cart-button").click()
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,"//*[@class='mgn2_14 mp0t_0a m9qz_yp mp7g_oh mse2_40 mqu1_40 mtsp_ib mli8_k4 mp4t_0 m3h2_0 mryx_0 m911_5r mefy_5r mnyp_5r mdwl_5r msbw_2 mldj_2 mtag_2 mm2b_2 mqvr_2 msa3_z4 mqen_m6 meqh_en m0qj_5r mh36_16 mvrt_16 mg9e_0 mj7a_0 mjir_sv m2ha_2 m8qd_qh mjt1_n2 blgl9 mgmw_9u msts_enp mrmn_qo mrhf_u8 m31c_kb m0ux_fp b1jc1 munh_0 munh_56_s']"))).click()
   
    driver.find_element(By.XPATH, "//a[@data-analytics-click-label='continueShopping']").click()
    input("Nacisnij enter")

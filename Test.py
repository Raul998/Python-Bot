from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/local/share/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.converse.com/shop/p/chuck-taylor-all-star-unisex-low-top-shoe/M9696MP.html?dwvar_M9696MP_color=optical%20white&styleNo=M7652&cgid=chuck-taylor-all-star-shoes")
buy = driver.find_element_by_xpath('//*[@id="variationDropdown-size"]')
buy.click()
buy = driver.find_element_by_xpath('//*[@id="variationDropdown-size"]/option[16]')
buy.click()
driver.implicitly_wait(5)
add_cart = driver.find_element_by_xpath('//*[@id="add-to-cart-M7652_100"]')
add_cart.click()
driver.implicitly_wait(5)
# checkout = driver.find_element_by_xpath('//*[@id="toggleID-2949--target"]/div[4]/div[4]/a')
# checkout.click()
driver.get("https://www.converse.com/shipping")
driver.implicitly_wait(5)
input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_firstName"]')
input.send_keys("Raul")
input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_lastName"]')
input.send_keys("Parra")
input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_address1"]')
input.send_keys("Dolan")
input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_address2"]')
input.send_keys("Street")
input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_city"]')
input.send_keys("El Paso")
input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_postal"]')
input.send_keys("72400")
input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_states_state"]')
input.send_keys("Texas")


driver.quit()

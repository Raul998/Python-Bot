from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import ReadOrWriteCredentials



def connecting_to_site():
    return driver.get("https://www.converse.com/shop/p/chuck-taylor-all-star-unisex-low-top-shoe/M9696MP.html?dwvar_M9696MP_color=optical%20white&styleNo=M7652&cgid=chuck-taylor-all-star-shoes")

def clicking_to_buy():
    buy = driver.find_element_by_xpath('//*[@id="variationDropdown-size"]')
    buy.click()
    buy = driver.find_element_by_xpath('//*[@id="variationDropdown-size"]/option[16]')
    buy.click()
    driver.implicitly_wait(5)
    add_cart = driver.find_element_by_xpath('//*[@id="add-to-cart-M7652_100"]')
    add_cart.click()
# checkout = driver.find_element_by_xpath('//*[@id="toggleID-2949--target"]/div[4]/div[4]/a')
# checkout.click()
def inserting_shipping():
    driver.get("https://www.converse.com/shipping")
    input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_firstName"]')
    input.send_keys(credentials["firstName"])
    input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_lastName"]')
    input.send_keys(credentials["lastName"])
    input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_address1"]')
    input.send_keys(credentials["street"] + ' ' + credentials["house_number"])
    input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_address2"]')
    input.send_keys(" ")
    input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_city"]')
    input.send_keys(credentials["city"])
    input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_postal"]')
    input.send_keys(credentials["postal"])
    input = driver.find_element_by_xpath('//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_states_state"]')
    input.send_keys(credentials["state"])

credentials = ReadOrWriteCredentials.rw_credentials()
driver = webdriver.Chrome()
connecting_to_site()
clicking_to_buy()
driver.implicitly_wait(5)
inserting_shipping()
driver.implicitly_wait(5)
driver.quit()

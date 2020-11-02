import requests
import json
from selenium import webdriver
import time
import ReadOrWriteCredentials

def availability_check():
    r = requests.get('https://www.shoepalace.com/collections/men/products.json')
    products = json.loads((r.text))['products']
    for product in products:
        # print(product['title'])
        product_name = product['title']
        if product_name == 'Air Max 97 Mens Running Shoe (White)':
            product_url = 'https://www.shoepalace.com/collections/men/products/' + product['handle']
            print('Found Item')
            return (product_url)
    else:
        return False


def checkout_process(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get(str(url))

    # Selecting Size
    driver.find_element_by_xpath('//div[@data-value="9.5"]').click()
    time.sleep(2)

    # Add To Cart
    driver.find_element_by_xpath('//div[@class="productForm-buttons"]').click()
    time.sleep(3)

    # Checkout
    driver.find_element_by_xpath('//button[@name="checkout"]').click()
    time.sleep(1)

    # Email
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(credentials["email"])
    time.sleep(1)

    # First Name
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys(credentials["firstName"])
    time.sleep(1)

    # Last Name
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys(credentials["lastName"])
    time.sleep(1)

    # Addres
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys(credentials["street"] + ' ' + credentials["house_number"])
    time.sleep(1)

    # City
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys(credentials["city"])
    time.sleep(1)

    # Zip
    driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys(credentials["ZIP"])
    time.sleep(1)

    # phone
    driver.find_element_by_xpath('//input[@placeholder="Phone"]').send_keys(credentials["cellphone"] + u'\ue007')

    # Continue to Payment
    driver.find_element_by_xpath('//button[@id="continue_button"]').click()

    # Card Number
    driver.find_element_by_xpath('//input[@placeholder="Card number"]').send_keys('1234567890')

    # Name on Card
    driver.find_element_by_xpath('//input[@placeholder="Name on card"]').send_keys('Harry Potter')

    #  Expiration Data
    driver.find_element_by_xpath('//input[@placeholder="Expiration date (MM / YY)"]').send_keys('0121')

    #  Security Code
    driver.find_elements_by_xpath('//input[@placeholder="Security code"]').send_keys('123' + u'\ue007')

credentials = ReadOrWriteCredentials.rw_credentials()
while True:
    my_url = availability_check()
    if my_url != False:
        checkout_process(my_url)
        break
    else:
        print('No')

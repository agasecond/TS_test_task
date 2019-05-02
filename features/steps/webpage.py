from selenium import webdriver
from behave import *


@step('I get userlist from webpage')
def get_users_from_webpage(context):
    chromedriver = r'C:\Users\Andrey\PycharmProjects\TS_test_task\utils\chromedriver.exe'
    browser = webdriver.Chrome(chromedriver)
    browser.get('http://146.185.143.168')

    username = browser.find_element_by_id("username")
    username.send_keys("administrator")
    browser.find_element_by_xpath('//input[@value="Login"]').click()

    password = browser.find_element_by_id("password")
    password.send_keys("mantisbt2019")
    browser.find_element_by_xpath('//input[@value="Login"]').click()

    browser.get('http://146.185.143.168/manage_user_page.php')
    table_id = browser.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div/table/tbody')
    rows = table_id.find_elements_by_tag_name("tr")
    users_from_webpage = set()
    for row in rows:
        col = row.find_elements_by_tag_name("td")[0]
        users_from_webpage.add(col.text)
    context.users_from_webpage = users_from_webpage

import pytest
import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_checking_add_to_basket_button(browser):
    # open page
    browser.get(link)
    #time.sleep(30)
    
    # find buttons
    button = browser.find_elements_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    # count buttons
    button_cnt = len(button)
    
    assert button_cnt == 1, "The basket button is missing!"

# -*- coding: utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open_gcp_calc():
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get('https://cloud.google.com/products/calculator/')



open_gcp_calc()

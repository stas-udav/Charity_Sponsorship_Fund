#! /usr/bin/env python3
from functions import *
from classes import *

def test_reports():
    reports_page = ReportsPage(webdriver.Chrome())
    reports_page.open()
    reports_page.loading_check()
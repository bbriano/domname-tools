#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import time

URL = "https://domains.google.com/registrar/search?searchTerm=%s"

for line in sys.stdin:
    domname = line[:-1]

    opts = Options()
    # opts.headless = True
    driver = webdriver.Chrome(options=opts)
    driver.get(URL % domname)
    time.sleep(2)

    try:
        driver.find_element_by_xpath("/html/body/domains-app/div/div/main/dreg-router-outlet/div/search-root/responsive-centered-container/div/div/search-results/div/mat-tab-group/div/mat-tab-body[1]/div/related-search-results/exact-match-card/div/search-result-card-header/search-result-card-header-desktop/gmat-card/div/div[2]/row-tags/dreg-tag")
        available = True
    except:
        available = False

    if available:
        print(domname)
    driver.close()

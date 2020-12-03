# -*- coding: utf-8 -*-

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome


@pytest.fixture
def driver(request):
    driver = Chrome(ChromeDriverManager().install())

    def quit():
        driver.quit()

    request.addfinalizer(quit)
    return driver

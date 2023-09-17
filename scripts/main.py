from selenium import webdriver
#from selenium.webdriver.common.by import By

def get_driver():
    """ Set up Selenium webdriver for Chrome"""
    #options = webdriver.FirefoxOptions()
    options = webdriver.ChromeOptions()
    options.add_argument("disable_infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
                                    ["enable-automation"])

    options.add_argument(
                         "disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    return driver

def main():
    """Main script"""
    driver = get_driver()
    driver.get("http://automated.pythonanywhere.com")
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    print(element.text)

if __name__ == "__main__":
    main()

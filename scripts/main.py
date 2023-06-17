from selenium import webdriver


def main():
    """Main script"""
    options = webdriver.ChromeOptions()
    options.add_argument("disable_infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
                                    ["enable-automation"])
    options.add_argument(
                         "disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome()


if __name__ == "__main__":
    main()

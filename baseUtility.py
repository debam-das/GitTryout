from selenium import webdriver


class baseutility:
    def __init__(self):
        self.__driver = webdriver.Chrome()

    def initialization(self, browserName, url):
        if browserName == "chrome":
            self.__driver = webdriver.Chrome()
        elif browserName == "firefox":
            self.__driver = webdriver.Firefox()
        elif browserName == "IE":
            self.__driver = webdriver.Ie()
        else:
            pass
        self.__driver.get(url)

    def getDriver(self):
        return self.__driver

    def termination(self):
        self.__driver.close()
        self.__driver.quit()

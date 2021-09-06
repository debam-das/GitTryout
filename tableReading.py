from selenium import webdriver
from pythonFirstPage import serachPage
from baseUtility import baseutility

# class testCase():
#     def start(cls):
#         cls.driver=webdriver.Chrome()
#         cls.driver.get("http://www.python.org")
#     def process(self):
#         obj=serachPage(self.driver)
#         obj.firstMetohd()
#     def closure(cls):
#         cls.driver.close()
#         cls.driver.quit()
    
# obj1=testCase()
# obj1.start()
# obj1.process()
# obj1.closure()

#1st test case Exctution using POM style 
bu=baseutility()
bu.intialiazation("firefox","http://www.python.org")
sp=serachPage(bu.getDriver())
sp.firstMetohd("pycon")
bu.tremination()

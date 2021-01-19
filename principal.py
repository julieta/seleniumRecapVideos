from selenium import webdriver
import unittest
#import time
from pages.pageindex import *

#driver = webdriver.Chrome('/home/juli/PycharmProjects/autorep/chromedriver')
#driver.get('http://localhost/apptitud/sistema-administracion/')
#driver.find_element_by_name('username').send_keys('max@power.com')
#driver.find_element_by_name('pass').send_keys('power')
#driver.find_element_by_xpath('/html/body/div/div/div/div/login/div/div[2]/form/div[3]/div/action-button/button').click()
#time.sleep(3)
#driver.quit()

#cada prueba va ser un metodo de mi clase. Todas las pruebas que haga tienen que comenzar con el sufijo test para que
#unitest lo tome que son pruebas y no otras cosas
class Items(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
       # chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('/home/juli/PycharmProjects/autorep/chromedriver', options=chrome_options)
        self.driver.get('http://automationpractice.com/index.php')

    def test_view_item_page(self):
        page_index = Page_index(self.driver) #aca cree el objeto page_index de la clase Page_index
        page_index.search_items('dress')
        self.driver.implicitly_wait(5) #esperar que cargue la pagina para que esté disponible para usar
        self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()
        title = self.driver.find_element_by_xpath('//*[@id="center_column"]/div/div/div[3]/h1').text
        self.assertEqual(title, 'Printed Summer Dress', 'Text should be different')

    def test_search_with_no_items(self):
        page_index = Page_index(self.driver) #aca cree el objeto page_index de la clase Page_index
        page_index.search_items('computer')


    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()

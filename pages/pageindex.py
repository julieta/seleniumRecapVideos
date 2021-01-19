class Page_index():
    def __init__(self, driver): #es un contructor y vamos hacer que nos traiga el driver
        self.driver = driver

    def search_items(self, item):
        self.driver.find_element_by_id('search_query_top').send_keys(item)
        self.driver.find_element_by_name('submit_search').click()
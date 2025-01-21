from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from utilities.utils import Utils

from base.base_driver import BaseDriver

class SearchResults(BaseDriver):
    log = Utils.cust_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _1_STOP_FILTER_ELEMENT = "//div[contains(@class,'filter-stops')]/descendant::p[text()=1]"
    _2_STOPS_FILTER_ELEMENT = "//div[contains(@class,'filter-stops')]/descendant::p[text()=2]"
    _NON_STOP_FILTER_ELEMENT = "//div[contains(@class,'filter-stops')]/descendant::p[text()=0]"
    SEARCH_RESULTS_STOP = "//div[@class='flightItem border-shadow pr']/descendant::span[contains(text(),'Stop')][1]"
    PROGRESS_BAR_SEARCH_RESULTS_PAGE = ".flight-loader"

    def wait_for_all_results_to_be_fetched(self):
        self.wait_for_presence_of_element_located(By.CSS_SELECTOR, self.PROGRESS_BAR_SEARCH_RESULTS_PAGE)
        try:
            self.wait_for_text_to_be_present_in_element_attribute(By.CSS_SELECTOR, self.PROGRESS_BAR_SEARCH_RESULTS_PAGE, "class",
                                                                        "ng-hide")
        except TimeoutException:
            self.log.warning("Timeout Waiting for progress bar in search results page to hide")

    def get_1_stop_filter_element(self):
        return self.driver.find_element(By.XPATH,self._1_STOP_FILTER_ELEMENT)

    def get_2_stops_filter_element(self):
        return self.driver.find_element(By.XPATH,self._2_STOPS_FILTER_ELEMENT)

    def get_non_stop_filter_element(self):
        return self.driver.find_element(By.XPATH,self._NON_STOP_FILTER_ELEMENT)

    def get_results_all_stops(self):
        return self.driver.find_elements(By.XPATH,self.SEARCH_RESULTS_STOP)

    def filter_by_stops(self,num_of_stops):
        self.log.debug("Number of Stops = {}".format(num_of_stops))
        if num_of_stops == 1:
            self.log.info("Filtering flights by 1 Stop")
            self.get_1_stop_filter_element().click()
            return  "1 Stop"
        elif num_of_stops == 2:
            self.log.info("Filtering flights by 2 Stops")
            self.get_2_stops_filter_element().click()
            return  "2 Stops"
        elif num_of_stops == 0:
            self.log.info("Filtering flights by 0 Stops")
            self.get_non_stop_filter_element().click()
            return  "Non Stop"
        else:
            self.log.error("Please provide valid filter option. Value received is: {}".format(num_of_stops))

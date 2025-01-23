from time import sleep

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_results_page import SearchResults
from utilities.utils import Utils


class YatraHomePage(BaseDriver):
    log = Utils.cust_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =  driver

    #Locators
    # DEPART_FROM_FIELD = "(//div[@class='MuiBox-root css-1epn4zm']/descendant::p[@class='MuiTypography-root MuiTypography-body1  css-17kn1z8'])[1]"
    # DEPART_FROM_FIELD = "(//p[@class ='MuiTypography-root MuiTypography-body1 css-17kn1z8'])[1]"
    DEPART_FROM_FIELD = "(//p[contains(@class,'css-17kn1z8')])[1]"
    DEPART_FROM_INPUT_FIELD = "#input-with-icon-adornment"
    FROM_CITY_AUTO_SUGGESTIONS_LIST_LOCATOR = "//div[@class='MuiBox-root css-134xwrj']/descendant::li"
    FROM_CITY_AUTO_SUGGESTIONS_CONTAINER = "//div[@class='MuiBox-root css-134xwrj']"
    # GOING_TO_FIELD = "(//div[@class='MuiBox-root css-1epn4zm']/descendant::p[@class='MuiTypography-root MuiTypography-body1  css-17kn1z8'])[2]"
    # GOING_TO_FIELD = "(//p[@class ='MuiTypography-root MuiTypography-body1 css-17kn1z8'])[2]"
    GOING_TO_FIELD = "(//p[contains(@class,'css-17kn1z8')])[2]"
    GOING_TO_INPUT_FIELD = "#input-with-icon-adornment"
    TO_CITY_AUTO_SUGGESTIONS_LIST_LOCATOR = "//div[@class='MuiBox-root css-134xwrj']/descendant::li"
    TO_CITY_AUTO_SUGGESTIONS_CONTAINER = "//div[@class='MuiBox-root css-134xwrj']"
    # DEPARTURE_DATE_FIELD = ".css-rd021u"
    DEPARTURE_DATE_FIELD = "(//div[@class ='css-rd021u'])[1]"
    NAVIGATE_MONTH_BUTTON = "(//button[@class='react-datepicker__navigation react-datepicker__navigation--next'])[2]"
    MONTH_YEAR_ELEMENTS_LOCATOR = ".react-datepicker__current-month"
    # SEARCH_BUTTON = "div[class='MuiBox-root css-1pr41rr'] button[type='button']"
    SEARCH_BUTTON = "//button[text()='Search']"


    MULTI_CITY_RADIO_BUTTON = "//h4[normalize-space() = 'Multi City']"

    # DEPART_FROM_FIELD_2 = "(//p[@class ='MuiTypography-root MuiTypography-body1 css-17kn1z8'])[3]"
    DEPART_FROM_FIELD_2 = "(//p[contains(@class,'css-17kn1z8')])[3]"
    DEPART_FROM_INPUT_FIELD_2 = "#input-with-icon-adornment"
    FROM_CITY_AUTO_SUGGESTIONS_LIST_LOCATOR_2 = "//div[@class='MuiBox-root css-134xwrj']/descendant::li"
    FROM_CITY_AUTO_SUGGESTIONS_CONTAINER_2 = "//div[@class='MuiBox-root css-134xwrj']"
    # GOING_TO_FIELD_2 = "(//p[@class ='MuiTypography-root MuiTypography-body1 css-17kn1z8'])[4]"
    GOING_TO_FIELD_2 = "(//p[contains(@class,'css-17kn1z8')])[4]"
    GOING_TO_INPUT_FIELD_2 = "#input-with-icon-adornment"
    TO_CITY_AUTO_SUGGESTIONS_LIST_LOCATOR_2 = "//div[@class='MuiBox-root css-134xwrj']/descendant::li"
    TO_CITY_AUTO_SUGGESTIONS_CONTAINER_2 = "//div[@class='MuiBox-root css-134xwrj']"
    DEPARTURE_DATE_FIELD_2 = "(//div[@class ='css-rd021u'])[2]"
    NAVIGATE_MONTH_BUTTON_2 = "(//button[@class='react-datepicker__navigation react-datepicker__navigation--next'])[2]"
    MONTH_YEAR_ELEMENTS_LOCATOR_2 = ".react-datepicker__current-month"

    CALENDAR_CONTAINER = ".MuiBox-root.css-1hl8t8y"

    def handle_republic_day_dialogue(self):
        self.wait_for_frame_to_be_available_and_switch(By.ID,"webklipper-publisher-widget-container-notification-frame")
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,".wewidgeticon.we_close.icon-large").click()
        self.driver.switch_to.default_content()

    def get_depart_from_field(self):
        return self.driver.find_element(By.XPATH,self.DEPART_FROM_FIELD)

    def get_depart_from_input_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.DEPART_FROM_INPUT_FIELD)

    def get_all_from_cities_locators_auto_suggestions(self):
        return self.driver.find_elements(By.XPATH, self.FROM_CITY_AUTO_SUGGESTIONS_LIST_LOCATOR)

    def get_locator_from_city_auto_suggestions_container(self):
        return self.FROM_CITY_AUTO_SUGGESTIONS_CONTAINER

    def get_going_to_field(self):
        return self.driver.find_element(By.XPATH,self.GOING_TO_FIELD)

    def get_going_to_input_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.GOING_TO_INPUT_FIELD)

    def get_all_to_cities_locators_auto_suggestions(self):
        return self.driver.find_elements(By.XPATH, self.TO_CITY_AUTO_SUGGESTIONS_LIST_LOCATOR)

    def get_locator_to_city_auto_suggestions_container(self):
        return self.TO_CITY_AUTO_SUGGESTIONS_CONTAINER

    def get_locator_calendar_container(self):
        return self.CALENDAR_CONTAINER

    def get_departure_date_field(self):
        # return self.driver.find_element(By.CSS_SELECTOR, self.DEPARTURE_DATE_FIELD)
        return self.driver.find_element(By.XPATH, self.DEPARTURE_DATE_FIELD)

    def get_navigate_month_button(self):
        return self.driver.find_element(By.XPATH,self.NAVIGATE_MONTH_BUTTON)

    def get_month_year_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.MONTH_YEAR_ELEMENTS_LOCATOR)

    def get_date_element (self,departure_date):
        if int(departure_date[0]) <= 9:
            return self.driver.find_element(By.XPATH,
                                 "//div[contains(@class,'react-datepicker__day--00{date}')][contains(@aria-label,'{month}')]".format(
                                     date=departure_date[0], month=departure_date[1]))
        elif 10<=int(departure_date[0]) <= 31:
            return self.driver.find_element(By.XPATH,
                                     "//div[contains(@class,'react-datepicker__day--0{date}')][contains(@aria-label,'{month}')]".format(
                                         date=departure_date[0], month=departure_date[1]))
        else:
            return

    def get_search_button_element(self):
        # return self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_BUTTON)
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def get_locator_search_button_element(self):
        # return self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_BUTTON)
        return self.SEARCH_BUTTON

    def select_departure_from(self,from_city):
        # Click and send first 3 characters of 'from city'
        self.get_depart_from_field().click()
        self.get_depart_from_input_field().send_keys(from_city[0:3])
        sleep(1)
        # Get the list of  auto  suggestions of  'from city'
        from_city_list= self.get_all_from_cities_locators_auto_suggestions()

        # find and click on the 'from city' from the above list
        for city in from_city_list:
            if from_city in city.text:
                city.click()
                break

        # wait for autosuggestion list to disappear from dom
        self.wait_until_element_not_present(By.XPATH, self.get_locator_from_city_auto_suggestions_container())

    def select_going_to(self,to_city):
        # Click and send first 3 characters of 'to  city'
        self.get_going_to_field().click()
        self.get_going_to_input_field().send_keys(to_city[0:3])
        sleep(1)
        # Get the list of  auto  suggestions of  'to city'
        to_city_list = self.get_all_to_cities_locators_auto_suggestions()

        # find and click on the 'to city' from the above list
        for city in to_city_list:
            if to_city in city.text:
                city.click()
                break

        # wait for autosuggestion list to disappear from dom
        self.wait_until_element_not_present(By.XPATH, self.get_locator_to_city_auto_suggestions_container())

    def select_departure_date(self,departure_date):

        # click on departure date field
        self.get_departure_date_field().click()

        month_found = False

        # locator for navigating to next 2 months
        navigate_to_next_month_button = self.get_navigate_month_button()
        # navigating to  the year and  month
        while not month_found:
            months_years_in_view =  self.get_month_year_elements()
            for my in months_years_in_view:
                if departure_date[2] in my.text:
                    if departure_date[1] in my.text:
                        month_found = True
                        break
            if month_found:
                break
            if "hidden" not in navigate_to_next_month_button.get_attribute("style"):
                navigate_to_next_month_button.click()
                navigate_to_next_month_button.click()
            else:
                break

        # selecting the date
        if month_found:
            if int(departure_date[0]) <= 9:
                date_found = self.get_date_element(departure_date)
                if "react-datepicker__day--disabled" in date_found.get_attribute(
                        "class") or "react-datepicker__day--outside-month" in date_found.get_attribute("class"):
                    self.log.error("The date is not selectable")
                else:
                    date_found_value = date_found.get_attribute("aria-label").removeprefix("Choose ")
                    date_found.click()
                    self.log.info("Date " + date_found_value + " selected")

            elif 10 <= int(departure_date[0]) <= 31:
                date_found = self.get_date_element(departure_date)
                if "react-datepicker__day--disabled" in date_found.get_attribute(
                        "class") or "react-datepicker__day--outside-month" in date_found.get_attribute("class"):
                    self.log.error("The date is not selectable")
                else:
                    date_found_value = date_found.get_attribute("aria-label").removeprefix("Choose ")
                    date_found.click()
                    self.log.info("Date " + date_found_value + " selected")
            else:
                self.log.error("Date should be in between 1 and 31")
        else:
            self.log.error("Month,Year not found")

    def click_on_search(self):
        # clicking on the search button
        self.get_search_button_element().click()

    def search_flights(self,from_city,to_city,departure_date):
        self.select_departure_from(from_city)
        self.select_going_to(to_city)
        self.log.debug("Departure date is " + str(departure_date))
        self.select_departure_date(departure_date)
        self.click_on_search()
        search_results = SearchResults(self.driver)
        return search_results

##################################################################################################################

    ##
    # get from city field_2
    # click
    # get from city input field_2
    # send keys
    # pick from city_2 from auto suggestions


    def get_multi_city_radio_button(self):
        return self.driver.find_element(By.XPATH,self.MULTI_CITY_RADIO_BUTTON)

    def click_on_multi_city_radio_button(self):
        self.get_multi_city_radio_button().click()

    def get_depart_from_field_2(self):
        return self.driver.find_element(By.XPATH,self.DEPART_FROM_FIELD_2)

    def get_depart_from_input_field_2(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.DEPART_FROM_INPUT_FIELD_2)

    def get_all_from_cities_locators_auto_suggestions_2(self):
        return self.driver.find_elements(By.XPATH, self.FROM_CITY_AUTO_SUGGESTIONS_LIST_LOCATOR_2)

    def get_locator_from_city_auto_suggestions_container_2(self):
        return self.FROM_CITY_AUTO_SUGGESTIONS_CONTAINER_2

    def get_going_to_field_2(self):
        return self.driver.find_element(By.XPATH,self.GOING_TO_FIELD_2)

    def get_going_to_input_field_2(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.GOING_TO_INPUT_FIELD_2)

    def get_all_to_cities_locators_auto_suggestions_2(self):
        return self.driver.find_elements(By.XPATH, self.TO_CITY_AUTO_SUGGESTIONS_LIST_LOCATOR_2)

    def get_locator_to_city_auto_suggestions_container_2(self):
        return self.TO_CITY_AUTO_SUGGESTIONS_CONTAINER_2

    def get_departure_date_field_2(self):
        # return self.driver.find_element(By.CSS_SELECTOR, self.DEPARTURE_DATE_FIELD)
        return self.driver.find_element(By.XPATH, self.DEPARTURE_DATE_FIELD_2)

    def get_navigate_month_button_2(self):
        return self.driver.find_element(By.XPATH,self.NAVIGATE_MONTH_BUTTON_2)

    def get_month_year_elements_2(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.MONTH_YEAR_ELEMENTS_LOCATOR_2)

    def get_date_element_2 (self,departure_date):
        if int(departure_date[0]) <= 9:
            return self.driver.find_element(By.XPATH,
                                 "//div[contains(@class,'react-datepicker__day--00{date}')][contains(@aria-label,'{month}')]".format(
                                     date=departure_date[0], month=departure_date[1]))
        elif 10<=int(departure_date[0]) <= 31:
            return self.driver.find_element(By.XPATH,
                                     "//div[contains(@class,'react-datepicker__day--0{date}')][contains(@aria-label,'{month}')]".format(
                                         date=departure_date[0], month=departure_date[1]))
        else:
            return


    def select_departure_from_2(self,from_city):
        # Click and send first 3 characters of 'from city'
        self.get_depart_from_field_2().click()
        self.get_depart_from_input_field_2().send_keys(from_city[0:3])
        sleep(1)
        # Get the list of  auto  suggestions of  'from city'
        from_city_list= self.get_all_from_cities_locators_auto_suggestions_2()

        # find and click on the 'from city' from the above list
        for city in from_city_list:
            if from_city in city.text:
                city.click()
                break

        # wait for autosuggestion list to disappear from dom
        self.wait_until_element_not_present(By.XPATH, self.get_locator_from_city_auto_suggestions_container_2())

    def select_going_to_2(self,to_city):
        # Click and send first 3 characters of 'to  city'
        self.get_going_to_field_2().click()
        self.get_going_to_input_field_2().send_keys(to_city[0:3])
        sleep(2)
        # Get the list of  auto  suggestions of  'to city'
        to_city_list = self.get_all_to_cities_locators_auto_suggestions_2()

        # find and click on the 'to city' from the above list
        for city in to_city_list:
            if to_city in city.text:
                city.click()
                break

        # wait for autosuggestion list to disappear from dom
        self.wait_until_element_not_present(By.XPATH, self.get_locator_to_city_auto_suggestions_container_2())

    def select_departure_date_2(self,departure_date):

        # click on departure date field
        self.get_departure_date_field_2().click()

        month_found = False

        # locator for navigating to next 2 months
        navigate_to_next_month_button = self.get_navigate_month_button_2()
        # navigating to  the year and  month
        while not month_found:
            months_years_in_view =  self.get_month_year_elements_2()
            for my in months_years_in_view:
                if departure_date[2] in my.text:
                    if departure_date[1] in my.text:
                        month_found = True
                        break
            if month_found:
                break
            if "hidden" not in navigate_to_next_month_button.get_attribute("style"):
                navigate_to_next_month_button.click()
                navigate_to_next_month_button.click()
            else:
                break

        # selecting the date
        if month_found:
            if int(departure_date[0]) <= 9:
                date_found = self.get_date_element_2(departure_date)
                if "react-datepicker__day--disabled" in date_found.get_attribute(
                        "class") or "react-datepicker__day--outside-month" in date_found.get_attribute("class"):
                    self.log.error("The date is not selectable")
                else:
                    date_found_value = date_found.get_attribute("aria-label").removeprefix("Choose ")
                    self.log.debug("date_found_value is " + date_found_value)
                    date_found.click()
                    self.log.info("Date " + date_found_value + " selected")
                    # self.wait_for_element_to_be_clickable(By.XPATH, self.get_locator_search_button_element())
                    self.wait_until_element_not_present(By.CSS_SELECTOR,self.get_locator_calendar_container())

            elif 10 <= int(departure_date[0]) <= 31:
                date_found = self.get_date_element_2(departure_date)
                if "react-datepicker__day--disabled" in date_found.get_attribute(
                        "class") or "react-datepicker__day--outside-month" in date_found.get_attribute("class"):
                    self.log.error("The date is not selectable")
                else:
                    date_found_value = date_found.get_attribute("aria-label").removeprefix("Choose ")
                    self.log.debug("date_found_value is " + date_found_value)
                    date_found.click()
                    self.log.info("Date " + date_found_value + " selected")
                    # self.wait_for_element_to_be_clickable(By.XPATH, self.get_locator_search_button_element())
                    self.wait_until_element_not_present(By.CSS_SELECTOR,self.get_locator_calendar_container())
            else:
                self.log.error("Date should be in between 1 and 31")
        else:
            self.log.error("Month,Year not found")


    def search_flights_multi_city_cities_2(self,from_city,to_city,departure_date,from_city_2,to_city_2,departure_date_2):

        self.click_on_multi_city_radio_button()

        self.select_departure_from(from_city)
        self.select_going_to(to_city)
        self.log.debug("Departure date is " + str(departure_date))
        self.select_departure_date(departure_date)

        self.select_departure_from_2(from_city_2)
        self.select_going_to_2(to_city_2)
        self.log.debug("Departure date_2 is " + str(departure_date_2))
        self.select_departure_date_2(departure_date_2)

        sleep(1)
        self.click_on_search()
        search_results = SearchResults(self.driver)
        return search_results


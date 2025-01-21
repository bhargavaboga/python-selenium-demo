import pytest
import softest
from time import sleep
from pages.yatra_home_page import YatraHomePage
from utilities.utils import Utils
from ddt import ddt,data,file_data,unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.cust_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.yatra_home = YatraHomePage(self.driver)
        self.utils = Utils()

    # # @data(["Hyderabad, (HYD)","Calgary, (YYC)","31,January,2025","2"],["New Delhi, (DEL)","New York, (JFK)","27,February,2025","1"])
    # # @unpack
    # # @file_data("../testdata/testdata.json")
    # # @file_data("../testdata/testdata.yaml")
    #
    @pytest.mark.xfail
    @data(*Utils.excel_reader("D:\\PythonSelenium\\TestFrameWorkDemo\\testdata\\Test_Data_Yatra.xlsx","Sheet1"))
    @unpack
    # @data(*Utils.csv_reader("D:\\PythonSelenium\\TestFrameWorkDemo\\testdata\\Test_Data_Yatra.csv"))
    # @unpack
    def test_search_flights_n_Stops(self,from_city,to_city,departure_date,num_of_stops):

        self.log.debug("Test Data is: {} {} {} {}".format(from_city,to_city,departure_date,num_of_stops))
        self.yatra_home.handle_republic_day_dialogue() ####Temp Code
        search_results = self.yatra_home.search_flights(from_city, to_city, departure_date.split(','))
        search_results.wait_for_all_results_to_be_fetched()
        self.log.info("Search is completed")
        search_results.dynamic_scrolling()
        all_flight_stops = search_results.get_results_all_stops()
        self.log.info("Total Number of  Flights: " + str(len(all_flight_stops)))
        self.log.debug("Number of Stops are: {}".format(num_of_stops))
        stops_text = search_results.filter_by_stops(num_of_stops=num_of_stops)
        sleep(2)
        filtered_flight_stops = search_results.get_results_all_stops()
        self.log.info("Number of Flights Filtered: " + str(len(filtered_flight_stops)))
        self.utils.assert_text_of_web_elem_list(filtered_flight_stops,stops_text)

    @data(*Utils.excel_reader("D:\\PythonSelenium\\TestFrameWorkDemo\\testdata\\Test_Data_Yatra.xlsx","Sheet2"))
    @unpack
    def test_search_flights_multi_city(self,from_city,to_city,departure_date,from_city_2,to_city_2,departure_date_2):

        self.log.debug("Test Data is: {} {} {} {} {} {}".format(from_city,to_city,departure_date,from_city_2,to_city_2,departure_date_2))
        self.yatra_home.handle_republic_day_dialogue() ####Temp Code
        search_results = self.yatra_home.search_flights_multi_city_cities_2(from_city,to_city,departure_date.split(','),from_city_2,to_city_2,departure_date_2.split(','))
        search_results.wait_for_all_results_to_be_fetched()
        self.log.info("Search is completed")






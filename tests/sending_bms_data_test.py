import unittest
from src.sending_bms_data import generate_random_number, logging_temperature, logging_soc,  verify_invalid_value
import src.config as Config


class sendingBMSdataTest(unittest.TestCase):

    def setUp(self) -> None:
        self.charging_temperature_list = generate_random_number(Config.sensor_value_count,
                                                                Config.first_sensor_value['min_value']
                                                                , Config.first_sensor_value['max_value'])
        self.state_of_charge_list = generate_random_number(Config.sensor_value_count,
                                                           Config.second_sensor_value['min_value'],
                                                           Config.second_sensor_value['max_value'])

    def test_charging_temperature(self):
        logging_temperature("charging temperature", self.charging_temperature_list)

    def test_second_state_of_charge(self):
        logging_soc("state_of_charge", self.state_of_charge_list)

    def test_check_invalid_value(self):
        self.assertFalse(verify_invalid_value(0, 0, 45))
        self.assertTrue(verify_invalid_value(-1, 0, 0))
        self.assertFalse(verify_invalid_value(20, 0, 45))
        self.assertTrue(verify_invalid_value(-20, 0, 100))
        self.assertTrue(verify_invalid_value(-1, 0, -1))
        self.assertTrue(verify_invalid_value(46, 0, 45))
        self.assertTrue(verify_invalid_value(110, 0, 100))
        self.assertTrue(verify_invalid_value(110, -1, 100))

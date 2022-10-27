import unittest
from Sender.sending_bms_data import generate_random_number, verify_invalid_value, data_length
import Sender.config as Config


class sendingBMSdataTest(unittest.TestCase):

    def setUp(self) -> None:
        self.charging_temperature_list = generate_random_number(Config.sensor_value_count,
                                                                Config.first_sensor_value['min_value']
                                                                , Config.first_sensor_value['max_value'])
        self.state_of_charge_list = generate_random_number(Config.sensor_value_count,
                                                           Config.second_sensor_value['min_value'],
                                                           Config.second_sensor_value['max_value'])

    def test_check_invalid_value(self):
        self.assertFalse(verify_invalid_value(0, 0, 45))
        self.assertTrue(verify_invalid_value(-1, 0, 0))
        self.assertFalse(verify_invalid_value(20, 0, 45))
        self.assertTrue(verify_invalid_value(-20, 0, 100))
        self.assertTrue(verify_invalid_value(-1, 0, -1))
        self.assertTrue(verify_invalid_value(46, 0, 45))
        self.assertTrue(verify_invalid_value(110, 0, 100))
        self.assertTrue(verify_invalid_value(110, -1, 100))

    def test_data_length(self):
        self.assertTrue(data_length({"temp": [0, -1, 5, 7], "soc": [-5, 2, 0, 6]}) == 4)
        self.assertFalse(data_length({"temp": [0], "soc": [2]}) == 2)
        self.assertTrue(data_length(-1) == 0)

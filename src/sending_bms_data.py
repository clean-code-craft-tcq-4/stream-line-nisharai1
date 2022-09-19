import random
import src.config as Config


def generate_random_number(n, min_num, max_num):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(min_num, max_num))
    return rand_list


def verify_invalid_value(val, min_val, max_val):
    if val < min_val or val > max_val:
        return True
    return False


def logging_temperature(sensor_val, sensor_data):
    for i in range(len(sensor_val)):
        if verify_invalid_value(sensor_data[i], Config.first_sensor_value['min_value'],
                                Config.first_sensor_value['max_value']):
            sensor_data[i] = "invalid"
        print('{{"{}":{}}}\n'.format(sensor_val, sensor_data[i]))


def logging_soc(sensor_val, sensor_data):
    for i in range(len(sensor_val)):
        if verify_invalid_value(sensor_data[i], Config.second_sensor_value['min_value'],
                                Config.second_sensor_value['max_value']):
            sensor_data[i] = "invalid"
        print('{{"{}":{}}}\n'.format(sensor_val, sensor_data[i]))

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


def data_length(data):
    if isinstance(data, dict):
        return [len(value) for key, value in data.items()][0]
    else:
        return 0


def logging_sensor_data(data):
    length = data_length(data)
    for index in range(length):
        formatted_string = '{{'
        for sensor in data:
            if verify_invalid_value(data[sensor][index], Config.range_values[sensor][0],
                                    Config.range_values[sensor][1]):
                data[sensor][index] = "INVALID VALUE"
            formatted_string = formatted_string + '"{0}":{1}'.format(sensor, data[sensor][index]) + ', '
        formatted_string = formatted_string[:len(formatted_string) - 2] + '}}\n'
        print(formatted_string.format())


def main():
    temperature_list = generate_random_number(Config.sensor_value_count, Config.range_values[Config.sensor[0]][0],
                                              Config.range_values[Config.sensor[0]][1])
    soc_list = generate_random_number(Config.sensor_value_count, Config.range_values[Config.sensor[1]][0],
                                      Config.range_values[Config.sensor[1]][1])
    logging_sensor_data({Config.sensor[0]: temperature_list, Config.sensor[1]: soc_list})


if __name__ == '__main__':
    main()

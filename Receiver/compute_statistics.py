from statistics import mean


def convert_to_single_dimension_dict(data):
    result = {}
    for i in data:
        for key in i.keys():
            if result.get(key):
                result[key].append(i[key])
            else:
                result[key] = []
                result[key].append(i[key])
    return result


simple_moving_average_indexes = [-5, None]  # for last 5


def calculate_statistics(data):
    data = convert_to_single_dimension_dict(data)
    stats = []
    for key in data.keys():
        stats.append(f"the minimum value of '{key}' is {min(data[key])}")
        stats.append(f"the maximum value of '{key}' is {max(data[key])}")
        data_set_for_simple_moving_average = data[key][
            simple_moving_average_indexes[0] : simple_moving_average_indexes[1]
        ]
        stats.append(
            f"simple moving average of last {len(data_set_for_simple_moving_average)} values for '{key}' is {mean(data_set_for_simple_moving_average)}"
        )
    return stats


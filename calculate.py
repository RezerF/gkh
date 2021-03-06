
def get_new_data():
    new_data = {
        "cold_water": float(input("cold_water")),
        "hot_water": float(input("hot_water")),
        "electricity": float(input("electricity")),
        "heat": float(input("heat")),
    }
    return new_data


old_data = {
    "cold_water": 20,
    "hot_water": 9,
    "electricity": 102,
    "heat": 178,
}

tariffs = {
    "water_in": 24.53,
    "water_out": 29.9,
    "heating_water": 2199.18,
    "electricity": 4.29,
    "heating": 2199.18,
}


def calculate_consumption(old, new):
    # return data
    consumption = {}
    for pos in old:
        value = new[pos] - old[pos]
        consumption.update([(pos, value)])
    return consumption


def send_data():
    pass


def cold_water_calc_money(consumption, tariffs):
    return (tariffs['water_in'] + tariffs['water_out']) * consumption


def hot_water_calc_money(consumption, tariffs):
    heating = tariffs['heating_water'] * consumption
    return cold_water_calc_money(consumption, tariffs) + heating


def electricity_calc_money(consumption, tariffs):
    return tariffs['electricity'] * consumption


def heating_calc_money(consumption, tariffs):
    return tariffs['heating'] * consumption


def calculate_money(consumptions):
    # consumptions = calculate_consumption(old_data, new_data)
    con_cold_water = consumptions["cold_water"]
    con_hot_water = consumptions["hot_water"]
    con_electricity = consumptions["electricity"]
    con_heating = consumptions["heat"]
    return (
            cold_water_calc_money(con_cold_water, tariffs)
            + hot_water_calc_money(con_hot_water, tariffs)
            + electricity_calc_money(con_electricity, tariffs)
            + heating_calc_money(con_heating, tariffs)
    )

#
# print(calculate_consumption(old_data, new_data))
# print(calculate_money())

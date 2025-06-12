from data_storage import get_car_params
import numpy as np
import math

def calculate_payment(cargo_amount, distance, max_speed, cargo_multiplyer = 1.75, base = 80, car = False):
    if not car:
        ticket_speed_multipyer = (max_speed/3.6)**0.86 + 10
    else:
        ticket_speed_multipyer = (max_speed/3.6)**0.78 + 4
        base = 135
    # print(ticket_speed_multipyer)
    price_per_cargo = (0.3 + distance/1000) * cargo_multiplyer * ticket_speed_multipyer
    return cargo_amount * price_per_cargo * base

def get_fiscal_multiplyer(time):
    fical_time = 730
    return time / fical_time

def calculate_maintance(base_cost, time):
    return base_cost * get_fiscal_multiplyer(time)

def calculate_train_acceleration(P, F, m, v_max, max_distance = math.inf, max_time=3000, dt=0.01, car=False):
    """
    Рассчитывает разгон поезда с учётом ограничения мощности и тягового усилия

    Параметры:
    P - мощность локомотива (Вт)
    F - тяговое усилие (Н)
    m - общая масса поезда (кг)
    v_max - максимальная скорость (м/с)
    max_time - максимальное время расчёта (сек)
    dt - шаг времени (сек)
    """
    # Инициализация переменных
    time = np.arange(0, max_time, dt)
    velocity = np.zeros_like(time)
    distance = np.zeros_like(time)

    threshold = 0
    if not car:
        threshold = P / F
    k = 240

    for i in range(1, len(time)):
        if velocity[i - 1] <= 0.01:  # Для избежания деления на 0 в начале
            current_velocity = 0.01
        else:
            current_velocity = velocity[i - 1]

        # Вычисляем требуемую силу для текущего ускорения
        required_force = P / current_velocity

        # Проверяем ограничение по тяговому усилию
        if required_force > F and not car:
            effective_power = P / 2  # Мощность режется вдвое
        else:
            effective_power = P

        # Вычисляем новое ускорение
        if current_velocity < threshold and not car:
            a = (F - k*current_velocity)/ m
        else:
            a = (effective_power / current_velocity - k*current_velocity) / m

        # Обновляем скорость и расстояние
        velocity[i] = velocity[i - 1] + a * dt
        distance[i] = distance[i - 1] + velocity[i] * dt

        # Останавливаем расчёт при достижении максимальной скорости
        if velocity[i] >= v_max or distance[i] >= max_distance:
            time = time[:i + 1]
            velocity = velocity[:i + 1]
            distance = distance[:i + 1]
            break

    return time, velocity, distance

def get_time_to_pass_distance(_power, _force, _mass, _max_speed, _distance, _car=False, debug = False):
    time, velocity, distance = calculate_train_acceleration(_power, _force, _mass, _max_speed, _distance, car = _car)


    passed_dist = distance[-1]
    passed_time = time[-1]

    if debug:
        print(f"Расстояние разгона {passed_dist:.2f}")
        print(f"Время разгона {passed_time:.2f}")

    fullspeed_time = 0
    if passed_dist <= _distance:
        fullspeed_time = (_distance - passed_dist) / _max_speed
        if debug:
            print(f"Разгон завершён за {(_distance - passed_dist):.2f} м. до конца пути")
    elif debug:
        print(f"Разгон не завершён до конца пути")

    full_time = passed_time + fullspeed_time
    average_speed = (_distance / full_time) * 3.6
    return full_time, average_speed

def get_car_ROI(car_name, distance, road_wiggle, loaded_both_ways = False):

    car_cost, car_maintance, car_speed, car_power, car_capacity, car_mass = get_car_params(car_name)
    one_cargo_mass = 1200
    cargo_weight = car_capacity * one_cargo_mass
    loaded_car_weight = car_mass + cargo_weight
    # print(car_cost, car_maintance, car_speed, car_power, car_capacity, car_mass, cargo_weight, loaded_car_weight)

    loaded_time, _ = get_time_to_pass_distance(car_power, 0, loaded_car_weight, car_speed, distance, _car=True)

    wiggle_distance = distance*road_wiggle
    if not loaded_both_ways:
        unloaded_time, _ = get_time_to_pass_distance(car_power, 0, car_mass, car_speed, wiggle_distance, _car=True)
    else:
        unloaded_time, _ = get_time_to_pass_distance(car_power, 0, loaded_car_weight, car_speed, wiggle_distance, _car=True)


    payment = calculate_payment(car_capacity, distance, car_speed, car=True)
    if loaded_both_ways:
        payment*=2

    total_time = loaded_time + unloaded_time
    profit_per_cycle = (payment / get_fiscal_multiplyer(total_time)) - car_maintance

    roi_value = profit_per_cycle / car_cost
    return roi_value




# # Настройки
# import matplotlib.pyplot as plt
# car_name = "Тентованный Benz 1912"
# distances = range(100, 10000, 100)  # От 100 до 100000 с шагом 100
# roi_values = []
#
# # Расчет ROI для каждой дистанции
# for distance in distances:
#     roi = get_car_ROI(car_name, distance, loaded_both_ways=False)
#     roi_values.append(roi)
#
# # Построение графика
# plt.figure(figsize=(12, 6))
# plt.plot(distances, roi_values, label=f'ROI для {car_name}')
# plt.title('Зависимость ROI от дистанции')
# plt.xlabel('Дистанция (км)')
# plt.ylabel('ROI')
# plt.grid(True)
# plt.legend()
# plt.show()

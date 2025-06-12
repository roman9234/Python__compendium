from functions import *
from data_storage import get_railcar_params, get_loco_params, get_car_params
import matplotlib.pyplot as plt
import numpy as np




def simulate_train_performance(loco_name, railcar_name, car_name, road_wiggle, full_distance, loco_amount = 1, max_railcars=30, loaded_both_ways = False):
    one_cargo_mass = 1200

    # Получаем параметры локомотива
    engine_speed, P, F, engine_mass, engine_maintance, engine_price, engine_length = get_loco_params(loco_name, loco_amount)

    # Параметры вагонов
    railcar_mass, railcar_maintance, railcar_price, railcar_capacity, railcar_speed, railcar_length = get_railcar_params(railcar_name)

    # Сравнение с автомобилем
    car_roi = get_car_ROI(car_name, full_distance, road_wiggle, loaded_both_ways)

    # Подготовим массивы для хранения результатов
    railcars_counts = np.arange(0, max_railcars + 1)
    payments = []
    maintances = []
    profits = []
    roi = []
    lengths = []
    rois_for_length = []
    capacities = []
    car_rois = []

    for railcars_amount in railcars_counts:
        # Рассчитываем параметры состава
        railcars_fill_price = railcar_price * railcars_amount
        railcars_full_mass = railcar_mass * railcars_amount
        railcars_full_maintance = railcar_maintance * railcars_amount

        # Весь поезд
        full_mass = engine_mass + railcars_full_mass
        full_maintance = engine_maintance + railcars_full_maintance
        full_price = engine_price + railcars_fill_price
        full_capacity = railcar_capacity * railcars_amount
        full_loaded_mass = engine_mass + railcars_full_mass + full_capacity * one_cargo_mass
        full_length = engine_length + railcar_length * railcars_amount

        train_max_speed = min(engine_speed, railcar_speed)

        # Рассчитываем время в пути (туда с грузом, обратно без груза)
        time_loaded, _ = get_time_to_pass_distance(P, F, full_loaded_mass, train_max_speed, full_distance)
        if not loaded_both_ways:
            time_unloaded, _ = get_time_to_pass_distance(P, F, full_mass, train_max_speed, full_distance)
        else:
            time_unloaded, _ = get_time_to_pass_distance(P, F, full_loaded_mass, train_max_speed, full_distance)
        total_time = time_loaded + time_unloaded

        capacity_transfered = full_capacity
        # Рассчитываем финансовые показатели в единицу времени (в час)
        payment = calculate_payment(full_capacity, full_distance, train_max_speed)
        if loaded_both_ways:
            payment *= 2



        maintance = calculate_maintance(full_maintance, total_time)
        profit = payment - maintance

        capacity_per_cycle = capacity_transfered / get_fiscal_multiplyer(total_time)
        payment_per_cycle = payment / get_fiscal_multiplyer(total_time)
        maintance_per_cycle = maintance / get_fiscal_multiplyer(total_time)
        profit_per_cycle = profit / get_fiscal_multiplyer(total_time)

        roi_value = profit_per_cycle / full_price if full_price > 0 else 0

        payments.append(payment_per_cycle)
        maintances.append(maintance_per_cycle)
        profits.append(profit_per_cycle)
        roi.append(roi_value)
        lengths.append(full_length)
        capacities.append(capacity_per_cycle)
        car_rois.append(car_roi)

        roi_for_length = profit_per_cycle / full_length

        rois_for_length.append(roi_for_length)

        # payments.append(payment)
        # maintances.append(maintance)
        # profits.append(profit)
        # roi.append(roi_value)
    # Построение графиков
    plt.figure(figsize=(14, 10))


    # Преобразуем списки в numpy массивы
    roi_array = np.array(roi)
    car_rois_array = np.array(car_rois)
    rois_for_length_array = np.array(rois_for_length)

    # График выручки, затрат и прибыли
    plt.subplot(2, 2, 1)
    plt.plot(railcars_counts, payments, label='Выручка', color='blue', linestyle='-', linewidth=2)
    plt.plot(railcars_counts, maintances, label='Затраты', color='red', linestyle='--', linewidth=2)
    plt.plot(railcars_counts, profits, label='Прибыль', color='green', linestyle='-', linewidth=2)
    plt.xlabel('Количество вагонов', fontsize=10)
    plt.ylabel('Денежный поток за цикл ($)', fontsize=10)
    plt.title('Финансовые показатели по количеству вагонов', fontsize=12, pad=10)
    plt.legend(loc='upper left', fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.axhline(0, color='black', linewidth=0.5)

    # График рентабельности с заливкой
    plt.subplot(2, 2, 2)
    plt.plot(railcars_counts, roi_array, label='ROI поезда', color='darkgreen', linestyle='-', linewidth=2)
    plt.plot(railcars_counts, car_rois_array, label='ROI автомобиля', color='darkred', linestyle='--', linewidth=2)
    plt.axhline(0, color='black', linewidth=1, linestyle=':')
    # Заливка отрицательной области
    plt.fill_between(railcars_counts, 0, roi_array, where=(roi_array < 0),
                     color='red', alpha=0.15, interpolate=True)
    plt.fill_between(railcars_counts, 0, car_rois_array, where=(car_rois_array < 0),
                     color='red', alpha=0.15, interpolate=True)
    plt.xlabel('Количество вагонов', fontsize=10)
    plt.ylabel('ROI (прибыль/$ инвестиций)', fontsize=10)
    plt.title('Сравнение рентабельности', fontsize=12, pad=10)
    plt.legend(loc='upper right', fontsize=9)
    plt.grid(True, alpha=0.3)

    # График длины состава
    plt.subplot(2, 2, 3)
    plt.plot(railcars_counts, lengths, label='Длина состава', color='purple', linestyle='-', linewidth=2)
    plt.xlabel('Количество вагонов', fontsize=10)
    plt.ylabel('Длина (метры)', fontsize=10)
    plt.title('Длина железнодорожного состава', fontsize=12, pad=10)
    plt.legend(loc='upper left', fontsize=9)
    plt.grid(True, alpha=0.3)

    # График ROI на метр с заливкой
    plt.subplot(2, 2, 4)
    plt.plot(railcars_counts, rois_for_length_array, label='Прибыль/метр', color='orange', linestyle='-', linewidth=2)
    plt.axhline(0, color='black', linewidth=1, linestyle=':')
    # Заливка отрицательной области
    plt.fill_between(railcars_counts, 0, rois_for_length_array, where=(rois_for_length_array < 0),
                     color='red', alpha=0.15, interpolate=True)
    plt.xlabel('Количество вагонов', fontsize=10)
    plt.ylabel('Прибыль на метр состава ($/м)', fontsize=10)
    plt.title('Эффективность использования длины', fontsize=12, pad=10)
    plt.legend(loc='upper right', fontsize=9)
    plt.grid(True, alpha=0.3)

    plt.tight_layout(pad=3.0)
    plt.show()

    # Найдем оптимальное количество вагонов
    # optimal_idx = np.argmax(profits)
    optimal_idx = np.argmax(roi)
    print(f"Оптимальное количество вагонов по прибыли: {railcars_counts[optimal_idx]}")
    print(f"Прибыль за цикл: {profits[optimal_idx]:.0f}")
    print(f"Рентабельность при этом: {roi[optimal_idx]:.3f}")
    print(f"Пропускная способность: {capacities[optimal_idx]:.4f}")
    print(f"Длина при этом: {lengths[optimal_idx]:.4f}")
    print(f"Циклов до окупаемости: {1 / roi[optimal_idx]:.4f}")

    # print()
    # optimal_idx = np.argmax(rois_for_length)
    # print(f"Оптимальное количество вагонов по длине: {railcars_counts[optimal_idx]}")
    # print(f"Прибыль за цикл: {profits[optimal_idx]:.0f}")
    # print(f"Рентабельность при этом: {roi[optimal_idx]:.3f}")
    # print(f"Пропускная способность: {capacities[optimal_idx]:.4f}")
    # print(f"Длина при этом: {lengths[optimal_idx]:.4f}")
    # print(f"Циклов до окупаемости: {1 / roi[optimal_idx]:.4f}")




def simulate_varying_distance(loco_name, railcar_type, car_name, road_wiggle, railcars_amount, min_distance=500, max_distance=15000, step=100, loaded_both_ways = False):
    one_cargo_mass = 1200

    # Получаем параметры локомотива
    engine_speed, P, F, engine_mass, engine_maintance, engine_price, engine_length = get_loco_params(loco_name, 1)

    # Параметры вагонов
    railcar_mass, railcar_maintance, railcar_price, railcar_capacity, railcar_speed, railcar_length = get_railcar_params(railcar_type)

    # Рассчитываем параметры состава
    railcars_fill_price = railcar_price * railcars_amount
    railcars_full_mass = railcar_mass * railcars_amount
    railcars_full_maintance = railcar_maintance * railcars_amount

    # Весь поезд
    full_mass = engine_mass + railcars_full_mass
    full_maintance = engine_maintance + railcars_full_maintance
    full_price = engine_price + railcars_fill_price
    full_capacity = railcar_capacity * railcars_amount
    full_loaded_mass = engine_mass + railcars_full_mass + full_capacity * one_cargo_mass
    full_length = engine_length + railcar_length * railcars_amount

    train_max_speed = min(engine_speed, railcar_speed)

    # Подготовим массивы для хранения результатов
    distances = np.arange(min_distance, max_distance + step, step)
    payments = []
    maintances = []
    profits = []
    roi = []
    speeds = []
    lengths = []
    capacities = []
    car_rois = []

    for distance in distances:

        car_roi = get_car_ROI(car_name, distance, road_wiggle, loaded_both_ways)
        car_rois.append(car_roi)

        # Рассчитываем время в пути (туда с грузом, обратно без груза)
        time_loaded, speed_loaded = get_time_to_pass_distance(P, F, full_loaded_mass, train_max_speed, distance)
        if loaded_both_ways:
            time_unloaded, _ = get_time_to_pass_distance(P, F, full_loaded_mass, train_max_speed, distance)
        else:
            time_unloaded, _ = get_time_to_pass_distance(P, F, full_mass, train_max_speed, distance)
        total_time = time_loaded + time_unloaded
        avg_speed = 2 * distance / (time_loaded + time_unloaded)  # Средняя скорость за полный цикл

        capacity_transfered = full_capacity
        # Рассчитываем финансовые показатели в единицу времени (в час)
        payment = calculate_payment(full_capacity, distance, train_max_speed)
        if loaded_both_ways:
            payment *= 2

        maintance = calculate_maintance(full_maintance, total_time)
        profit = payment - maintance

        # Конвертируем общие показатели в почасовые

        payment_per_cycle = payment / get_fiscal_multiplyer(total_time)
        maintance_per_hour = maintance / get_fiscal_multiplyer(total_time)
        profit_per_hour = profit / get_fiscal_multiplyer(total_time)

        roi_value = profit_per_hour / full_price if full_price > 0 else 0

        payments.append(payment_per_cycle)
        maintances.append(maintance_per_hour)
        profits.append(profit_per_hour)
        roi.append(roi_value)
        speeds.append(avg_speed / 3.6)  # конвертируем м/с в км/ч
        lengths.append(full_length)
        capacities.append(capacity_transfered)

    optimal_idx = np.argmax(roi)
    print(f"Оптимальное расстояние для прибыли: {distances[optimal_idx]}")
    print(f"Прибыль за цикл: {profits[optimal_idx]:.0f}")
    print(f"Рентабельность при этом: {roi[optimal_idx]:.3f}")
    print(f"Длина при этом: {lengths[optimal_idx]:.4f}")
    print(f"Циклов до окупаемости: {1 / roi[optimal_idx]:.4f}")

    roi_array = np.array(roi)
    car_rois_array = np.array(car_rois)
    profits_array = np.array(profits)

    # Построение графиков
    plt.figure(figsize=(14, 10))

    # График 1: Финансовые показатели
    plt.subplot(2, 2, 1)
    plt.plot(distances, payments, label='Выручка', color='blue', linestyle='-', linewidth=2)
    plt.plot(distances, maintances, label='Затраты', color='red', linestyle='--', linewidth=2)
    plt.plot(distances, profits, label='Прибыль', color='green', linestyle='-', linewidth=2)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.xlabel('Расстояние перевозки (м)', fontsize=10)
    plt.ylabel('Денежный поток за цикл ($)', fontsize=10)
    plt.title(f'Финансовые показатели по расстоянию ({railcars_amount} вагонов)', fontsize=12, pad=10)
    plt.legend(loc='upper left', fontsize=9)
    plt.grid(True, alpha=0.3)

    # График рентабельности с заливкой
    plt.subplot(2, 2, 2)
    plt.plot(distances, roi_array, label='ROI поезда', color='darkgreen', linestyle='-', linewidth=2)
    plt.plot(distances, car_rois_array, label='ROI автомобиля', color='darkred', linestyle='--', linewidth=2)
    plt.axhline(0, color='black', linewidth=1, linestyle=':')
    # Заливка отрицательной области
    plt.fill_between(distances, 0, roi_array, where=(roi_array < 0),
                     color='red', alpha=0.15, interpolate=True)
    plt.fill_between(distances, 0, car_rois_array, where=(car_rois_array < 0),
                     color='red', alpha=0.15, interpolate=True)
    plt.xlabel('Расстояние перевозки (м)', fontsize=10)
    plt.ylabel('ROI (прибыль/$ инвестиций)', fontsize=10)
    plt.title('Сравнение рентабельности', fontsize=12, pad=10)
    plt.legend(loc='upper right', fontsize=9)
    plt.grid(True, alpha=0.3)

    # График 3: Скорость
    plt.subplot(2, 2, 3)
    plt.plot(distances, speeds, label='Средняя скорость', color='purple', linestyle='-', linewidth=2)
    plt.xlabel('Расстояние перевозки (м)', fontsize=10)
    plt.ylabel('Скорость (м/с)', fontsize=10)
    plt.title('Средняя скорость перевозки', fontsize=12, pad=10)
    plt.legend(loc='upper right', fontsize=9)
    plt.grid(True, alpha=0.3)

    # График прибыли на метр с заливкой
    plt.subplot(2, 2, 4)
    profit_per_meter = profits_array / distances
    plt.plot(distances, profit_per_meter, label='Прибыль на метр', color='orange', linestyle='-', linewidth=2)
    plt.axhline(0, color='black', linewidth=1, linestyle=':')
    # Заливка отрицательной области
    plt.fill_between(distances, 0, profit_per_meter, where=(profit_per_meter < 0),
                     color='red', alpha=0.15, interpolate=True)
    plt.xlabel('Расстояние перевозки (м)', fontsize=10)
    plt.ylabel('Прибыль на метр ($/м)', fontsize=10)
    plt.title('Эффективность по расстоянию', fontsize=12, pad=10)
    plt.legend(loc='upper right', fontsize=9)
    plt.grid(True, alpha=0.3)

    plt.tight_layout(pad=3.0)
    plt.show()


def get_loco_effectiveness(loco_name):
    engine_speed, P, F, engine_mass, engine_maintance, engine_price, engine_length = get_loco_params(loco_name, 1)
    print(f"Локомтив {loco_name}, эффективность равна {P / engine_mass:.0f}")
    return ""

# Пример использования

# loco_name = "Ферли"
# loco_name = "BR89 T3"
# loco_name = "4-4-2 Atlantic"
# loco_name = "PLM 220"
# loco_name = "Паровоз ОВ"
# loco_name = "2-6-0 Mogul"
# loco_name = "Паровоз Щ"


# loco_name = "Десятиколёсник"
# loco_name = "A 3/5"
loco_name = "MILW EP-2"
# loco_name = "Flying Scotsman"
# loco_name = "Крокодил"
# loco_name = "Class 9000"
print(get_loco_effectiveness(loco_name))




railcar_type = "20-тонник 1900"
# railcar_type = "15-тонник 1900"
# railcar_type = "10-тонник 1900"

car_name = "Тентованный Benz 1912"
# car_name = "Тентованный паровой грузовик 1894"

# loaded_both_ways = True
loaded_both_ways = False
distance = 2500
loco_amount = 1
road_wiggle = 2

# Пример использования
# simulate_train_performance(loco_name, railcar_type, car_name, road_wiggle, distance, loco_amount, 28, loaded_both_ways = loaded_both_ways)

railcars = 28
# railcars = 40
simulate_varying_distance(loco_name, railcar_type,  car_name, road_wiggle, railcars, min_distance=1000, max_distance=8000, step=200, loaded_both_ways = loaded_both_ways)  # Для 10 вагонов

def scenario_1():
    # Поезд для коротких дистанций
    # Scotsman может генерировать прибыль даже на 10-15 вагонах 20т

    loco_name = "Flying Scotsman"
    railcar_type = "20-тонник 1900"
    loaded_both_ways = False
    distance = 2500
    loco_amount = 1
    road_wiggle = 2

    simulate_train_performance(loco_name, railcar_type, car_name, road_wiggle, distance, loco_amount, 30,
                               loaded_both_ways=loaded_both_ways)


# scenario_1()
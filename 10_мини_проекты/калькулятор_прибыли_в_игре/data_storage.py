# Параметры локомотивов
def get_loco_params(name, loco_amount=1):
    # Локомотив симметричный
    if name == "Ферли":
        v_max = 45 /3.6 # Максимальная скорость (45 км/ч = 12.5 м/с)
        P = 310 *loco_amount*1000 # Мощность (310 кВт)
        F = 130 *loco_amount*1000 # Тяговое усилие (130 кН)
        m_loco = 90 *loco_amount*1000
        maintance = 189_184 *loco_amount
        price = 1_135_104 *loco_amount
        engine_length = 14

    # Локомотив T 3
    elif name == "BR89 T3":
        v_max = 40 /3.6
        P = 213 *loco_amount*1000
        F = 40 *loco_amount*1000
        m_loco = 30 *loco_amount*1000
        maintance = 131_181 *loco_amount
        price = 787_086 *loco_amount
        engine_length = 8.6


    # Локомотив десятикол
    elif name == "Десятиколёсник":
        v_max = 80 /3.6
        P = 700 *loco_amount*1000
        F = 100 *loco_amount*1000
        m_loco = 130 *loco_amount*1000
        maintance = 339_541 *loco_amount
        price = 2_037_246 *loco_amount
        engine_length = 19

    elif name == "A 3/5":
        v_max = 100 /3.6
        P = 1000 *loco_amount*1000
        F = 115 *loco_amount*1000
        m_loco = 107 *loco_amount*1000
        maintance = 617_351 *loco_amount
        price = 3_704_108 *loco_amount
        engine_length = 19


    elif name == "4-4-2 Atlantic":
        v_max = 100 /3.6
        P = 700 *loco_amount*1000
        F = 100 *loco_amount*1000
        m_loco = 130 *loco_amount*1000
        maintance = 432_146 *loco_amount
        price = 2_592_876 *loco_amount
        engine_length = 24

    elif name == "PLM 220":
        v_max = 60 /3.6
        P = 450 *loco_amount*1000
        F = 75 *loco_amount*1000
        m_loco = 57 *loco_amount*1000
        maintance = 271_970 *loco_amount
        price = 1_631_822 *loco_amount
        engine_length = 17

    elif name == "Паровоз ОВ":
        v_max = 60 /3.6
        P = 441 *loco_amount*1000
        F = 95 *loco_amount*1000
        m_loco = 52 *loco_amount*1000
        maintance = 266_531 *loco_amount
        price = 1_599_186 *loco_amount
        engine_length = 17

    elif name == "2-6-0 Mogul":
        v_max = 75 /3.6
        P = 400 *loco_amount*1000
        F = 80 *loco_amount*1000
        m_loco = 122 *loco_amount*1000
        maintance = 242_651 *loco_amount
        price = 1_455_908 *loco_amount
        engine_length = 19

    elif name == "Паровоз Щ":
        v_max = 75 /3.6
        P = 460 *loco_amount*1000
        F = 150 *loco_amount*1000
        m_loco = 78 *loco_amount*1000
        maintance = 279_049 *loco_amount
        price = 1_674_294 *loco_amount
        engine_length = 20

    elif name == "MILW EP-2":
        v_max = 120 /3.6
        P = 3_311 *loco_amount*1000
        F = 516 *loco_amount*1000
        m_loco = 240 *loco_amount*1000
        maintance = 2_080_353 *loco_amount
        price = 12_482_118 *loco_amount
        engine_length = 23

    elif name == "Flying Scotsman":
        v_max = 120 /3.6
        P = 1_655 *loco_amount*1000
        F = 135 *loco_amount*1000
        m_loco = 98 *loco_amount*1000
        maintance = 1_039_862 *loco_amount
        price = 6_239_176 *loco_amount
        engine_length = 21

    elif name == "Крокодил":
        v_max = 75 /3.6
        P = 1_650 *loco_amount*1000
        F = 150 *loco_amount*1000
        m_loco = 128 *loco_amount*1000
        maintance = 1_000_937 *loco_amount
        price = 6_005_622 *loco_amount
        engine_length = 20

    elif name == "Class 9000":
        v_max = 100 / 3.6
        P = 3_542 * loco_amount * 1000
        F = 430 * loco_amount * 1000
        m_loco = 355 * loco_amount * 1000
        maintance = 2_168_658 * loco_amount
        price = 13_119_948 * loco_amount
        engine_length = 31



    return v_max, P, F, m_loco, maintance, price, engine_length

# Параметры вагонов
def get_railcar_params(railcar_name):

    if railcar_name == "20-тонник 1900":
        railcar_mass = 20 * 1000
        railcar_maintance = 93_435
        railcar_price = 560_608
        railcar_capacity = 12
        railcar_speed = 80
        railcar_length = 9.5

    if railcar_name == "15-тонник 1900":
        railcar_mass = 15 * 1000
        railcar_maintance = 93_435
        railcar_price = 560_608
        railcar_capacity = 12
        railcar_speed = 80
        railcar_length = 12

    if railcar_name == "10-тонник 1900":
        railcar_mass = 10 * 1000
        railcar_maintance = 62_290
        railcar_price = 373_740
        railcar_capacity = 8
        railcar_speed = 80
        railcar_length = 10



    return railcar_mass, railcar_maintance, railcar_price, railcar_capacity, railcar_speed, railcar_length


# Параметры автомобилей
def get_car_params(car_name):
    if car_name == "Тентованный Benz 1912":
        car_cost = 85_296
        car_maintance = 14_216
        car_speed = 40 /3.6
        car_power = 35 *1000
        car_capacity = 7
        car_mass = 1.5 *1000

    if car_name == "Тентованный паровой грузовик 1894":
        car_cost = 47_416
        car_maintance = 7_903
        car_speed = 25 /3.6
        car_power = 4 *1000
        car_capacity = 6
        car_mass = 1 *1000

    return car_cost, car_maintance, car_speed, car_power, car_capacity, car_mass









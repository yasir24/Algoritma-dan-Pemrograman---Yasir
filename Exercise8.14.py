# 8.14 CARS
# Buat fungsi yang menyimpan informasi mobil dalam dictionary. Fungsi harus menerima nama produsen, 
# model mobil, dan sejumlah informasi tambahan menggunakan keyword arguments.

def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }

    for key, value in car_info.items():
        car[key] = value

    return car


car = make_car(
    "BYD",
    "outback",
    color="blue",
    tow_package=True
)

print(car)
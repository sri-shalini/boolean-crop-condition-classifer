def classify_crop(temperature, humidity, soil_moisture, rainfall):

    temperature_ok = 20 <= temperature <= 35
    humidity_ok = 40 <= humidity <= 80
    soil_moisture_ok = soil_moisture >= 40
    rainfall_ok = 20 <= rainfall <= 100

    crop_condition = (
        temperature_ok
        and humidity_ok
        and soil_moisture_ok
        and rainfall_ok
    )

    return crop_condition


def run_classifier():

    print("====================================")
    print(" BOOLEAN LOGIC CROP CLASSIFIER")
    print("====================================")

    temperature = float(input("Enter Temperature (C): "))
    humidity = float(input("Enter Humidity (%): "))
    soil_moisture = float(input("Enter Soil Moisture (%): "))
    rainfall = float(input("Enter Rainfall (mm): "))

    temperature_ok = 20 <= temperature <= 35
    humidity_ok = 40 <= humidity <= 80
    soil_moisture_ok = soil_moisture >= 40
    rainfall_ok = 20 <= rainfall <= 100

    print("\n--- Boolean Conditions ---")
    print("Temperature OK   :", temperature_ok)
    print("Humidity OK      :", humidity_ok)
    print("Soil Moisture OK :", soil_moisture_ok)
    print("Rainfall OK      :", rainfall_ok)

    result = classify_crop(
        temperature,
        humidity,
        soil_moisture,
        rainfall
    )

    print("\nFinal Classification:")

    if result:
        print("Suitable")
    else:
        print("Not Suitable")


if __name__ == "__main__":
    run_classifier()
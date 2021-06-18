temperature = float(input("What is the temperature? "))
f_or_h = (input("Farenheit or Celsius? (F/C)? "))

if f_or_h.lower() == "c":
    temperature = (temperature * 9/5) + 32 

for v in range(5, 65, 5):
    def wind_chill(temperature, v):
        return 35.74 + (0.6215 * temperature) - 35.75 * (v ** .16) + (0.4275 * temperature) * (v ** .16)
    list_of_temps = wind_chill(temperature, v)
    print(f"At temperature {temperature:.1f}F, and wind speed {v} MPH, the wind chill is: {list_of_temps:.2f}F")


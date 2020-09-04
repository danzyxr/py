from random import randint
import matplotlib.pyplot as plt


if __name__ == "__main__":
    hours_24 = list(range(1, 25))
    hours_24 = [f"0{i}:00" if i < 10 else f"{i}:00" for i in hours_24]

    temps_24 = [randint(0, 100) for each in hours_24]
    temps_24 = [float(i) + (float(randint(0, 10))/10) for i in temps_24]

    plt.figure(figsize=(15, 5))
    plt.title("Random 24-hour temps for the lulz")
    plt.xlabel("Time of day")
    plt.ylabel("Degrees °C")
    plt.plot(hours_24, temps_24)
    plt.show()

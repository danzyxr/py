import math

# Chapter 3


def signal_noise(signal, noise):
    ratio = signal / noise
    decibels = 10 * math.log10(ratio)
    return decibels


print(signal_noise(100, 10))


def get_radians(degrees):
    radians = (degrees / 180.0) * math.pi
    return radians


print(math.sin(get_radians(45)))
print(math.sqrt(2) / 2.0)

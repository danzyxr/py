def proto():
    km = 10
    mi = km / 1.61

    minutes = 43
    seconds = 30
    time_sec = (minutes * 60) + seconds
    time_min = time_sec / 60
    time_hrs = time_min / 60

    print("Minutes per mile: " + str(time_min / mi))
    print("Miles per hour: " + str(mi / time_hrs))


# Implementation


def minute_mile(dist, isKilo, min, sec):
    if isKilo is True:
        dist = dist / 1.61

    time_sec = (min * 60) + sec
    time_min = time_sec / 60
    time_hrs = time_min / 60

    return {
        "minutes per mile": str(time_min / dist),
        "miles per hour": str(dist / time_hrs),
    }


if __name__ == "__main__":
    proto()
    print(minute_mile(10, True, 43, 30))

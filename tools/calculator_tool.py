import statistics


def average(values):

    if len(values) == 0:
        return None

    return round(sum(values) / len(values), 2)


def median(values):

    if len(values) == 0:
        return None

    return round(statistics.median(values), 2)


def maximum(values):

    if len(values) == 0:
        return None

    return max(values)


def minimum(values):

    if len(values) == 0:
        return None

    return min(values)


def percentage_change(old_value, new_value):

    if old_value == 0:

        return None

    change = (
        (new_value - old_value)
        / old_value
    ) * 100

    return round(change, 2)


def percentage_increase(old_value, new_value):

    return percentage_change(
        old_value,
        new_value
    )


def percentage_decrease(old_value, new_value):

    return percentage_change(
        old_value,
        new_value
    )


if __name__ == "__main__":

    print(
        percentage_change(
            100,
            125
        )
    )

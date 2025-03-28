def lottery(data, size):
    array = []

    if data is None or size is None:
        return array

    for a in data:
        counter = 0
        for b in data:
            if a == b:
                counter += 1
        if counter == size:
            if a not in array:
                array.append(a)

    return array

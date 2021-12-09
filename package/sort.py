def selection_sort(data: list):
    for i in range(len(data) - 1):
        current_elem = data[i]
        min_index = i
        for j in range(i + 1, len(data)):
            if min(data[j]['age'], data[min_index]['age']) != data[min_index]['age']:
                min_index = j
        data[i] = data[min_index]
        data[min_index] = current_elem
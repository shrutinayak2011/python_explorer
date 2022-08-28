
def compute_average(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num

    avg = sum / len(num_list)
    return avg


num_list = [1, 2, 3, 4, 5, 6, 7]

print(compute_average(num_list))
def common_elements():
    multiples_of_3 = [i for i in range(1, 101) if i % 3 == 0]
    multiples_of_5 = [i for i in range(1, 101) if i % 5 == 0]

    set_of_multiples_of_3 = set(multiples_of_3)
    set_of_multiples_of_5 = set(multiples_of_5)

    common_elements_set = set_of_multiples_of_3.intersection(set_of_multiples_of_5)

    return common_elements_set

result = common_elements()
print("Спільні елементи:", result)

def is_present_in_list(number_to_search, list_to_search):
    counter = 0
    while (counter < len(list_to_search)):
        if number_to_search == list_to_search[counter]:
            return True
        counter += 1

    return False

print (is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9]))
print (is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9]))


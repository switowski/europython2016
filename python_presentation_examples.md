# Counting elements in a list:
    def slow_list_count(array):
        number_of_elements = 0
        for element in array:
            number_of_elements += 1
        return number_of_elements

and a better way:

    def fast_list_count(array)
        return len(array)
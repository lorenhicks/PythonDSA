my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print(" 'Bob' has hash code:", hash_function('Bob'))
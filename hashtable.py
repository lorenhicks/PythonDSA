my_list = [[], [], [], [], [], [], [], [], [], []]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print(" 'Bob' has hash code:", hash_function('Bob'))

def add(name):
    index = hash_function(name)
    my_list[index].append(name)

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)

def contains(name):
    index = hash_function(name)
    return my_list[index] == name

print(" 'Pete' is in the Hash Table:", contains('Pete'))
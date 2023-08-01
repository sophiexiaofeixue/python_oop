#chap134

def remove_even_values(dictionary):
    for key, value in dictionary.items():
        if value % 2 == 0:
            del dictionary[key]


my_dictionary = {"a":1, "b":2, "c":3, "d":4}
remove_even_values(my_dictionary) # will throw an error

# runtime error. dictionary changed size during running
# deletion occurs in the for loop
# mutate the dictionary
# violates dictionary.items()
# an example of risk of mutation



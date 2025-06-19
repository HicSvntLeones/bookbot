def get_word_count(string):
    split_string = string.split()
    word_count = len(split_string)
    return word_count 

def get_character_count(string):
    count_dictionary = {}
    for i in range (0, len(string)):
        char = string[i]
        char = char.lower()
        if char in count_dictionary:
            count_dictionary[char] +=1
        else:
            count_dictionary[char] = 1
        # print (count_dictionary[char])
    del count_dictionary[" "]
    return count_dictionary

def sorter(dict):
    return dict["num"]

def sort_salad(unsorted_salad):
    sorted_salad = []
    keys_list = list(unsorted_salad.keys())
    #print(keys_list)
    for i in range (0, len(unsorted_salad)):
        temp_num = unsorted_salad[keys_list[i]]
        #print (temp_num)
        sorted_salad.append({"key":keys_list[i], "num":temp_num})
        #print (sorted_salad[i])
    #print (sorted_salad)
    sorted_salad.sort(reverse=True, key=sorter)
    #print (sorted_salad)
    return sorted_salad 
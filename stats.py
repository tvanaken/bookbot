def get_book_count(fht):
    with open(fht) as f:
        file_contents = f.read()
        f.close()
    content_length = file_contents.split()

    return len(content_length)

def get_char_count(fht):
    with open(fht) as f:
        file_contents = f.read()
        f.close()
    content_length = file_contents.split()

    my_dict = {}
    for word in content_length:
        for char in word:
            if char.lower() in my_dict:
                my_dict[char.lower()] += 1
            else: 
                my_dict[char.lower()] = 1

    return my_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"letter": key, "count": dict[key]})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
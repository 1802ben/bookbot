def word_count(words):
    count = 0
    for word in words:
        count +=1
    return count


def char_count(words):
    char_dict = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict


def sort_on(dict):
    return dict["num"]


def sort_dicts(dict):
    char_list = []
    for char, count in dict.items():
       char_list.append({"char": char, "num": count})
       
    char_list = [item for item in char_list if item["char"].isalnum()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

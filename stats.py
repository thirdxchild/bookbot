def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    for char in text:
        char_lowered = char.lower()
        if char_lowered.isalpha():
            if char_lowered not in char_dict:
                char_dict[char_lowered] = 1
            else:
                char_dict[char_lowered] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def report(chars_count):
    double_dict = []
    for char in chars_count:
        count = chars_count[char]
        double_dict.append({"name": char,"num": count})
    double_dict.sort(reverse=True, key=sort_on)
    return(double_dict)
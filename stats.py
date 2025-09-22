def get_num_words(text):
    words = text.split()
    return len(words)
def character_count(text):
    character_total = {}
    for char in text:
        char = char.lower()
        if char in character_total:
            character_total[char] += 1
        else:
            character_total[char] = 1
    return character_total
def sort_on_num(d):
    return d["num"]

def character_count_sorted(character_amount):
    char_list = [{"char": k, "num": v} for k, v in character_amount.items()]
    char_list.sort(reverse=True, key=sort_on_num)
    return char_list

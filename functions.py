import json


def create_dict_from_txt_file(txt_file):
    """ Converts the txt file to a dictionary. One row in txt_file represents one flashcard, where at first there is
    a target word and then divided by '--' a native word, e.g.: cat - kot. """
    with open(txt_file, 'r') as f:
        lines = f.readlines()

    words_dict = {}
    for line in lines:
        words = line.strip().split('--')
        native_word = words[0].strip()
        target_word = words[1].strip()
        words_dict[native_word] = target_word

    return words_dict


def create_json_from_dict(words_dict):
    """ Creates json files from dictionary. Overwrites flashcards.json file. """
    with open('flashcards.json', 'w', encoding='utf-8') as f:
        json.dump(words_dict, f, ensure_ascii=False, indent=4)


create_json_from_dict(create_dict_from_txt_file('slowka.txt'))

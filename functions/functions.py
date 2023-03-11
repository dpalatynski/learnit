import json
import os


def create_dict_from_txt_file(txt_file: str) -> dict:
    """ Converts the txt file to a dictionary. One row in txt_file represents one flashcard, where at first there is
    a name of word list, the second is target word and a native word, all divided by '--'
    e.g.: animals -- cat -- kot. """
    with open(txt_file, 'r') as f:
        lines = f.readlines()

    words_dict = {}
    for line in lines:
        words = line.strip().split('--')
        word_group = words[0].strip()
        if word_group not in words_dict:  # create new list of words
            words_dict[word_group] = {}

        native_word = words[1].strip()
        target_word = words[2].strip()
        words_dict[word_group].update({native_word: target_word})

    return words_dict


def create_json_from_dict(words_dict: dict, filename='flashcards.json') -> None:
    """ Creates json files from dictionary. """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(words_dict, f, ensure_ascii=False, indent=4)


def read_json_to_dict(words_json: str, list_of_words: str) -> dict:
    """ Converts json file to dictionary """
    with open(words_json, 'r', encoding='utf-8') as f:
        words_dict = json.load(f)

    return words_dict[list_of_words]


def find_list_of_flashcards(words_json: str) -> list:
    """ Returns all lists of flashcards"""
    with open(words_json, 'r', encoding='utf-8') as f:
        words_dict = json.load(f)

    return list(words_dict.keys())


if __name__ == '__main__':
    # Create json from txt file
    create_json_from_dict(create_dict_from_txt_file(os.path.join(os.pardir, 'data\\words.txt')),
                          os.path.join(os.pardir, 'data\\flashcards.json'))

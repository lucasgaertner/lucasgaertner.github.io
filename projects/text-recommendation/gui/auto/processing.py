import re
from collections import Counter

def process_data(file_name):
    words = []
    file = open(file_name, 'r')
    lines = file.read()
    extracted = re.findall('\w+', lines)
    for w in extracted:
        w = w.lower()
        words.append(w)
    file.close()
    return words


def get_count(word_l):
    word_count_dict = {}  
    word_count_dict = Counter(word_l)
    return word_count_dict


def get_probs(word_count_dict):
    probs = {}
    m = sum(word_count_dict.values())
    for w, c in word_count_dict.items():
        p = c / m
        probs[w] = p
    return probs





from .processing import *
from .string_manipulation import *
from .combining import *
from .corrections import *
from .min_edit import min_edit_distance

import os
import numpy as np
import pandas as pd

debug = False

# Getting Vocabulary
data = os.path.join(os.getcwd(), "auto", 'shakespeare.txt')
word_l = process_data(data)
vocab = set(word_l)

word_count_dict = get_count(word_l)
if debug:  print(f"There are {len(word_count_dict)} key values pairs")
if debug:  print(f"The count for the word 'thee' is {word_count_dict.get('thee',0)}")

probs = get_probs(word_count_dict)
if debug:  print(f"Length of probs is {len(probs)}")
if debug:  print(f"P('thee') is {probs['thee']:.4f}")

# Combining edits

tmp_word = "at"
tmp_edit_one_set = edit_one_letter(tmp_word)
# turn this into a list to sort it, in order to view it
tmp_edit_one_l = sorted(list(tmp_edit_one_set))

if debug:  print(f"input word {tmp_word} \nedit_one_l \n{tmp_edit_one_l}\n")
if debug:  print(f"The type of the returned object should be a set {type(tmp_edit_one_set)}")
if debug:  print(f"Number of outputs from edit_one_letter('at') is {len(edit_one_letter('at'))}")


tmp_edit_two_set = edit_two_letters("a")
tmp_edit_two_l = sorted(list(tmp_edit_two_set))
if debug:  print(f"Number of strings with edit distance of two: {len(tmp_edit_two_l)}")
if debug:  print(f"First 10 strings {tmp_edit_two_l[:10]}")
if debug:  print(f"Last 10 strings {tmp_edit_two_l[-10:]}")
if debug:  print(f"The data type of the returned object should be a set {type(tmp_edit_two_set)}")
if debug:  print(f"Number of strings that are 2 edit distances from 'at' is {len(edit_two_letters('at'))}")


# Spelling Suggestions
my_word = 'hello' 
tmp_corrections = get_corrections(my_word, probs, vocab, 2, verbose=debug) # keep verbose=True
for i, word_prob in enumerate(tmp_corrections):
    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")


# testing implementation
source =  'play'
target = 'stay'
matrix, min_edits = min_edit_distance(source, target)
print("minimum edits: ",min_edits, "\n")
idx = list('#' + source)
cols = list('#' + target)
df = pd.DataFrame(matrix, index=idx, columns= cols)
print(df)

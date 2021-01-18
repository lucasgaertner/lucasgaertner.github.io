import itertools

def delete_letter(word, verbose=False):
    delete_l = []
    split_l = []
    split_l = [(word[:l], word[l:]) for l in range(len(word) + 1) if word[:l] is not word]
    delete_l = [(L + R[1:]) for L,R in split_l  if R]
    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")
    return delete_l

def switch_letter(word, verbose=False):
    switch_l = []
    split_l = []
    split_l = [(word[:l], word[l:]) for l in range(len(word) + 1) if word[:l] is not word]
    switch_l = [L+R[1]+R[0]+R[2:] for L,R in split_l if len(R)>1]
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}") 
    return switch_l

def replace_letter(word, verbose=False):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_l = []
    split_l = []
    split_l = [(word[:l], word[l:]) for l in range(len(word) + 1) if word[:l] is not word]
    for l in range(len(letters)):
        replace = [L+(R).replace(R[0],letters[l]) for L,R in split_l if letters[l] != R[0]]
        replace_l.append(replace)
        replace_set = list(itertools.chain.from_iterable(replace_l))
    # turn the set back into a list and sort it, for easier viewing
    replace_l = sorted(list(replace_set))
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")   
    return replace_l

# GRADED FUNCTION: inserts
def insert_letter(word, verbose=False):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_l = []
    split_l = []
    split_l = [(word[:l], word[l:]) for l in range(len(word) + 1)]
    insert_l = [L+c+R for c in letters for L,R in split_l]
    if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
    return insert_l


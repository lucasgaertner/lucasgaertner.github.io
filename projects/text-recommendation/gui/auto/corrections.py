from .combining import edit_one_letter, edit_two_letters
from collections import Counter

def get_corrections(word, probs, vocab, n=2, verbose = False):
    n_best = []
    suggestions = []

    one = edit_one_letter(word)
    two = edit_two_letters(word)
    
    if word in vocab:
        suggestions.append(word)
    elif word not in vocab:
        e1_set = set(one & vocab)
        suggestions.extend(e1_set)
    elif (len(el_set) < 1):
        e2_set = set(two & vocab)
        suggestions.extend(e2_set)
    else:
        suggestions.append(word)
        
    best_words = Counter()
    for w in suggestions:
        best_words.update({w: probs.get(w, 0)})
        
    n_best = best_words.most_common(n)
    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)
    return n_best, best_words 






if debug:  print(f"The first ten words in the text are: \n{word_l[0:10]}")
if debug:  print(f"There are {len(vocab)} unique words in the vocabulary.")

word_count_dict = get_count(word_l)
if debug:  print(f"There are {len(word_count_dict)} key values pairs")
if debug:  print(f"The count for the word 'thee' is {word_count_dict.get('thee',0)}")

probs = get_probs(word_count_dict)
if debug:  print(f"Length of probs is {len(probs)}")
if debug:  print(f"P('thee') is {probs['thee']:.4f}")


delete_word_l = delete_letter(word="cans", verbose=debug)
if debug:  print(f"Number of outputs of delete_letter('at') is {len(delete_letter('at'))}")


switch_word_l = switch_letter(word="eta", verbose=debug)
if debug:  print(f"Number of outputs of switch_letter('at') is {len(switch_letter('at'))}")

replace_l = replace_letter(word='can', verbose=debug)
if debug:  print(f"Number of outputs of switch_letter('at') is {len(switch_letter('at'))}")


insert_l = insert_letter('at', verbose=debug)
if debug:  print(f"Number of strings output by insert_letter('at') is {len(insert_l)}")
if debug:  print(f"Number of outputs of insert_letter('at') is {len(insert_letter('at'))}")


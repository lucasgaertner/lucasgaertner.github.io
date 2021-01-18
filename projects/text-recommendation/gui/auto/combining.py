from .string_manipulation import replace_letter, insert_letter, delete_letter, switch_letter

def edit_one_letter(word, allow_switches = True):
    edit_one_set = set()
    no_switch = replace_letter(word)+insert_letter(word)+delete_letter(word)
    edit_one_set = set(no_switch + switch_letter(word) if allow_switches else no_switch)
    return edit_one_set


def edit_two_letters(word, allow_switches = True):
    edit_two_set = set()
    edit_one = edit_one_letter(word,allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two_set = edit_two_set | edit_one_letter(w, allow_switches)
    return edit_two_set
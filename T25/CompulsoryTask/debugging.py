def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])            #3 NameError "k" should be "key"

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"} #1. Syntax Error changed quotations on D'oh

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) #2 TypeError (takes 2 positional arguments)  but its actually a syntax error the keys should be a list

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''


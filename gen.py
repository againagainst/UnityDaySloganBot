import random
import sys

import pymorphy2


def make_slogan():
    with open('data/zdb_selected_utf8.txt', 'r') as ifp:
        raw_data = ifp.read()
        data = raw_data.split('\n')
    
    with open('data/zdb_term_selected_utf8.txt', 'r') as ifp:
        raw_data = ifp.read()
        term_data = raw_data.split('\n')
    
    morph = pymorphy2.MorphAnalyzer()
    one = random.choice(term_data)
    two = random.choice(data) 
    three = random.choice(data)
    parsed = morph.parse(three)[0]
    three = parsed.inflect({'gent'}).word
    return "{0} — {1} {2}".format(one, two, three)
import os
import codecs
import rid
import json
full = set(range(1,365))
numbers = set()
rid_dict = rid.RegressiveImageryDictionary()
rid_dict.load_dictionary_from_string(rid.DEFAULT_RID_DICTIONARY)
rid_dict.load_exclusion_list_from_string(rid.DEFAULT_RID_EXCLUSION_LIST)

def generate_results():
    all_results = [None]*365

    for f in os.listdir('poems'):
        if f.endswith('.txt'):
            name, _, ext = f.partition('.')
            ordinal, _, number = name.partition('_')
            poem_number = int(number) - 1 # minus one for zero indexed list
            
            with codecs.open('poems/' + f, 'r', 'utf-8') as fileobj:
                contents = fileobj.read()
                results = rid_dict.analyze(contents)
                all_results[poem_number] = results
    return all_results



def slice_n_dice():
    all_results = generate_results()
    sorted_results = sorted(all_results, key=lambda x: x.word_count)
    print json.dumps([x.word_count for x in sorted_results])
    print json.dumps(['' for x in sorted_results])
       
 
slice_n_dice()

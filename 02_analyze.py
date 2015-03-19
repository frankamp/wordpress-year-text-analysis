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

def sum_window(i ,results):
    print "for", i
    totals = {}
    for result in results:
        for cat, num in result.category_count.iteritems():
            totals.setdefault(cat.full_name(), 0)
            totals[cat.full_name()] += num
    return totals

def slice_n_dice():
    all_results = generate_results()
    window = 30
    count = len(all_results)
    for i, value in enumerate(all_results):
        lower_bound = i - (window / 2)
        upper_bound = i + (window / 2)

        average_results = []
        if lower_bound < 0:
            average_results = all_results[lower_bound:] + all_results[:upper_bound]
        elif upper_bound > (count - 1):
            remainder = upper_bound - (count)
            average_results = all_results[lower_bound:] + all_results[:remainder]
        else:
            average_results = all_results[lower_bound:upper_bound]
        assert len(average_results) == window
        totals = sum_window(i, average_results)
        print "running", i
        with codecs.open('rolling_totals/%03d.json' % i, 'w', 'utf-8') as w:
            w.write(json.dumps(totals))
            

slice_n_dice()

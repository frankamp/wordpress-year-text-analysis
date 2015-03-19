import os
import codecs
import json
from datetime import date, timedelta
all_results = [None]*365
for f in os.listdir('rolling_totals'):
    if f.endswith('.json'):
        with codecs.open('rolling_totals/%s' % f, 'r', 'utf-8') as r:
            data = json.loads(r.read())
            name, _, ext = f.partition('.')
            all_results[int(name)] = data


all_percents = [None]*365
for i, r in enumerate(all_results):
    totals = {
        'primary': 0,
        'secondary': 0,
        'emotions': 0
    }
    for k, v in r.iteritems():
        totals[k.split(":")[0].lower()] += v
    cumulative = float(sum(totals.values()))
    percents = {k: v/cumulative * 100 for k, v in totals.iteritems()}
    all_percents[i] = percents

with codecs.open('load_template.js', 'r', 'utf-8') as template:
    template_string = template.read()

with codecs.open('load.js', 'w', 'utf-8') as output:
    labels = []
    data_1 = []
    data_2 = []
    data_3 = []
    last_month = ""
    for i, v in enumerate(all_percents):
        current_date = date(1900, 1, 1) + timedelta(days=i)
        current_month = current_date.strftime("%b")
        if current_month != last_month:
            last_month = current_month
            label = last_month
        else:
            label = ""
        labels.append(label) #str(i)
        data_1.append(v['primary'])
        data_2.append(v['secondary'])
        data_3.append(v['emotions'])
    output.write(template_string % (json.dumps(labels), json.dumps(data_1), json.dumps(data_2), json.dumps(data_3)))

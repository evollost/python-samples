import json
from collections import defaultdict, Counter
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

path = 'data/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(squence):
    counts = defaultdict(int)
    for x in squence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
 # two methods
counts = get_counts(time_zones)
#print top_counts(counts)
counts2 = Counter(time_zones)
#print counts2.most_common(10)

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
plt = tz_counts[:10].plot(kind='barh', rot=0).get_figure()
plt.savefig('result/tz.png')

results = Series([x.split()[0] for x in frame.a.dropna()])
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 				   'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subnet = agg_counts.take(indexer)[-10:]
normed_subnet = count_subnet.div(count_subnet.sum(1), axis=0)
plt2 = normed_subnet.plot(kind='barh', stacked=True).get_figure()
plt2.savefig('result/tz_os.png')




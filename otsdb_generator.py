import numpy as np


SAMPLE_NUMBERS=10000
START_EPOCH=1495041816
STEP = 5

METRIC_PREFIX="metric"
METRIC_NUMBER=100
TSDB_RECORD='{m} {t} {v}\n'


mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, SAMPLE_NUMBERS)

for metric_index in range(METRIC_NUMBER):
    metric_name=METRIC_PREFIX+str(metric_index)
    
    records  =[(metric_name,(START_EPOCH + i*STEP),val) for i, val in enumerate(s)]
    print(len(records))
    
    with open(metric_name+'.txt','w+') as fd:
        for r in records:
            fd.write(TSDB_RECORD.format(m=r[0],t=r[1],v=r[2]))



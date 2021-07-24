import numpy as np
import os
import pickle
from glob import glob
import pickle

"""
taggram = glob(pathname="../representations/hubert_gtzan16k/*/*")
tags = []
for t in taggram:
    tags.append(t.split("gtzan16k/")[1].split('/')[0])


with open("../representations/hubert_gtzan16k/labels.pickle", 'wb') as handle:
    pickle.dump(tags, handle, protocol=pickle.HIGHEST_PROTOCOL)"""



hubert = glob(pathname="../representations/hubert_gtzan16k/*/*")
i = 0
for rep in hubert:
    m = np.load(rep)
    if m.shape[0] != 2067:
        #print(rep)
        if m.shape[0] > 2067:
            this_m = m[:2067]
        elif m.shape[0] < 2067:
            this_m = np.concatenate((m, np.zeros((2067 - m.shape[0], 768))))
        np.save(rep, this_m)
        print(this_m.shape)
    i += 1

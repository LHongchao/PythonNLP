#coding:utf8

import os, pickle

def corpus(dir):
    for fname in os.listdir(dir):
        if fname != '.DS_Store':
            fpath = os.path.join(dir,fname)
            sentences = pickle.load(open(fpath,'rb'))
            for sentence in sentences:
                yield sentence


'''

sentences = corpus(r'D:\data\test')
for s in sentences:
    print(s)
'''


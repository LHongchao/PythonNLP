#coding:utf8

import re,os,pickle
from collections import Counter
from gensim import corpora
from gensim.models import Phrases
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import math

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

'''
这个程序是用来....，输入要求是。。。输出的是了，，
'''


def para2sentences(para):
    marks = re.compile(r'(。\(PERIODCATEGORY\)|！\(EXCLANATIONCATEGORY\)|？\(QUESTIONCATEGORY\))')
    if marks.search(para):
        sentences_with_marks = marks.split(para)#这里的split是内置函数，用来讲字符串进行切分，其中的参数是表示切分
        sentences = [''.join(sentence).strip() for sentence in zip(sentences_with_marks[0::2],sentences_with_marks[1::2])]
    else:
        sentences = [para]
    new_sentences = [s for s in sentences if s is not None]
    return new_sentences



def file2sentences_sinica(file_path):
    with open(file_path,'r',-1,encoding='utf8') as fo:
        raw_paras = fo.readlines()
    clean_paras = [para2sentences(para) for para in raw_paras if not para.startswith('###<')]
    names = os.path.split(file_path)
    outfile_name = 'out_'+names[1]
    outfile_path = os.path.join(names[0],outfile_name)
    with open(outfile_path,'w',-1,encoding='utf8') as outfile:
        for para in clean_paras:
            for sentence in para:
                sentence = sentence+'\n'
                outfile.writelines(sentence)
    return clean_paras


def file2sentences_giga(file_path):
    with open(file_path,'r',-1,encoding='utf8') as fo:
        raw_lines = fo.readlines()
        paras = []
        for i,raw_line in enumerate(raw_lines):
            if '<P>' in raw_line and i < len(raw_lines):
                while '</P>' not in raw_lines[i]:
                    i += 1
                    raw_line += raw_lines[i]
                raw_line = raw_line.replace('\n', ' ').replace('<P>', '').replace('</P>', '').strip()
                paras.append(raw_line)
    sentences = [para2sentences(para) for para in paras if para is not None]
    dir, fname = os.path.split(file_path)
    outfile_path = os.path.join(dir,'out_'+fname)
    with open(outfile_path, 'w', -1, encoding='utf8') as outfile:
        Ss = []
        for para in sentences:
            for s in para:
                outfile.writelines(s+'\n')
                Ss.append(s.strip().split(r' '))
    with open(outfile_path+'.plk','wb') as plkfile:
        pickle.dump(Ss,plkfile)


def dir2sentences_in_newfile(dir_path):
    for fname in os.listdir(dir_path):
        fpath = os.path.join(dir_path,fname)
        file2sentences_giga(fpath)

def corpus(dir):
    for fname in os.listdir(dir):
        if fname != '.DS_Store':
            fpath = os.path.join(dir,fname)
            sentences = pickle.load(open(fpath,'rb'))
            for sentence in sentences:
                yield sentence



def corpus_word_freq(dir):
    sentences = corpus(dir)
    d = Counter()
    for sentence in sentences:
        d += Counter(sentence)
    return d

def sentence_word_freq(s):
    d = {}
    for word in s:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


def sentence_word_freq(s):
    d = {}
    for word in s:
        if word in d:#{'i':1}
            d[word] += 1
        else:
            d[word] = 1
    return d


def Ss_word_freq(Ss):
    Ss_d = {}
    for s in Ss:
        for word in s:
            if word in Ss_d:
                Ss_d[word] += 1
            else:
                Ss_d[word] =1
    return Ss_d



def get_bigram(sentences):
    bi_gram_model = Phrases(sentences,min_count=1,threshold=1)
    bigram_list = []
    unigram_list = []
    for k,v in bi_gram_model.vocab.items():
        k = k.decode('utf8')
        if re.search("V_2",k):
            k = k.replace("V_2","V2")#有(V_2)敌人(Na)
            collocation = re.split(r'_', k)
            if len(collocation) == 2:
                bigram_list.append([*collocation,v])
        else:
            collocation = re.split(r'_', k)
            if len(collocation) == 2:
                bigram_list.append([*collocation,v])
            elif len(collocation) == 1:
                unigram_list.append([*collocation,v])
    bi_df = DataFrame(bigram_list)
    bi_df.columns = ['word1','word2','freq']
    bi_df.sort_values(by='freq',inplace=True,ascending=False)
    uni_df = DataFrame(unigram_list)
    uni_df.columns = ['word','freq']
    uni_df.sort_values(by='freq',inplace=True, ascending=False)
    return [uni_df,bi_df]




def ngrams(sentences,n):
    grams = []
    gram_num = 1
    while gram_num <= n:
        gram_list = []
        for s in sentences:
            [gram_list.append(tuple(s[i:i+gram_num])) for i in range(len(s)-gram_num+1)]
        grams.append(gram_list)
        gram_num += 1
    return grams

def ngrams_2(sentences,n):
    grams = []
    gram_num = 1
    while gram_num <= n:
        gram_list = []
        for s in sentences:
            [gram_list.append('_'.join(s[i:i+gram_num])) for i in range(len(s)-gram_num+1)]
        grams.append(gram_list)
        gram_num += 1
    return grams

def gram_dic(ngrams):
    dic = {}
    for ngram in ngrams:
        if ngram in dic:
            dic[ngram] += 1
        else:
            dic[ngram] = 1
    return dic

def ngrams_dic(ngram_list):
    dics_list = []
    for ngram in ngram_list:
        d = gram_dic(ngram)
        dics_list.append(d)
    return dics_list


def write_nrgams(ngrams,fpath):
    with open(fpath,'w',-1,'utf8') as fp:
        for i in range(len(ngrams)):
            for ngram in ngrams[i]:
                if i == 0:
                    fp.writelines(str(ngram[0])+'\n')
                else:
                    line = '_'.join(str(coll) for coll in ngram)
                    fp.writelines(line+'\n')


def write_dics(dics,dir):
    for i in range(len(dics)):
        dic_path = os.path.join(dir,str(i+1)+'元gram.csv')
        df = DataFrame(Series(dics[i]))
        df.to_csv(dic_path,encoding='utf_8_sig')


def build_pmi_matrix_from_bigram(corpus_dir,n=2):
    ss = list(corpus(corpus_dir))
    ngram_list = ngrams(ss,n)
    ngram_dics_List = ngrams_dic(ngram_list)
    uni_d, bi_d = ngram_dics_List[0], ngram_dics_List[1]
    unigram, bigram = DataFrame(Series(uni_d), columns=['freq']), DataFrame(Series(bi_d), columns=['freq_xy'])
    bigram['col'] = bigram.index
    bigram[['x', 'y']] = bigram['col'].apply(pd.Series)
    df = pd.merge(bigram, unigram, how='inner', left_on='x', right_index=True)
    df = pd.merge(df, unigram, how='inner', left_on='y', right_index=True)
    df['p(x)'] = df['freq_x'] / unigram['freq'].sum()
    df['p(y)'] = df['freq_y'] / unigram['freq'].sum()
    df['p(y|x)'] = df['freq_xy'] / df['freq_x']
    df['pmi(x,y)'] = np.log2(df['p(y|x)'] / df['p(y)'])  # I(x,y)=log p(x|y)/p(x) = log p(y|x)/p(y)
    outFile_dir, infile_name = os.path.split(corpus_dir)
    outFile_path = os.path.join(outFile_dir,'bi_pmi.csv')
    df.to_csv(outFile_path, encoding='utf_8_sig')
'''
d = r"D:\\data\\giga\\xin\\plk"
build_pmi_matrix_from_bigram(d)

'''
d = r"D:\\data\\giga\\xin\\plk-test"
ss = list(corpus(d))
ns = ngrams_2(ss,2)
d = ngrams_dic(ns)
bi_d = d[1]
df = DataFrame(Series(bi_d))
df['col'] = df.index
new = df['col'].str.split(r'_', 2, True)
new_df = pd.merge(new, df, right_index=True, left_index= True)
new_df.to_csv(r"D:\\data\\giga\\xin\\test5.csv")



'''


d = ngrams_dic(ns)
bi_d = d[1]
df = DataFrame(Series(bi_d))
df['col'] = df.index
new = df['col'].str.split(r'_', 2, True)
new_df = pd.merge(new, df, right_index=True, left_index= True)
new_df.to_csv(r"D:\\data\\giga\\xin\\test5.csv")


uni_d = {}
bi_d = {}
tri_d = {}

for k,v in d.items():
    if len(k) == 1:
        uni_d[k] = d[k]
    elif len(k) == 2:
        bi_d[k] = d[k]

unigram = DataFrame(Series(uni_d), columns=['freq'])
bigram = DataFrame(Series(bi_d), columns=['freq_xy'])
bigram['col'] = bigram.index
bigram['col_len'] = bigram['col'].apply(len)
bigram[['x','y']] = bigram['col'].apply(pd.Series)
df = pd.merge(bigram,unigram,how='inner',left_on='x',right_index=True)
df = pd.merge(df,unigram,how='inner',left_on='y',right_index=True)
df['p(x)'] = df['freq_x']/unigram['freq'].sum()
df['p(y)'] = df['freq_y']/unigram['freq'].sum()
df['entropy_x'] = -1*df['p(x)']*np.log2(df['p(x)'])
df['entropy_y'] = -1*df['p(y)']*np.log2(df['p(y)'])
df['p(x|y)'] = df['freq_xy']/df['freq_x']
df['pmi(x,y)'] = np.log2(df['p(x|y)']/df['p(x)'])#I(x,y)=log p(x|y)/p(x)
df.to_csv(r"D:\\data\\giga\\xin\\test3.csv",encoding='utf_8_sig')

'''



'''
d = ngrams_dics(ns)
df = DataFrame(Series(d),columns=['freq'])
df['col'] = df.index
df['col_len'] = df['col'].apply(len)
unigram = df[df['col_len'] == 1]
bigram = df[df['col_len'] == 2]
trigram = df[df['col_len'] == 3]
print(bigram)


unigram = DataFrame(Series(dics[0]), columns=['freq'])
bigram = DataFrame(Series(dics[1]), columns=['freq_xy'])
bigram['col'] = bigram.index
bigram['col_len'] = bigram['col'].apply(len)
bigram[['x','y']] = bigram['col'].apply(pd.Series)
df = pd.merge(bigram,unigram,how='inner',left_on='x',right_index=True)
df = pd.merge(df,unigram,how='inner',left_on='y',right_index=True)
df['p(x)'] = df['freq_x']/unigram['freq'].sum()
df['p(y)'] = df['freq_y']/unigram['freq'].sum()
df['entropy_x'] = -1*df['p(x)']*np.log2(df['p(x)'])
df['entropy_y'] = -1*df['p(y)']*np.log2(df['p(y)'])
df['p(x|y)'] = df['freq_xy']/df['freq_y']
print(df)


'''













'''
r"D:\\data\\giga\\xin\\ngrams_result.txt"
'''






























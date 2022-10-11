#coding:utf8
import re
'''
raw_sentence = '整(Neqa) 個(Nf) 中醫(Na) 理論(Na) 體系(Na) ！(EXCLANATIONCATEGORY) 如上(VH) 所(D) 簡述(VE) ，(COMMACATEGORY) 脈絡(Na) 分明(VH) ，(COMMACATEGORY) 系統(Na) 有(V_2) 序(Na) 。(PERIODCATEGORY)'
ss = re.split(r'(？\(QUESTIONCATEGORY\)|。\(PERIODCATEGORY\)|！\(EXCLANATIONCATEGORY\))',raw_sentence)
new_ss = [s.strip() for s in ss]
deli = new_ss[1::2]
ss = new_ss[0::2]
l = [s for s in zip(ss,deli)]
for item in l:
    s = ' '.join(item)
    print(s)

'''




def para2sentences(para):
    clean_para = para
    raw_sentences = re.split(r'(？\(QUESTIONCATEGORY\)|。\(PERIODCATEGORY\)|！\(EXCLANATIONCATEGORY\))',clean_para)
    clean_sentences = [s.strip() for s in raw_sentences if s != None]
    deli = clean_sentences[1::2]
    ss = clean_sentences[0::2]
    sentence_list = [s for s in zip(ss,deli)]
    sentences = []
    for s in sentence_list:
        new_s = ' '.join(s)
        sentences.append(new_s)
    return sentences

raw_sentence = '整(Neqa) 個(Nf) 中醫(Na) 理論(Na) 體系(Na) ！(EXCLANATIONCATEGORY) 如上(VH) 所(D) 簡述(VE) ，(COMMACATEGORY) 脈絡(Na) 分明(VH) ，(COMMACATEGORY) 系統(Na) 有(V_2) 序(Na) 。(PERIODCATEGORY)'
sentences = para2sentences(raw_sentence)
for s in sentences:
    print(s)




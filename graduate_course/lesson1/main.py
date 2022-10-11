#coding:utf8
import re
raw_string = '李(Nb) 院長(Na) 於(P) 二月(Nd) 二十六日(Nd) 至(P) 三月(Nd) 十五日(Nd) 赴(VCL) 美(Nc) 訪問(VC) ，(COMMACATEGORY) 期間(Na) 將(D) 與(P) 在(P) 美(Nc) 院士(Na) 商討(VE) 院務(Na) ，(COMMACATEGORY) 與(P) 美國(Nc) 大學(Nc) 聯繫(VC) 商討(VE) 長期(Nd) 合作(VH) 事宜(Na) ，(COMMACATEGORY) 並(Cbb) 辦理(VC) 加州(Nc) 大學(Nc) 退休(VH) 等(Cab) 手續(Na) 。(PERIODCATEGORY) 出國(Nv) 期間(Na) 院務(Na) 由(P) 羅(Nb) 副院長(Na) 代行(VC) 。(PERIODCATEGORY)'
sentence = raw_string.split(r' ')
sentence_lenth = len(sentence)

noun_words = []
for word in sentence:
    noun_mark = re.compile('N')
    if noun_mark.search(word):
        noun_words.append(word)
words_dict = {}
pos_dic = {}
for word_pos_pair in sentence:
    word, pos = word_pos_pair.split(r'(')
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
    if pos in pos_dic:
        pos_dic[pos] += 1
    else:
        pos_dic[pos] = 1
print(words_dict)
print(pos_dic)

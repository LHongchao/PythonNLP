import re
from pandas import Series,DataFrame
from collections import Counter
raw_sentence = '整(Neqa) 個(Nf) 中醫(Na) 理論(Na) 體系(Na) ！(EXCLANATIONCATEGORY) 如上(VH) 所(D) 簡述(VE) ，(COMMACATEGORY) 脈絡(Na) 分明(VH) ，(COMMACATEGORY) 系統(Na) 有(V_2) 序(Na) 。(PERIODCATEGORY)'



def para2sentences(para):
    sentences_with_marks = re.split(r'(。\(PERIODCATEGORY\)|！\(EXCLANATIONCATEGORY\))',para)
    sentences = [''.join(sentence).strip() for sentence in zip(sentences_with_marks[0::2],sentences_with_marks[1::2])]
    new_sentences = [s for s in sentences if s != None]
    return new_sentences

ss = para2sentences(raw_sentence)
for s in ss:
    print(s)

'''
raw_sentence = '本(Nes) 院(Nc) 附設(Nv) 幼稚園(Nc) 訂(VC) 四月(Nd) 一日(Nd) 至(Caa) 十五日(Nd) ，(COMMACATEGORY) 辦理(VC) 八十三學年(Nd) 小班(Nc) 幼生(Na) 新生(Na) 招收(Nv) 事宜(Na) ，(COMMACATEGORY) 有關(VJ) 事項(Na) 如(VG) 下(Ncd) ：(COLONCATEGORY) 本(Nes) 學年(Na) 招(VC) 小班(Nc) 新生(Na) 三十(Neu) 名(Nf) ，(COMMACATEGORY) 限(VJ) 民國(Nd) 八十年(Nd) 九月(Nd) 一日(Nd) 以前(Ng) 出生(VA) 滿(VJ) 三(Neu) 足歲(Nf) 之(DE) 本(Nes) 院(Nc) 員工(Na) 子女(Na) 、(PAUSECATEGORY) 孫子女(Na) 、(PAUSECATEGORY) 外孫(Na) 子女(Na) 報名(VA) 。(PERIODCATEGORY) 請(VF) 親(D) 持(VC) 戶口名簿(Na) 於(P) 四月(Nd) 一日(Nd) 至(Caa) 十五日(Nd) 每(Nes) 日(Nf) 上午(Nd) 九時(Nd) 至(Caa) 十二時(Nd) 至(P) 幼稚園(Nc) 辦理(VC) 登記(VC) 並(Cbb) 繳交(VC) 報名費(Na) 五百(Neu) 元(Nf) 。(PERIODCATEGORY) 報名(Nv) 人數(Na) 逾(VJ) 三十(Neu) 名(Nf) 時(Ng) 於(P) 四月(Nd) 十八日(Nd) 上午(Nd) 十時(Nd) 整(Neqb) 依(P) 董事會(Na) 園生(Na) 入學(Nv) 辦法(Na) 辦理(VC) 抽籤(VA) 。(PERIODCATEGORY) 幼稚園(Nc) 另(Nes) 設(VC) 暑期班(Nc) ，(COMMACATEGORY) 於(P) 八十三年(Nd) 七月(Nd) 一日(Nd) 開始(VL) 受理(VC) 新生(Na) 入學(VA) 。(PERIODCATEGORY) 如(Cbb) 有(V_2) 疑問(Na) ，(COMMACATEGORY) 請(VF) 電洽(VC) 園長(Na) 范瓊方(Nb) （(PARENTHESISCATEGORY) ＴＥＬ(Na,+fw) ：(COLONCATEGORY) ７８３—５３２５(Neu) ）(PARENTHESISCATEGORY) 。(PERIODCATEGORY)'
split_s = re.split(r'(\!|\.|\?|！|？|。\([a-zA-Z]+\))',raw_sentence)
for s in split_s[1::2]:
    print(s)

'''

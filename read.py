#!/bin/python

import sys
from collections import OrderedDict
import tensorflow as tf
import numpy as np

def w2v_to_idx(wordlist, veclist):
    idx_dic=OrderedDict()
    i = len(idx_dic)+1
    for word, vec in zip(wordlist, veclist):
        if word not in idx_dic:
            idx_dic[word]=i
            i+=1

    return (idx_dic, i)
        
def id_and_vec(idx_dic, wordlist, veclist):
    vec_dic = OrderedDict()
    for word, vec in zip(wordlist, veclist):
        if word in idx_dic:
            vec_dic[idx_dic[word]]=vec

    return vec_dic

a = sys.argv[1]

f = open(a,"r")
word=[]
vec=[]
word_vec = f.read().split("\n")
#print(word_vec)
for line in word_vec:
    sp=line.split(" ")
    word.append(sp[0])
    vec.append(",".join(sp[1:]))

idx_dic,i = w2v_to_idx(word, vec)
vec_dic = id_and_vec(idx_dic, word, vec)


embedding_matrix = np.zeros((i, 200))
for w in word:
    if w in idx_dic:
        embedding_matrix[i] = vec_dic[idx_dic[w]]



#for line in word_vec:
#    print(line[0])
#    print(line[1])

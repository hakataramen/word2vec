#!/bin/python

import sys
from gensim.models import word2vec

txt = sys.argv[1]

# 学習
sentences = word2vec.Text8Corpus(txt)
model = word2vec.Word2Vec(sentences, size=100)
# モデルの保存と読込
model.save("sample.model")
model = word2vec.Word2Vec.load("sample.model")
# 単語間の類似度計算
model.similarity(word1, word2)
# 意味の足し引き
model.most_similar(positive=[word11, word12, ...], negative=[word21, word22, ...])

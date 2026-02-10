# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 4:20 下午
# @Author  : Lee_zix
# @Email   : Lee_zix@163.com
# @File    : ent2word.py.py
# @Software: PyCharm

import os

def load_index(input_path):
    index, rev_index = {}, {}
    with open(input_path) as f:
        for i, line in enumerate(f.readlines()):        # relaions.dict和entities.dict中的id都是按顺序排列的
            rel, id = line.strip().split("\t")
            index[rel] = id
            rev_index[id] = rel
    return index, rev_index

entity2id, id2entity = load_index(os.path.join('entity2id.txt'))
relation2id, id2relation = load_index(os.path.join('relation2id.txt'))

count = 0
count1 = 0
word_list = set()
for entity_str in entity2id.keys():
    word_list.add(entity_str)

num_word = len(word_list)

word2id = {word: id for id, word in enumerate(word_list)}
id2word = {id: word for id, word in enumerate(word_list)}
# print(word2id)
# print(id2word)

print(len(word2id.keys()))
print(float(count)/(len(entity2id.keys()) + 1e-12))
print(float(count1)/(float(count)+1e-12))

with open("word2id.txt", "w") as f:
    for word in word2id.keys():
        f.write(word + "\t" + str(word2id[word])+'\n')

eid2wid = []
for id in range(len(id2entity.keys())):
    entity_str = id2entity[str(id)]
    eid2wid.append([str(entity2id[entity_str]), "0", str(word2id[entity_str])])

with open("e-w-graph.txt", "w") as f:
    for line in eid2wid:
        f.write("\t".join(line)+'\n')





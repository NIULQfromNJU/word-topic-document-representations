#!/usr/bin/python
#_*_ coding: utf-8 _*_

#niuliqiang
#2014-12-30
#calculate similarity

import sys
import os
import re
import struct
import math

wordsim353_file = 'ws353.txt'
vectors_file = 'skip-topic-lexeme-vectors.bin'

##
word_pair = []
human_score = []
human_order = []
sim_score = []
sim_order = []
vectors = {}

##
def read_word_pair():
    in_fp = open(wordsim353_file)
    line = ''
    line_num = 0
    line = in_fp.readline()
    while 1:
        line = in_fp.readline()
        line_num += 1
        if line:
            line = line.strip()
            line = line.lower()
            line_values = line.split('\t')
            words = []
            words.append(line_values[0])
            words.append(line_values[1])
            word_pair.append(words)
            human_score.append(float(line_values[2]))
        else:
            print 'end line!'
            break
    ##
    #print 'line_num: ', line_num, word_pair[0], human_score[0]
def  read_vectors():
    ##
    print 'vectors file: ', vectors_file
    vfp = open(vectors_file)
    line = ''
    word_num = 0
    dim = 0
    #line = vfp.readline()
    #line_values = line.split(' ')
    #word_num = line_values[0]
    #dim = line_values[1]
    ###
    while 1:
        line = vfp.readline()
        if line:
            line = line.strip()
            line_values = line.split(' ')
            word = line_values[0]
            #print 'word: ', word
            dim = len(line_values) - 1
            vectors[word] = line_values[1:dim]
        else:
            print 'end line!'
            break
    print 'word num: ', len(vectors)
    #print vectors['more']
    
def calculate_spearman():
    print 'calculate spearman'
    ##
    for item in word_pair:
        word1 = item[0]
        word2 = item[1]
        ###
        if vectors.has_key(word1) and vectors.has_key(word2):
            cosine = 0.0
            vector1 = vectors[word1]
            vector2 = vectors[word2]
            v1 = 0
            for index in range(len(vector1)):
                v1 += float(vector1[index]) * float(vector1[index])
            v2 = 0
            for index in range(len(vector2)):
                v2 += float(vector2[index]) * float(vector2[index])
            v3 = 0
            for index in range(len(vector1)):
                v3 += float(vector1[index]) * float(vector2[index])
            cosine = v3/(math.sqrt(v1)*math.sqrt(v2))
            sim_score.append(cosine)
        else:
            sim_score.append(0.5)
    ###
    #print 'sim score: ',  sim_score
    #print 'len sim_score: ', len(sim_score)
    ###
    print 'sort human score...'
    for i in range(len(human_score)):
        human_order.append(-1.0)
    lastmax = 11.0
    maxindex = []
    order = 1.0
    for i in range(len(human_score)):
        max = 0
        for j in range(len(human_score)):
            if human_score[j] < lastmax and human_score[j] > max:
                max = human_score[j]
        for k in range(len(human_score)):
            if human_score[k] == max:
                maxindex.append(k)
        lastmax = max
        ##
        currentorder = 0.0
        length = len(maxindex)
        if length == 0:
            break
        for l in range(length):
            currentorder += order
            order += 1
        currentorder = currentorder/length
        #print currentorder
        for l in range(length):
            human_order[maxindex[l]] = currentorder
        del maxindex[:]
    ###
    #print 'human order: ', human_order
    ###
    print 'sim score...'
    for i in range(len(sim_score)):
        sim_order.append(-1.0)
    lastmax1 = 2.0
    maxindex1 = []
    order1 = 1.0
    for i in range(len(sim_score)):
        max = -2.0
        for j in range(len(sim_score)):
            if sim_score[j] < lastmax1 and sim_score[j] > max:
                max = sim_score[j]
        for k in range(len(sim_score)):
            if sim_score[k] == max:
                maxindex1.append(k)
        lastmax1 = max
        ##
        currentorder1 = 0.0
        length1 = len(maxindex1)
        if length1 == 0:
            break
        for l in range(length1):
            currentorder1 += order1
            order1 += 1
        #print currentorder1
        currentorder1 = currentorder1/length1
        #print currentorder1
        for l in range(length1):
            sim_order[maxindex1[l]] = currentorder1
        del maxindex1[:]
    ###
    #print 'sim order: ', sim_order
    ###
    print 'calculate spearman...'
    spearman = 0.0
    if len(sim_order) != len(human_order):
        exit(1)
    length = len(sim_order)
    value = 0.0
    for i in range(length):
        value += (sim_order[i] - human_order[i]) * (sim_order[i] - human_order[i])
    value *= 6
    value /= (length * (length * length - 1))
    spearman = 1 - value
    print 'spearman: ',  spearman
    ###
if __name__ == '__main__':
    for arg in sys.argv:
        print arg
    vectors_file = sys.argv[1]
    ##
    read_word_pair()
    read_vectors()
    calculate_spearman()

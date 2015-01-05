#!/usr/bin/python
#_*_ coding: utf-8 _*_

#niuliqiang
#2014-12-19
#data preprocessing

import sys
import os
import re
from nltk import WordNetLemmatizer
from nltk import pos_tag as pt
from nltk.corpus import wordnet as wn

word_map_file = 'wordmap.txt'

id_word_dict = {}
word_id_dict = {}
word_num = 0

word_lexeme_id_dict = {}
##
word_topic_file = 'model-00200.tassign'
word_topic_lexeme_file = 'word-topic-lexeme.tassign'
max_line_num = 1000000
##

def read_wordmap():
    wm_fp = open(word_map_file)
    line = ''
    line_num = 0
    line = wm_fp.readline()
    word_num = int(line)
    print 'word num: ', word_num
    while 1:
        line = wm_fp.readline()
        if line:
            line = line.strip()
            line_words = line.split(' ')
            word = line_words[0]
            id = line_words[1]
            word_id_dict[word] = id
            id_word_dict[id] = word
        else:
            print 'end line!'
            break
    ##
    print 'dic size: ', len(word_id_dict)
    
###
def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']

def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

def is_adverb(tag):
    return tag in['RB', 'RBR', 'RBS']
    
def is_adjective(tag):
    return tag in['JJ', 'JJR', 'JJS']

def penn_to_wn(tag):
    if is_noun(tag):
        return wn.NOUN
    elif is_adjective(tag):
        return wn.ADJ
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return wn.NOUN
###
def add_lemmatizer():
    in_fp = open(word_topic_file)
    out_fp = open(word_topic_lexeme_file,  'w')
    wnl = WordNetLemmatizer()
    ###
    line = ''
    line_num = 0
    while 1 and line_num < max_line_num:
        line = in_fp.readline()
        line = line.strip()
        line_words = line.split(' ')
        line_write = ''
        for words in line_words:
            word_topic = words.split(':')
            word_id = word_topic[0]
            topic_id = word_topic[1]
            line_write += word_id
            line_write += ':'
            line_write += topic_id
            line_write += ':'
            ##
            if id_word_dict.has_key(word_id):
                word = id_word_dict[word_id]
                if word_lexeme_id_dict.has_key(word):
                    line_write += word_lexeme_id_dict[word]
                    line_write += ' '
                else:
                    word_list = []
                    word_list.append(word)
                    pos = pt(word_list)
                    tag = pos[0][1]
                    lexeme = wnl.lemmatize(word,  penn_to_wn(tag))
                    #print ': ', word,  lexeme
                    if word_id_dict.has_key(lexeme):
                        lexeme_id = word_id_dict[lexeme]
                        word_lexeme_id_dict[word] = lexeme_id
                        line_write += lexeme_id
                        line_write += ' '
                    else:
                        word_lexeme_id_dict[word] = word_id
                        line_write += word_id
                        line_write += ' '
                
            ##
        line_write = line_write.strip()
        out_fp.write(line_write)
        if line_num < max_line_num -1:
            out_fp.write('\n')
        line_num += 1
        if line_num%1000 ==0:
            print 'line: ', line_num
    ###
    in_fp.close()
    out_fp.close()
###
###
if __name__ == '__main__':
    read_wordmap()
    add_lemmatizer()
    
    

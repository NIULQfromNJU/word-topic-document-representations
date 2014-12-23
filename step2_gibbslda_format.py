#!/usr/bin/python
#_*_ coding: utf-8 _*_

#niuliqiang
#2014-11-24
#turn data to plda format

import sys
import os
import re

#original file
original_file = 'ltw_100k.txt'
#minimum count
min_count = 5
#dictionary
dict_word_count = {}
#
max_line_num = 100000
#
stop_words = {}
#

gibbs_lda_format_file = 'ltw_glda_format_100k.txt'


########
def turn_gibbs_lda_format():
    #------------------------------------------------#
    print 'read stop words'
    sw = open('stop_words.txt')
    sw_line = sw.readline()
    if sw_line:
        sw_line_words = sw_line.split(',')
        for word in sw_line_words:
            stop_words[word] = 1
        #
    print 'stop words num: ',len(stop_words)
    sw.close()
    #------------------------------------------------#
    fp = open(original_file)
    line_num = 0
    while 1:
        line = fp.readline()
        if line and line_num < max_line_num:
            #
            line = line.strip()
            line_words = line.split(' ')
            #print line_words
            for word in line_words:
                flag = True
                for c in word:
                    if c < 'a' or c > 'z':
                        flag = False
                        #print 'illegal: ',word
                        break
                if len(word) > 1 and flag and stop_words.has_key(word)== False:
                    if dict_word_count.has_key(word):
                        count = dict_word_count[word]
                        dict_word_count[word] = count+1
                    else:
                        dict_word_count[word] = 1
                #
            #
        else:
            #
            print 'end line'
            break
            #
        line_num += 1
    ###end while
    print 'line_num : ',line_num
    ###
    print 'dict_word_count length : ',len(dict_word_count)
    #print dict_word_count.items()
    ###dict sort
    print 'dict_word_count filter - min_count : ',min_count
    for word in dict_word_count.keys():
        if dict_word_count[word] < min_count:
            del dict_word_count[word]
        #
    #
    print 'dict_word_count length : ',len(dict_word_count)
    #
    fp.close()
    #------------------------------------------------#
    #------------------------------------------------#
    fp1 = open(original_file)
    gibbs_lda_format_fp = open(gibbs_lda_format_file, 'w')
    #
    gibbs_lda_format_fp.write(str(line_num)+'\n')
    #
    line_num1 = 0
    while 1:
        line1 = fp1.readline()
        if line1 and line_num1 < max_line_num:
            #
            line1 = line1.strip()
            line_words1 = line1.split(' ')
            #
            #print line_words1
            gibbs_lda_format_line = ''
            for word1 in line_words1:
                if dict_word_count.has_key(word1):
                    gibbs_lda_format_line += word1
                    gibbs_lda_format_line += ' '
                #
            #
            #print 'line_dict length : ',len(line_dict)
            #
            gibbs_lda_format_line = gibbs_lda_format_line.strip()
            gibbs_lda_format_fp.write(gibbs_lda_format_line)
            if line_num1 < line_num-1:
                gibbs_lda_format_fp.write('\n')
            #
        else:
            #
            print 'end line'
            break
            #
        line_num1 += 1
    ###end while
    fp1.close()
    gibbs_lda_format_fp.close()
    print 'turn to gibbs lda format data'
    #------------------------------------------------#
    
    #------------------------------------------------#
#######
#
if __name__ == '__main__':
    turn_gibbs_lda_format()

#!/usr/bin/python
#_*_ coding: utf-8 _*_

#niuliqiang
#2014-11-23
#data preprocessing

import sys
import os
import re

#file list
input_path = 'ltw_eng'

all_files = list()

#output file
output_file = 'ltw_100k.txt'

all_text_num = 0
max_text_num = 100000

def preprocessing():
######
    all_files = os.listdir(input_path)
    outfp = open(output_file, 'w')
    ###
    for item in all_files:
        global all_text_num
        global max_text_num
        if all_text_num >= max_text_num:
            print 'satisfied!!!'
            break
        #print 'file name : ',item
        m = re.match('ltw_eng_2[0-9]{5}$',item)
        if(m is not None):
            item = m.group()
            print 'file real name : ',item
            #####
            fp = open(input_path+'/'+item)
            paragraph = ''
            start = False
            lines = 0
            while 1:
                line = fp.readline()
                if line:
                    #print line
                    # remove '\n'
                    line = line.replace(',',' ')
                    line = line.replace('.',' ')
                    line = line.replace('?',' ')
                    line = line.replace('"',' ')
                    line = line.replace('!',' ')
                    line = line.replace(':',' ')
                    line = line.replace(';',' ')
                    line = line.replace('(',' ')
                    line = line.replace(')',' ')
                    line = line.replace('{',' ')
                    line = line.replace('}',' ')
                    line = line.replace('[',' ')
                    line = line.replace(']',' ')
                    line = line.replace('``',' ')
                    line = line.replace('_',' ')
                    line = line.replace('--',' ')
                    line = line.replace('\'\'',' ')
		    line = line.replace('\'s',' ')
  		    line = line.replace('\'',' ')
		    line = line.replace('=',' ')
                    line = line.replace('-',' ')
                    #line = line.replace('','')
                    line = line.lower()
		    line = line.strip()
                    if start == False and line == '<p>':
                        start = True
                    elif start == True and line != '</p>':
                        paragraph += line
                        paragraph += ' '
                    elif start == True and line == '</p>':
                        start = False
                    elif start == False and line == '</text>':
                        if all_text_num < max_text_num:
                            if len(paragraph)>1000:
                                first_char = paragraph[0:1]
                                if first_char<='z' and first_char>='a' or first_char<='9' and first_char>='0':
                                    #write
                                    paragraph = paragraph.strip()
                                    outfp.write(paragraph+'\n')
                                    paragraph = ''
                                    #
                                    all_text_num += 1
                                    #print 'all text num : ',all_text_num
                                else:
                                    paragraph = ''
                            else:
                                paragraph = ''
                                #
                            #
                        else:
                            print 'all text num : ',all_text_num
                            break
                else:
                    print 'end line'
                    print 'all text num : ',all_text_num
                    break
                lines += 1
            #####
            fp.close()
    outfp.close()        
#######
#
if __name__ == '__main__':
    preprocessing()

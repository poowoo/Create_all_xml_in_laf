# -*- coding: utf8 -*-
import os
import pdb

def initial_ld(dictonary_fn):

    lexicon = dict()     
    diff = True

    l = open(dictonary_fn, mode = "r", encoding = 'utf-8')
    # for line in l.readlines():    
    for line in open(dictonary_fn, encoding = 'utf-8'):
        line = l.readline()
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        # name (0), hyphenation (1), en-US(2), en-US.aligned(3), PoS(4)
        line = line.split(',')        
        word_info = list()

        for i in range(len(line)):
            if(i == 0):
                continue
            if(len(line[i]) == 0):
                word_info.append("None")
            else:
                word_info.append(line[i].replace('-',''))# append from hyphenation


        if(line[0] in lexicon):

            word_info_tmp = lexicon[line[0]]

            for i in range(len(word_info_tmp)):
                # compare word info ,different then add 
                for t in word_info_tmp[i].split('|'):
                    if (word_info[i] ==  t):
                        diff = False
                if(diff == True and len(word_info[i]) != 0):                    
                    word_info_tmp[i] = word_info_tmp[i] + "|" + word_info[i]
                diff = True

        else:
            lexicon[line[0]] = word_info

    l.close()
    return lexicon
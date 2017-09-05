# -*- coding: utf8 -*-
import os
import pdb

def initial_ld(dictonary_fn):

    lexicon = dict() 
    diff = False
    l = open(dictonary_fn, mode = "r", encoding = 'utf-8')
    #for line in l.readlines():    
    for line in open(dictonary_fn, encoding = 'utf-8'):
        line = l.readline()
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        line = line.split(',')        
        tmp = list()
        for i in range(len(line)):
            if(i == 0):
                continue
            tmp.append(line[i])        

        if(line[0] in lexicon):
            tmp2 = lexicon[line[0]]

            for i in range(len(tmp2)):
                for t in tmp2[i].split('|'):
                    if (tmp[i] == t):
                        diff = False
                if(diff):
                    tmp2[i] = tmp2[i] + "|" + tmp[i]
                diff = True

        else:
            lexicon[line[0]] = tmp

    l.close()
    return lexicon
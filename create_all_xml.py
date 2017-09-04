# -*- coding: utf8 -*-
import sys
import os
import xml
import argparse

def Usage():
    print("Usage:")
    print("create_all_xml.py input_corpus_name output_name title_stateme sourceDesc langUsage textclass")        
    print("    title_stateme")
    print("    sourceDesc:  (use '-' to separate)")
    print("    sourceDesc corpus title:")
    print("    sourceDesc publisher:")
    print("    sourceDesc pubAddress:")
    print("    sourceDesc email:")
    print("    sourceDesc url:")
    print("    sourceDesc pubDate:")
    print("    langUsage language in iso639:")
    print("    langUsage language:")
    print("    textclass domain:")
    print("    textclass factuality:")
    print("    textclass preparedness:")
    print("    textclass purpose:")
    print("There is an example to show ,example.bat")
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Make corpus add  annotations.xml")    
    parser.add_argument("-l", "-lexicon_dictionary",  help="get word phone, dictonary format: abc   eʲ2.b-iː0.s-iː1")
    parser.add_argument("-c", "-corpus" , help="corpus file name")
    parser.add_argument("-o", "-output",  help="output file name,without extension, ex: 102CTL001")
    parser.add_argument("-a", "-annotations", help="annotations array, ex: \"s,Sentence-np,Noun chunks\"")
    parser.add_argument("-ts", "-title_statment", help="ex: 102CTL001", default="Unknow")
    parser.add_argument("-sd", "-source_description", help="ex: (title)ICIC Corpus of Philanthropic Fundraising Discourse-(publisher)ICIC-(pubAddress)620 Union Drive, Room 407, Indianapolis, Indiana 46202, U.S.A.-(email)icic@iupui.edu-(url)www.iupui.edu/~icic-(pubDate)2004",default="Unknow-Unknow-Unknow-Unknow-Unknow-Unknow")
    parser.add_argument("-lu", "-language_usage", help="ex: English-United States",default="Unknow-Unknow")
    parser.add_argument("-tc", "-text_class", help="ex: (domain type)philanthropic fundraising discourse-(factuality type)nonfiction-(preparedness type)prepared-(purpose type)fundraising",default="Unknow-Unknow-Unknow-Unknow")
    args = parser.parse_args()
        
    if args.c is None or args.a is None or args.o is None:
        parser.print_help()
        sys.exit(0)

    ann_types = args.a.split("-")
    word_count = xml.get_word_count(args.c)
    xml.write_xml_header(word_count,args.o,args.ts,args.sd,args.lu,args.tc,ann_types)
    
    #ann_types = list()
    xml.write_xml_anntations(args.c,args.o,ann_types,args.l)
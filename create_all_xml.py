# -*- coding: utf8 -*-
import sys
import os
import xml

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

    if len(sys.argv) != 7:
        Usage()
        sys.exit(0)
    word_count = xml.get_word_count(sys.argv[1])
    ann_types = xml.write_xml_header(word_count,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    #ann_types = list()
    xml.write_xml_anntations(sys.argv[1],sys.argv[2],ann_types)
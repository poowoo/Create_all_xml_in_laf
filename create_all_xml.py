# -*- coding: utf8 -*-
import sys
import os
import xml

def Usage():
    print("Usage:")
    print("create_all_xml.py input_corpus_name output_fn")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        Usage()
        sys.exit(0)
    #ann_types = xml.write_xml_header(sys.argv[2])
    ann_types = list()
    xml.write_xml_anntations(sys.argv[1],sys.argv[2],ann_types)
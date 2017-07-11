# -*- coding: utf8 -*-
import os

def write_header(fn):

	out = open(fn, mode='w', encoding='UTF-8')
	out.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
	out.close()

def write_ann_text_french(corpus_fn,out_fn):
    
    f = open(corpus_fn, "r",encoding="utf-8")                       
    w = open(out_fn + '.txt','w',encoding='utf-8')

    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        line = line.split(' ')
        for tok in line:
            w.write(tok.split('|')[0])
            if tok is not line[-1]:
            	w.write(" ")
        w.write('\n')

    f.close()
    w.close()

def write_ann_sentence(text_fn,ann):

    f = open(text_fn + ".txt",'r',encoding = 'utf-8')
    out_fn = 

def write_xml_anntations(corpus_fn,out_fn,ann_types):
    
    # change by the corpust data
    write_ann_text_french(corpus_fn,out_fn)

	ann_types = ["s,sentence"]
    for ann in ann_types:
        # change the code by different data
        if ann.split(',')[0] == "s":
            write_ann_sentence(out_fn,ann.split(',')[0])
        if ann.split(',')[0] == 'pos':
            print('b')
        if ann.split(',')[0] == "liason":
            print('c')
        

def write_xml_header(fn):
        
    title = input('set title: ')
    wordCount = input("set word count: ")
    source_title = input("set file description title: ")
    publisher = input("set file description publisher: ")
    pubAddress = input("set file description pubAddress: ")
    email = input("set file description email: ")
    url = input("set file description url: ")
    pubDate = input("set file description pubDate: ")

    iso639 = input("set language in iso639(shorthand): ")
    language = input("set language: ")

    domain = input("set textClass domain: ")
    factuality = input("set textClass factuality: ")
    preparedness = input("set textClass preparedness: ")
    purpose = input("set textClass purpose: ")

    ann_types = ["s,Sentence boundaries","pos,POS tags"]

    write_header(fn + ".xml")

    while(1):

    	ann_type = input("set annotation type,type -1 to leave\n")    	
    	
    	if ann_type == '-1':
    		break
    	else:
    		ann_types.append(ann_type)    	
    

    out = open(fn + ".xml", mode='a', encoding='UTF-8')
    out.write("<cesHeader>\n")
    out.write("    <fileDesc>\n")
    out.write("        <titleStmt>\n")    
    out.write("            <title>" + title + "</title>\n")
    out.write("        </titleStmt>\n")    
    out.write("        <extent wordCount=\"" + wordCount + "\"/>\n")
    out.write("        <sourceDesc>\n")
    out.write("            <title>" + source_title + "</title>\n")
    out.write("            <publisher>" + publisher + "</publisher>\n")
    out.write("            <pubAddress>" + pubAddress + "</pubAddress>\n")
    out.write("            <email>" + email + "</email>\n")
    out.write("            <url>" + url + "</url>\n")
    out.write("            <pubDate>" + pubDate + "</pubDate>\n")
    out.write("        </sourceDesc>\n")
    out.write("    </fileDesc>\n")
    out.write("    <profileDesc>\n")
    out.write("        <langUsage>\n")
    out.write("            <language iso639=\"" + iso639 + "\">" + language + "</language>\n")
    out.write("        </langUsage>\n")
    out.write("        <wsdUsage>\n")
    out.write("            <writingSystem id=\"UTF-8\">8-bit UCS/Unicode Transformation Format</writingSystem>\n")
    out.write("        </wsdUsage>\n")
    out.write("        <!-- catRef types DEFINED IN MAIN HEADER -->\n")
    out.write("        <textClass catRef=\"WR LT\">\n")
    out.write("            <domain type=\"" + domain + "\"/>\n")
    out.write("            <factuality type=\"" + factuality + "\"/>\n")
    out.write("            <preparedness type=\"" + preparedness + "\"/>\n")
    out.write("            <purpose type=\"" + purpose + "\"/>\n")
    out.write("        </textClass>\n")
    out.write("        <!-- MEDIUM DEFINED IN MAIN HEADER -->\n")
    out.write("        <primaryData loc=\"" + fn + ".txt\" medium=\"text\"/>\n")
    out.write("        <annotations>\n")    
    #out.write("             <annotation ann.loc=\"" + fn + "-s.xml\" type=\"s\">Sentence boundaries</annotation>\n")
    #out.write("             <annotation ann.loc=\"" + fn + "-pos.xml\" type=\"pos\">POS tags</annotation>\n")
    for ann in ann_types:
    	out.write("            <annotation ann.loc=\"" + fn + "-" + ann.split(',')[0] + ".xml\" type=\"" + ann.split(',')[0] + "\">" + ann.split(',')[1] + "</annotation>\n")
    out.write("             <annotation ann.loc=\"" + fn + ".txt\" type=\"content\">Document content</annotation>\n")
    out.write("          </annotations>\n")
    out.write("    </profileDesc>\n")
    out.write("</cesHeader>\n")
    out.close()
    return ann_types

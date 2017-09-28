# -*- coding: utf8 -*-
import os
import pdb
import language_dictonary

def write_header(fn):

	out = open(fn, mode='w', encoding='UTF-8')
	out.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
	out.close()

def get_word_count(corpus_fn):
    
    f = open(corpus_fn, mode =  "r", encoding = "utf-8")                       
    
    word_count = 0
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        line = line.split(' ')
        word_count += len(line);
    f.close()
    return word_count

#def write_ann_text_french(corpus_fn,out_fn):
#    
#    f = open(corpus_fn, mode =  "r", encoding = "utf-8")                       
#    w = open(out_fn + '.txt', mode = 'w', encoding = 'utf-8')
#
#    for line in f.readlines():
#        line = line.strip()
#        if not len(line) or line.startswith('#'):
#            continue
#        line = line.split(' ')
#        for tok in line:
#            word = tok.split('|')[0]            
#            #word = word.replace("\"","&quot;")# \" need to change to &quot;
#            w.write(word)
#            if tok is not line[-1]:
#                w.write(" ")
#        w.write('\n')
#    f.close()
#    w.close()

def write_ann_text(corpus_fn,out_fn):
    
    f = open(corpus_fn, mode =  "r", encoding = "utf-8")                       
    w = open(out_fn + '.txt', mode = 'w', encoding = 'utf-8')

    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        line = line.split(' ')
        for tok in line:
            w.write(tok)
            if tok is not line[-1]:
                w.write(" ")
        w.write('\n')
    f.close()
    w.close()

def write_xml_anntations(corpus_fn,out_fn,ann_types,lexicon_dict):
    
    # change by the corpust data
    # write_ann_text_french(corpus_fn,out_fn)
    write_ann_text(corpus_fn,out_fn)

    if(len(lexicon_dict) > 0):
        language_dict = language_dictonary.initial_ld(lexicon_dict)

    for ann in ann_types:
        # change the code by different data
        if ann.split(',')[0] == "s":
            write_ann_sentence(out_fn,ann.split(',')[0])
        if ann.split(',')[0] == "pron":            
            write_ann_pron(corpus_fn,out_fn,ann.split(',')[0],language_dict)
        if ann.split(',')[0] == "tok":
            write_ann_tok(corpus_fn,out_fn,ann.split(',')[0])
        if ann.split(',')[0] == "pos":
            write_ann_pos(corpus_fn,out_fn,ann.split(',')[0],language_dict)
        if ann.split(',')[0] == "liaison":
            write_ann_liason(corpus_fn,out_fn,ann.split(',')[0])        

def write_xml_header(word_count,fn,title_info,corpus_info,lan_info,text_info,ann_types):
        
    #title = input('set title: ')
    #wordCount = input("set word count: ")
    #source_title = input("set file description title: ")
    #publisher = input("set file description publisher: ")
    #pubAddress = input("set file description pubAddress: ")
    #email = input("set file description email: ")
    #url = input("set file description url: ")
    #pubDate = input("set file description pubDate: ")

    #iso639 = input("set language in iso639(shorthand): ")
    #language = input("set language: ")

    #domain = input("set textClass domain: ")
    #factuality = input("set textClass factuality: ")
    #preparedness = input("set textClass preparedness: ")
    #purpose = input("set textClass purpose: ")

    title = title_info
    wordCount = str(word_count)    
    source_title = corpus_info.split('-')[0]
    publisher = corpus_info.split('-')[1]
    pubAddress = corpus_info.split('-')[2]
    email = corpus_info.split('-')[3]
    url = corpus_info.split('-')[4]
    pubDate = corpus_info.split('-')[5]

    iso639 = lan_info.split('-')[0]
    language = lan_info.split('-')[1]

    domain = text_info.split('-')[0]
    factuality = text_info.split('-')[1]
    preparedness = text_info.split('-')[2]
    purpose = text_info.split('-')[3]

    #ann_types = ["s,Sentence boundaries","pos,POS tags","liaison,Liaison"]
    #ann_types = ["s,Sentence boundaries","phone,Phones tags"]

    write_header(fn + ".xml")

    #while(1):

    	#ann_type = input("set annotation type,type -1 to leave\n")    	
    	#
    	#if ann_type == '-1':
    	#	break
    	#else:
    	#	ann_types.append(ann_type)    	
    
    out = open(fn + ".xml", mode='a', encoding='UTF-8')
    out.write("<cesHeader>\n")
    out.write("  <fileDesc>\n")
    out.write("      <titleStmt>\n")    
    out.write("          <title>" + title + "</title>\n")
    out.write("      </titleStmt>\n")    
    out.write("      <extent wordCount=\"" + wordCount + "\"/>\n")
    out.write("      <sourceDesc>\n")
    out.write("          <title>" + source_title + "</title>\n")
    out.write("          <publisher>" + publisher + "</publisher>\n")
    out.write("          <pubAddress>" + pubAddress + "</pubAddress>\n")
    out.write("          <email>" + email + "</email>\n")
    out.write("          <url>" + url + "</url>\n")
    out.write("          <pubDate>" + pubDate + "</pubDate>\n")
    out.write("      </sourceDesc>\n")
    out.write("  </fileDesc>\n")
    out.write("  <profileDesc>\n")
    out.write("      <langUsage>\n")
    out.write("          <language iso639=\"" + iso639 + "\">" + language + "</language>\n")
    out.write("      </langUsage>\n")
    out.write("      <wsdUsage>\n")
    out.write("          <writingSystem id=\"UTF-8\">8-bit UCS/Unicode Transformation Format</writingSystem>\n")
    out.write("      </wsdUsage>\n")
    out.write("      <!-- catRef types DEFINED IN MAIN HEADER -->\n")
    out.write("      <textClass catRef=\"WR LT\">\n")
    out.write("          <domain type=\"" + domain + "\"/>\n")
    out.write("          <factuality type=\"" + factuality + "\"/>\n")
    out.write("          <preparedness type=\"" + preparedness + "\"/>\n")
    out.write("          <purpose type=\"" + purpose + "\"/>\n")
    out.write("      </textClass>\n")
    out.write("      <!-- MEDIUM DEFINED IN MAIN HEADER -->\n")
    out.write("      <primaryData loc=\"" + fn + ".txt\" medium=\"text\"/>\n")
    out.write("      <annotations>\n")            
    for ann in ann_types:
        out.write("          <annotation ann.loc=\"" + fn + "-" + ann.split(',')[0] + ".xml\" type=\"" + ann.split(',')[0] + "\">" + ann.split(',')[1] + "</annotation>\n")
    out.write("           <annotation ann.loc=\"" + fn + ".txt\" type=\"content\">Document content</annotation>\n")
    out.write("        </annotations>\n")
    out.write("  </profileDesc>\n")
    out.write("</cesHeader>\n")
    out.close()
    return ann_types

def corpus_fn_get_liason(corpus_fn):

    f = open(corpus_fn, mode = "r", encoding = 'utf-8')
    liason = list()  
    word = list()  
    for line in f.readlines():
            line = line.strip()
            if not len(line) or line.startswith('#'):
                continue
            line = line.split(' ')
            for tok in line:
                word.append(tok.split('|')[0].replace("\"","&quot;"))
                liason.append(tok.split('|')[2])
    f.close()
    return liason,word

def write_ann_liason(corpus_fn,text_fn,ann):

    liason,word = corpus_fn_get_liason(corpus_fn)

    id_index = 0
    out_fn = open(text_fn + "-" + ann + ".xml", mode = "w", encoding = 'utf-8')
    out_fn.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    out_fn.write("<graph>\n")
    out_fn.write("  <header>\n")
    out_fn.write("      <tagsDecl>\n")
    out_fn.write("          <tagUsage gi=\"" + ann + "\" occurs=\"" + str(int(len(liason))) + "\"/>\n")
    out_fn.write("      </tagsDecl>\n")
    out_fn.write("      <dependencies>\n")
    out_fn.write("          <dependsOn type=\"" + "pos" + "\"/>\n")
    out_fn.write("      </dependencies>\n")
    out_fn.write("      <annotationSets>\n")
    out_fn.write("          <annotationSet name=\"xces\" type=\"http://www.xces.org/schema/2003\"/>\n")
    out_fn.write("      </annotationSets>\n")
    out_fn.write("  </header>\n")
    while(1):        
        out_fn.write("  <node xml:id=\"" + ann + "-n" + str(id_index) +"\"/>\n")        
        out_fn.write("  <a label=\"" + ann + "\" ref=\"" + ann + "-n" + str(id_index) + "\" to=\"penn-n" + str(id_index) + "\" as=\"xces\">\n")
        out_fn.write("      <fs>\n")        
        #out_fn.write("          <f name=\"base\" value=\"" + word[id_index] + "\"/>\n")
        out_fn.write("          <f name=\"lia\" value=\"" + liason[id_index] + "\"/>\n")
        #out_fn.write("          <f name=\"lt\" value=\"" + liason[id_index] + "\"/>\n")
        #out_fn.write("          <f name=\"rt\" value=\"" + liason[id_index] + "\"/>\n")
        out_fn.write("      </fs>\n")
        out_fn.write("  </a>\n")
        id_index += 1
        if id_index == len(liason):
            break;
    id_index = 0
    while(1):        
        out_fn.write("  <edge xml:id=\"lnk" + str(id_index) + "\" from=\"" + ann + "-n" + str(id_index) + "\" to=\"penn-n" + str(id_index) + "\"/>\n")
        id_index += 1
        if id_index == len(liason):
            break;
    out_fn.write("</graph>\n")    
    out_fn.close()

def corpus_get_word_pron(text_fn,language_dict):

        
    pron = list()
    word = list()    

    f = open(text_fn + ".txt", mode = "r", encoding = 'utf-8')
    for line in f.readlines():
            line = line.strip()
            if not len(line) or line.startswith('#'):
                continue
            line = line.split(' ')
            for tok in line:
                word.append(tok.replace("\"","&quot;"))
                tok = "".join(c for c in tok if c not in ('!',',','.',':','\"')) 
                if(tok.lower() in language_dict):
                    pron.append(language_dict[tok.lower()][1])
                else:
                    pron.append("None")

    f.close()
    return pron,word

def write_ann_pron(corpus_fn,text_fn,ann,liexcon_dict):
    
    token_region = text_get_token_region(text_fn)
    pron,word = corpus_get_word_pron(text_fn,liexcon_dict)

    id_index = 0    
    out_fn = open(text_fn + "-" + ann + ".xml", mode = "w", encoding = 'utf-8')
    out_fn.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    out_fn.write("<graph>\n")
    out_fn.write("  <header>\n")
    out_fn.write("      <tagsDecl>\n")
    out_fn.write("          <tagUsage gi=\"" + ann + "\" occurs=\"" + str(int(len(pron))) + "\"/>\n")
    out_fn.write("      </tagsDecl>\n")
    out_fn.write("      <annotationSets>\n")
    out_fn.write("          <annotationSet name=\"xces\" type=\"http://www.xces.org/schema/2003\"/>\n")
    out_fn.write("      </annotationSets>\n")
    out_fn.write("  </header>\n")
    while(1):
        out_fn.write("  <region xml:id=\"pron-r" + str(id_index) + "\" anchors=\"" + str(token_region[id_index * 2]) +" "+ str(token_region[id_index * 2 + 1]) + "\"/>\n")
        out_fn.write("  <node xml:id=\"pron-n" + str(id_index) +"\">\n")
        out_fn.write("      <link targets=\"pron-r" + str(id_index) + "\"/>\n")
        out_fn.write("  </node>\n")
        out_fn.write("  <a label=\"" + ann + "\" ref=\"pron-n" + str(id_index) +"\" as=\"xces\">\n")
        out_fn.write("      <fs>\n")
        out_fn.write("          <f name=\"base\" value=\"" + word[id_index] + "\"/>\n")
        out_fn.write("          <f name=\"" + ann + "\" value=\"" + pron[id_index].split('|')[0] + "\"/>\n")
        out_fn.write("          <f name=\"" + ann + "s\" value=\"" + pron[id_index] + "\"/>\n")
        out_fn.write("      </fs>\n")
        out_fn.write("  </a>\n")
        id_index += 1
        if id_index == len(pron):
            break;
    out_fn.write("</graph>\n")    
    out_fn.close()

def text_get_token_region(text_fn):

    f = open(text_fn + ".txt", mode = "r", encoding = 'utf-8')
    region = list()
    pre_token_index = 0
    
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        line = line.split(' ')
        for tok in line:
            region.append(pre_token_index)
            region.append(pre_token_index + len(tok))
            pre_token_index += len(tok) + 1
        pre_token_index += 1 #window format
    f.close()
    return region

def corpus_get_pos_word(corpus_fn,language_dict):
    
    pos = list()
    word = list()
    f = open(corpus_fn, mode = "r", encoding = 'utf-8')
    for line in f.readlines():
            line = line.strip()
            if not len(line) or line.startswith('#'):
                continue
            line = line.split(' ')
            for tok in line:            	
                word.append(tok.replace("\"","&quot;"))
                tok = "".join(c for c in tok if c not in ('!',',','.',':','\"')) 
                if(tok.lower() in language_dict):
                    pos.append(language_dict[tok.lower()][3])
                    # hyphenation (0), en-US(1), en-US.aligned(2), PoS(3)
                else:
                    pos.append("None")
                # Umy French format
                #word.append(tok.split('|')[0].replace("\"","&quot;"))
                #pos.append(tok.split('|')[1].replace("\"","&quot;"))                
    f.close()
    return pos,word

def write_ann_pos(corpus_fn,text_fn,ann,liexcon_dict):

    # change in another data format
    pos_region = text_get_token_region(text_fn)
    pos,word = corpus_get_pos_word(corpus_fn,liexcon_dict)
    
    id_index = 0
    out_fn = open(text_fn + "-" + ann + ".xml", mode = "w", encoding = 'utf-8')
    out_fn.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    out_fn.write("<graph>\n")
    out_fn.write("  <header>\n")
    out_fn.write("      <tagsDecl>\n")
    out_fn.write("          <tagUsage gi=\"" + ann + "\" occurs=\"" + str(int(len(pos))) + "\"/>\n")
    out_fn.write("      </tagsDecl>\n")
    out_fn.write("      <annotationSets>\n")
    out_fn.write("          <annotationSet name=\"xces\" type=\"http://www.xces.org/schema/2003\"/>\n")
    out_fn.write("      </annotationSets>\n")
    out_fn.write("  </header>\n")
    while(1):
        out_fn.write("  <region xml:id=\"penn-r" + str(id_index) + "\" anchors=\"" + str(pos_region[id_index * 2]) +" "+ str(pos_region[id_index * 2 + 1]) + "\"/>\n")
        out_fn.write("  <node xml:id=\"penn-n" + str(id_index) +"\">\n")
        out_fn.write("      <link targets=\"penn-r" + str(id_index) + "\"/>\n")
        out_fn.write("  </node>\n")
        out_fn.write("  <a label=\"" + ann + "\" ref=\"penn-n" + str(id_index) +"\" as=\"xces\">\n")
        out_fn.write("      <fs>\n")
        out_fn.write("          <f name=\"base\" value=\"" + word[id_index] + "\"/>\n")
        out_fn.write("          <f name=\"msd\" value=\"" + pos[id_index].split('|')[0] + "\"/>\n")
        out_fn.write("      </fs>\n")
        out_fn.write("  </a>\n")
        id_index += 1
        if id_index == len(pos):
            break;
    out_fn.write("</graph>\n")    
    out_fn.close()

def corpus_get_word(corpus_fn):
    
    word = list()    

    f = open(corpus_fn, mode = "r", encoding = 'utf-8')
    for line in f.readlines():
            line = line.strip()
            if not len(line) or line.startswith('#'):
                continue
            line = line.split(' ')
            for tok in line:
                word.append(tok.replace("\"","&quot;"))                
    f.close()
    return word

def write_ann_tok(corpus_fn,text_fn,ann):

    # change in another data format
    tok_region = text_get_token_region(text_fn)
    tok = corpus_get_word(corpus_fn)
    
    id_index = 0
    out_fn = open(text_fn + "-" + ann + ".xml", mode = "w", encoding = 'utf-8')
    out_fn.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    out_fn.write("<graph>\n")
    out_fn.write("  <header>\n")
    out_fn.write("      <tagsDecl>\n")
    out_fn.write("          <tagUsage gi=\"" + ann + "\" occurs=\"" + str(int(len(tok))) + "\"/>\n")
    out_fn.write("      </tagsDecl>\n")
    out_fn.write("      <annotationSets>\n")
    out_fn.write("          <annotationSet name=\"xces\" type=\"http://www.xces.org/schema/2003\"/>\n")
    out_fn.write("      </annotationSets>\n")
    out_fn.write("  </header>\n")
    while(1):
        out_fn.write("  <region xml:id=\"penn-r" + str(id_index) + "\" anchors=\"" + str(tok_region[id_index * 2]) +" "+ str(tok_region[id_index * 2 + 1]) + "\"/>\n")
        out_fn.write("  <node xml:id=\"penn-n" + str(id_index) +"\">\n")
        out_fn.write("      <link targets=\"penn-r" + str(id_index) + "\"/>\n")
        out_fn.write("  </node>\n")
        out_fn.write("  <a label=\"" + ann + "\" ref=\"penn-n" + str(id_index) +"\" as=\"xces\">\n")
        out_fn.write("      <fs>\n")
        out_fn.write("          <f name=\"base\" value=\"" + tok[id_index] + "\"/>\n")        
        out_fn.write("      </fs>\n")
        out_fn.write("  </a>\n")
        id_index += 1
        if id_index == len(tok):
            break;
    out_fn.write("</graph>\n")    
    out_fn.close()

def text_get_sen_region(text_fn,ann):

    f = open(text_fn + ".txt", mode = "r", encoding = 'utf-8')    
    region = list()
    pre_line_index = 0
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        region.append(pre_line_index)
        region.append(pre_line_index + len(line))
        pre_line_index += len(line) + 2 #\r\n(2 charctures)
    f.close()
    return region

def write_ann_sentence(text_fn,ann):
    
    sen_region = text_get_sen_region(text_fn,ann)
    
    id_index = 0
    out_fn = open(text_fn + "-" + ann + ".xml", mode = "w", encoding = 'utf-8')
    out_fn.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    out_fn.write("<graph>\n")
    out_fn.write("  <header>\n")
    out_fn.write("      <tagsDecl>\n")
    out_fn.write("          <tagUsage gi=\"" + ann + "\" occurs=\"" + str(int(len(sen_region)/2)) + "\"/>\n")
    out_fn.write("      </tagsDecl>\n")
    out_fn.write("      <annotationSets>\n")
    out_fn.write("          <annotationSet name=\"xces\" type=\"http://www.xces.org/schema/2003\"/>\n")
    out_fn.write("      </annotationSets>\n")
    out_fn.write("  </header>\n")
    while(1):
        out_fn.write("  <region xml:id=\"s-r" + str(id_index) + "\" anchors=\"" + str(sen_region[id_index * 2]) +" "+ str(sen_region[id_index * 2 + 1]) + "\"/>\n")
        out_fn.write("  <node xml:id=\"s-n" + str(id_index) +"\">\n")
        out_fn.write("      <link targets=\"s-r" + str(id_index) + "\"/>\n")
        out_fn.write("  </node>\n")
        out_fn.write("  <a label=\"" + ann + "\" ref=\"s-n" + str(id_index) +"\" as=\"xces\"/>\n")
        id_index += 1
        if id_index == len(sen_region)/2:
        	break;
    out_fn.write("</graph>\n")   
    out_fn.close()


	
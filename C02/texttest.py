def wordcount(readtxt):
    dict={}
    readlist=readtxt.split()
    for every_word in readlist:
        if every_word in dict:
            dict[every_word]+=1
        else:
            dict[every_word]=1
    return dict

def testcmp(test1,test2):
    return_li=[]
    word_list1=test1.splitlines()
    word_list2=test2.splitlines()
    li_word=[column for column in word_list1 if column and column.isspace()]
    li_word2=[column for column in word_list2 if column and column.isspace()]
    li_len=len(li_word)
    li_len2=len(li_word2)
    for step in range(max(li_len,li_len2)):   
        if step<li_len and  step<li_len2:
            li_col1=li_word[step].split()
            li_col2=li_word2[step].split()
            if li_col1!=li_col2:
                return_li.append((word_list1.index(li_word[step]),
                     word_list2.index(li_word2[step]),li_word[step],li_word2[step]))
        else:
            if li_len>li_len2:
                return_li.append((word_list1.index(li_word[step]),-1,li_word[step],''))
            else:
                return_li.append((-1,word_list2.index(li_word2[step]),'',li_word2[step]))
    return return_li

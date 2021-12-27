from html_table_parser.parser import HTMLTableParser
import pandas as pd
from multiprocessing import Process
import os

def run(filename):

    f=open('raw/'+filename,'r',encoding='utf-8')
    xhtml=f.read()
    f.close()

    p = HTMLTableParser()
    p.feed(xhtml)

    data=p.tables
    # print(len(data)) 19


    ## data[1] starts ##

    df1=pd.DataFrame()
    #print(data[1])
    #print(len(data[1]))
    for i in range(len(data[1])):
        if i==len(data[1])-2: break
        head=data[1][i][0]
        content=data[1][i][1]

        df1[head]=[content]

    i=len(data[1])-2

    head=data[1][i][0]

    i=len(data[1])-1

    content=data[1][i][0]+' '+data[1][i][1]

    df1[head]=content



    ## data[1] ends ##

    ## data[2] starts ##

    head=data[2][1][0]

    content=''
    for i in range(len(data[2])):
        if i>1:
            string=' '.join(data[2][i])
            content+=string+' '

    content=content.replace('\n',' ')

    df1[head]=[content]


    ## data[2] ends ##

    ## data[3] starts ##

    head=data[3][1][0]

    content=''
    for i in range(len(data[3])):
        if i>1:
            string=' '.join(data[3][i])
            content+=string+' '

    content=content.replace('\n',' ')

    df1[head]=[content]

    ## data[3] ends ##

    ## data[4] start ##

    head=data[4][1][0]

    content=''
    for i in range(len(data[4])):
        if i>1:
            string=' '.join(data[4][i])
            content+=string+' '

    content=content.replace('\n',' ')

    df1[head]=[content]

    ## data[4] ends ##

    ## data[5] starts ##

    head=data[5][1][0]
    content=data[5][1][1]

    df1[head]=[content]

    ## data[5] ends ##

    ## data[6] starts ##

    head=data[6][1][0]
    content=' '.join(data[6][1][1:])+' '.join(data[6][2])+' '.join(data[6][3])
    content=content.replace('\n',' ')

    df1[head]=[content]

    ## data[6] ends ##

    ## data[7] starts ##

    head=data[7][1][0]
    content=data[7][1][1]+' '+data[7][2][0]+' '+data[7][1][2]+' '+data[7][2][1]

    df1[head]=[content]

    ## data[7] ends ##

    ## data[8] starts ##


    head=data[8][1][0]
    content=data[8][1][1]

    df1[head]=[content]

    ## data[8] ends ##


    df1.to_csv('output/'+filename+'_'+'out1.csv',index=False)


    ## data[8] starts again ##

    cols=data[8][3]
    information=data[8][4:]

    df2=pd.DataFrame(information,columns=cols)
    df2.to_csv('output/'+filename+'_'+'out2.csv',index=False)

    ## data[8] ends again ##

    ## data[9] starts ##

    cols=data[9][2]
    information=data[9][3:]

    df3=pd.DataFrame(information,columns=cols)
    df3.to_csv('output/'+filename+'_'+'out3.csv',index=False)

    ## data[9] ends ##

    print(filename+' completed')

if __name__ == '__main__':
    files=os.listdir('raw')
    for i in files:
        print(i,'Processing')
        Process(target=run,args=(i,)).start()
    print()




#print(p.tables[1])
#print("\n\nPANDAS DATAFRAME\n")
#print(pd.DataFrame(p.tables[1]))

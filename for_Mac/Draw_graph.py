#Draw_graph
import matplotlib.pyplot as plt

#for Mac
plt.rcParams['font.family'] ='AppleGothic'
plt.rcParams['axes.unicode_minus'] =False

coler = ['#3d59ff','#ffe13d']

################  test data setting
"""
maleS = {}
femaleS = {}p

for i in range(0,170,10):
    
    maleS[i] = i*(i-100)
    femaleS[i] = (i-50)*(i-150)
"""

##################################

#################  font setting
title_font = {
    'fontsize' : 20,
    'fontweight' : 'bold' 
}

sub_font = {
    'fontsize' : 10
}


############################################################
def DrawG( subject, maleS , femaleS):

    ### sorting data and relocated
    mkey = list(maleS.keys())
    mkey.sort()
    mvalue = []
    for i in range(0,170):
        if i in mkey:
            mvalue.append(maleS[i])

    fkey = list(femaleS.keys())
    fkey.sort()
    fvalue = []
    for i in range(0,170):
        if i in fkey:
            fvalue.append(femaleS[i])
    ##################################

    Mratio = []
    Fratio = []
    for i in range(0,len(mkey)):
        Mratio.append(mvalue[i]/(mvalue[i]+fvalue[i])*100)
        Fratio.append(100-Mratio[i])

    ### draw graph
    '''
    plt.plot(mkey,Mratio,"b-",)
    plt.plot(fkey,Fratio,"r-",)
    '''
    plt.margins(x=0,y=0)
    plt.stackplot(fkey,Mratio,Fratio, colors = coler,labels = ['남자','여자'])
    ### setting elements
    plt.ylabel('성별에 따른 비율')
    plt.xlabel('표준점수')
    plt.legend()
    plt.grid(True)
    plt.title(subject,fontdict =title_font ,loc = 'left', pad =15)
    plt.title("male = blue / female = red",fontdict = sub_font, loc = 'right', pad =15)
    plt.show()

#############################################################

###### test drawing
#DrawG("language", maleS, femaleS)

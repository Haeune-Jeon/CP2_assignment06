#Draw_graph
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='AppleGothic'
plt.rcParams['axes.unicode_minus'] =False


################  test data setting
"""
maleS = {}
femaleS = {}

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

    ### draw graph

    plt.plot(mkey,mvalue,"b-",)
    plt.plot(fkey,fvalue,"r-",)
    ### setting elements
    plt.ylabel('Number of student')
    plt.xlabel('Standard score')
    plt.title(subject,fontdict =title_font ,loc = 'left', pad =15)
    plt.title("male = blue / female = red",fontdict = sub_font, loc = 'right', pad =15)
    plt.show()

#############################################################

###### test drawing
#DrawG("language", maleS, femaleS)

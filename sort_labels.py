# -*- coding: utf-8 -*-
import pandas as pd
import argparse
import os

# In[]
def get_list(path, extension):
    temp=os.listdir(path)
    for i,v in enumerate(temp):
        if ('jpg' in v):
            temp.pop(i)
            
    for i,v in enumerate(temp):
        if ('classes' in v):
            temp.pop(i)
            
    temp2=[]
    for i,v in enumerate(temp):
        if '.txt' in v:
            temp2.append(os.path.join(path,v))
    return temp2

# In[]
parser = argparse.ArgumentParser(description="input the [-p path]path that would like to list in [-e extension]")
parser.add_argument('-p','--path',default='test_images')
parser.add_argument('-e','--extension',default='txt')
args=parser.parse_args()
print(args.__dict__)
temp=get_list(args.path, args.extension)


# In[]
for tempname in temp:
    print(tempname)
    data = pd.read_csv(tempname,delimiter=' ',encoding='utf-8',header=None,prefix='var')
    data.sort_values(by=['var2','var1'],inplace=True)
    data.to_csv(tempname,sep=' ',index=False,header=False)
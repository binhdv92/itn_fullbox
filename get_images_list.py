# -*- coding: utf-8 -*-


# In[] Import
import argparse
import os
import pandas as pd


# In[] Def
def get_list():
	temp2=os.listdir(args.path)
	temp=[]
	for i,v in enumerate(temp2):
		if args.extension in v:
			temp.append(v)
	return temp


def get_list_perfix():
    #temp_perfix=""
    #for i in args.perfix:
    #    temp_perfix=os.path.join(temp_perfix,i)
    
    temp2=os.listdir(args.path)
    temp=[]
    for i,v in enumerate(temp2):
        if args.extension in v:
            temp3=os.path.join(args.perfix,args.path,v)
            if args.linux:
                temp3 = temp3.replace("\\",'/')
            temp.append(temp3)
               
    return temp

# In[] Argument
parser=argparse.ArgumentParser(description="input the [-p path]path that would like to list in [-e extension]")
parser.add_argument('-p','--path', default = 'train_images')
parser.add_argument('-l', '--linux', default = 1)
parser.add_argument('-e','--extension', default = 'jpg')
parser.add_argument('-px','--perfix', default= 'itn2')
args=parser.parse_args()
print(f'Arguments: {args.__dict__}')


# In[] 
temp=get_list()
df=pd.DataFrame(temp)
df.to_csv(f'{args.path}.csv',header=False,sep=',',index=False,line_terminator='\n')
for i in temp:
	print(i)


# In[]
temp2=get_list_perfix()
df2=pd.DataFrame(temp2)
df2.to_csv(f'{args.path}_perfix.csv',header=False,sep=',',index=False,line_terminator='\n')
for i in temp2:
	print(i)
    

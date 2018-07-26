#import tool
import sys
inputfile_1=sys.argv[1]
inputfile_2=sys.argv[2]
#create dictionary
def list2dict(s):
    d={}
    for i in s:
        if i in d.keys():
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
#define a function to match key and value between 2 files
def cmplist (s1,s2):
    d1=list2dict(s1)
    d2=list2dict(s2)
    d1_keys=set(d1.keys())
    d2_keys=set(d2.keys())
    intersect_keys=d1_keys.intersection(d2_keys)
    added={}
    for i in (d2_keys-d1_keys):
        added[i]=d2[i]
    removed={}
    for i in (d1_keys-d2_keys):
        removed[i]=d1[i]
    modified={}
    for i in intersect_keys:
        if d1[i]!=d2[i]:
            modified[i]=d1[i],d2[i]
    same={}
    for i in intersect_keys:
        if d1[i]==d2[i]:
            same[i]=d1[i]
    return added, removed, modified,same
with open(inputfile_1,"r") as f1:
     result=f1.read().split('\n')
     print(result[0]) 
     f1list=[]
     for line in result:
         f1list.append(line)

with open(inputfile_2,"r") as f2:
    result2=f2.read().split('\n')
    f2list=[]
    for line in result2:
        f2list.append(line)
added_out, removed_out, modified_out, same_out=cmplist(f2list,f1list)
#print out the results on screen 
print("Number of observations in spec but not in output ----------")
print(len(added_out))
print("Number of observations in both docs--------")
print(len(same_out))
print("Number of observations in the output but not in spec---------")
print(len(removed_out))
print("Number of observations were modified in the output---------")
print(len(modified_out))
print("Below is the records in spec but not in the output-----")
print(added_out)
print("Below is the records in the output but not in spec------")
print(removed_out)


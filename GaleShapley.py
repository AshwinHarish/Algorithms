# Gale Shapley
menpref={"V":["A","B","C"],"W":["B","C","A"],"X":["A","B","C"]}
womenpref={"A":["W","X","V"],"B":["X","V","W"],"C":["V","W","X"]}
freemen=["V","W","X"]
takenwomen=[]
final={}
while freemen!=[]:
    for i in freemen:
        #print("MAN=",i)
        listofw=menpref.get(i)
        #print("List of women for ",i,listofw)
        for j in listofw:
            if j not in takenwomen:
                final[j]=i
                freemen.remove(i)
                #print("list of freemen",freemen)
                takenwomen.append(j)
                #print("final list= ",final)
                break
            else:
                listofm=womenpref.get(j)
                #print("list of men for ",j,listofm)
                r=final.get(j)
                #print("Previously matched man",r)
                p=listofm.index(i)
                #print(p)
                q=listofm.index(r)
                if p<q:
                    final[j]=i
                    freemen.remove(i)
                    freemen.append(r)
                    takenwomen.append(j)
                    break
print(final)

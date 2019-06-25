def findMinAndMax(L):
    if L==[]:
        return(None,None)
    else:
        min=max=L[0]
        for v in L:
            if v<min:
                min=v
            if v>max:
                max=v
        return(min,max)
                       

print(findMinAndMax([0,0,0,0,2]))

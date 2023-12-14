
# Ouverture et lecture du fichier .dat
with open('husqvarna.dat', 'r') as file:
    lignes = file.read()

x=None
y=None
xt=None
yt=None
orient=None

numbers =("0","1","2","3","4","5","6","7","8","9")

for i in range(0,len(lignes)-1):
    c = lignes[i]

    if x==None:
        x=int(c)
    elif y==None:
        y=int(c)
    else:
        if c in numbers:
            if lignes[i+1] in numbers:
                if xt!=None:
                    print(str(xt)+str(yt)+" "+orient)
                xt=int(c)
            else:
                yt=int(c)
        elif lignes[i-1]==" ":
            orient=c
        elif c=='G':
            if orient=='N':
                orient='W'
            elif orient=='W':
                orient='S'
            elif orient=='S':
                orient='E'
            else:
                orient='N'

        elif c=='D':
            if orient=='N':
                orient='E'
            elif orient=='E':
                orient='S'
            elif orient=='S':
                orient='W'
            else:
                orient='N'

        elif c=='A':
            if orient=='N' and yt>0:
                yt+=1
            elif orient=='W' and xt>0:
                xt-=1
            elif orient=='S'and yt<y:
                yt-=1
            elif orient=='E' and xt<x:
                xt+=1

    #print(c+" ; "+str(xt)+str(yt)+" "+str(orient))

print(str(xt)+str(yt)+" "+orient)



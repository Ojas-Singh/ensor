from termcolor import colored
def func(main,final):
    E=0
    for i in range(len(main[0])):
        for j in range(0,i):
            if main[i][j]==1:
                E=E+1
    print colored("non-bond in molecule :", 'blue'), E
    nE=0
    for x in final:
        for i in x[1]:
            for j in x[1]:
                if main[i-1][j-1]==1 and i>j:
                    if len(x[0])%2 == 0:
                        nE=nE-1
                    else:
                        nE=nE+1
    print colored("non-bond in Calculated Frags :", 'blue'),nE
    print colored("non-bond coverage :", 'blue'),colored(100*(float(nE)/float(E)), 'green')

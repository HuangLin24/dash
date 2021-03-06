import os

def data():
    realPath=os.path.realpath(__file__)[:-18]
    algorithmsNum=4
    TYPE_NAME=['same','diff']
    TRACE_LIST=[name for name in os.listdir(realPath+TYPE_NAME[0])]
    LEN=len(TRACE_LIST)
    #print(realPath+TYPE_NAME[0]+'/'+TRACE_LIST[0]+'/index.txt')



    Index=[[[0 for k in range(algorithmsNum)] for i in TYPE_NAME] for x in range(3)]
    # Index is 3 dim 
    # Index[0] is FairIndex,[1] is EfficiencyIndex,[2] is StabilityIndex
    # Index[0][0] is same,[0][1] is diff
    # Index[0][0][0] is bb,[0][0][1] is mpc,[0][0][2] is mpcfast,[0][0][3] is pensieve


    for typeindex,typename in enumerate(TYPE_NAME):
        for traceindex,tracename in enumerate(TRACE_LIST):
            with open(realPath+typename+'/'+tracename+'/index.txt') as f:
                for index,line in enumerate(f):
                    par=line.split()
                    for algorithmsindex,data in enumerate(par):
                        Index[index][typeindex][algorithmsindex]+=float(data)


    indexName=['fairness','efficiency','stability']
    for index in range(len(Index)):
        for typeindex in range(len(Index[index])):
            for algorithmsindex in range(algorithmsNum):
                Index[index][typeindex][algorithmsindex]/=LEN


    for i in Index:
        print(i)

    for index,name in enumerate(indexName):
        with open(realPath+indexName[index]+".txt",'wb') as f:
            for typeindex in range(len(TYPE_NAME)):
                for algorithmsindex in range(algorithmsNum):
                    f.write(str(Index[index][typeindex][algorithmsindex])+' ')
                f.write("\n")



if __name__ == '__main__' :
    data()

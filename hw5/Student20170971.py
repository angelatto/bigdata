import sys
import os
import numpy as np
import operator


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                            key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def changeFile(filename):
    Vector = np.zeros((1, 1024)) #(32*32) 2차원배열을 1차원배열로 
    f = open(filename)
    for i in range(32):
        lineStr = f.readline()
        for j in range(32):
            Vector[0, 32*i+j] = int(lineStr[j])
    return Vector #일차원배열이 출력(파일내용을 0과1으로주르륵 담은것)

def createDataSet():
    path_training = sys.argv[1]
    
    labels = []
    trainingFileList = os.listdir(path_training)
    trainingSize = len(trainingFileList) #파일개수
    trainingMat = np.zeros((trainingSize, 1024))
    
    for i in range(trainingSize):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        dataLabel = int(fileStr.split('_')[0])
        labels.append(dataLabel)
        trainingMat[i, :] = changeFile(path_training+'/%s' % fileNameStr)

    return trainingMat, labels

if __name__ == "__main__":
    group, labels = createDataSet() #그룹과 라벨이 서로 대응됨 

    #지금부터 뉴케이스를 구하는 코드 
    path_test = sys.argv[2]
    testFileList = os.listdir(path_test)
    testSize = len(testFileList)
    testMat = np.zeros((testSize, 1024))
    resultLabel = -1
    errorCount = 0

    j = 1
    while j <= 20:
        for i in range(testSize):
            testFileName = testFileList[i]
            testFileStr = testFileName.split('.')[0]
            answer = int(testFileStr.split('_')[0]) #진짜 답
            testMat[i, :] = changeFile(path_test + '/%s' % testFileName)
            if(answer !=  classify0(testMat[i], group, labels, j)):
                errorCount += 1
        print(int(errorCount / testSize * 100)) #에러율을 출력한다. 
        j += 2

import sys
import numpy as np
'''
    This function is used to read the training and testing files.
'''
def ReadFile(FileName):
    OpenedFile = open(FileName, 'r')
    Data = []

    Line = OpenedFile.readline()
    while Line != '':
        LineSplit = Line.split(',')
        list = []
        for x in LineSplit:
            list.append(int(x))
        Data.append(list)
        Line = OpenedFile.readline()
    return Data

'''
    This function separates the data based on their class number (0 and 1).
    This is done so that calculating prior probabilities become easier.
'''
def SeparatingBasedOnClasses(TrainingData):
    Data = {}
    Data[0] = []
    Data[1] = []
    Length = len(TrainingData)
    for x in range(Length):
        ClassNumber = TrainingData[x][0]
        TrainingData[x] = TrainingData[x][1:]
        Data[ClassNumber].append(TrainingData[x])
    return Data
    
'''
    This function is used to calculate the prior probabilities using the seperated training data.
'''
def PriorProbabilities(SeparatedTrainingData):
    d = 0
    TestNormal0 = np.zeros(22)
    TestNormal1 = np.zeros(22)
    TestAbnormal0 = np.zeros(22)
    TestAbnormal1 = np.zeros(22)
    
    for ClassNumber, Data in SeparatedTrainingData.items():
        if ClassNumber == 0:
            for y in range(22):
                for x in Data:
                    if x[y] == 0:
                        TestAbnormal0[y] += 1
                    elif x[y] == 1:
                        TestAbnormal1[y] += 1
        elif ClassNumber == 1:
            for y in range(22):
                for x in Data:
                    if x[y] == 0:
                        TestNormal0[y] += 1
                    elif x[y] == 1:
                        TestNormal1[y] += 1
    
    TestNormal0 /= float(80+2)
    TestNormal1 /= float(80+2)
    TestAbnormal0 /= float(80+2)
    TestAbnormal1 /= float(80+2)
    
    Normal = (40)/float(22)
    Abnormal = (40)/float(22)
    return (TestNormal0, TestNormal1, TestAbnormal0, TestAbnormal1, Normal, Abnormal)


'''
    This function predicts if the test results conclude as normal or abnormal and
    then compares it with the actual answer. Finally, the accuracy percentage is calculated.
'''
def predict(TestingData, TestNormal0, TestNormal1, TestAbnormal0, TestAbnormal1, Normal, Abnormal):
    Answer = []
    Length = len(TestingData)
    for x in range(Length):
        Answer.append(TestingData[x][0])
        TestingData[x] = TestingData[x][1:]
    
    Prediction = []
    for x in TestingData:
        c1 = Normal
        c0 = Abnormal
        for y in range(22):
            if x[y] == 0:
                c1 *= TestNormal0[y]
                c0 *= TestAbnormal0[y]
            elif x[y] == 1:
                c1 *= TestNormal1[y]
                c0 *= TestAbnormal1[y]
        if c1 > c0:
            Prediction.append(1)
        else:
            Prediction.append(0)
    
    
    accurate = 0
    for x in range(Length):
        if Prediction[x] == Answer[x]:
            accurate += 1
    
    accuracy = accurate/float(len(Prediction))
    accuracy *= 100.0
    
    print('Total Accuracy: = ', accuracy, '%\n')
    print('##########\n')

def main(TrainingFileName, TestingFileName):
    print('##########\n')
    print('Starting to Train on 80 data points . . .\n')
    
    TrainingData = ReadFile(TrainingFileName)
    SeparatedTrainingData = SeparatingBasedOnClasses(TrainingData)
    TestNormal0, TestNormal1, TestAbnormal0, TestAbnormal1, Normal, Abnormal = PriorProbabilities(SeparatedTrainingData)
    print('Training Complete\n\n')
    print('Testing on 187 data point . . .\n')
    
    
    TestingData = ReadFile(TestingFileName)
    predict(TestingData, TestNormal0, TestNormal1, TestAbnormal0, TestAbnormal1, Normal, Abnormal)
    
main(sys.argv[1], sys.argv[2])

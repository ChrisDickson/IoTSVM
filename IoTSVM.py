#Imports
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

import time
import pandas as pd
import datetime

#0 is benign, 1 is malicious
class_names = ['0','1']

def createSVM(X, y):
    #Variables used in the creation of the SVM and output
    c_values = [x/2 for x in range(1,21)]
    #Used to remove features with no variance (all the same value)
    fThresh = VarianceThreshold()
    
    fSel = SelectKBest(chi2, k=10)

    file = 'output - t - K = 10 L .csv'  
    outputDF = pd.DataFrame(columns=['Kernel', 'C Value', 
                                     'Confusion Matrix','Accuracy',
                                     'Training Time','Testing Time',
                                     'Total Time', 'Precision',
                                     'Recall', 'F1'])
    #Kernels used - not using poly as early tests showed it takes too long to be worth doing full runs with on this data set
    kernels = ['linear','rbf','sigmoid']
    '''
        Scaling required to ensure columns containing large integers, 
        such as Balance, age or day, do not have an inappropriately large effect on
        the SVM's training due to size of contents
    '''
    X_scaling = MinMaxScaler(feature_range=(0,1)).fit(X)
    X_scaled = X_scaling.transform(X)
    X_vari = fThresh.fit_transform(X_scaled)
    X_fSel = fSel.fit_transform(X_vari, y)
    X_train, X_test, y_train, y_test = train_test_split(X_fSel, y, 
                                                            test_size = 0.2,
                                                        random_state=42)

# =============================================================================
    for k in kernels:
         for c in c_values:
             start = time.time()
             svc = svm.SVC(kernel=k, C=c)
             svc.fit(X_train, y_train)
             trainTime = (time.time()-start)
             y_pred = svc.predict(X_test)
             testTime = time.time()-trainTime
             cnf_matrix = confusion_matrix(y_test, y_pred)
             asc = accuracy_score(y_test, y_pred)*100
             end = time.time()
             elapsed = end-start 
             prec = precision_score(y_test, y_pred)
             recall = recall_score(y_test, y_pred)
             f1_value = f1_score(y_test, y_pred)
             
             outputDF = outputDF.append({'Kernel':k,
                                         'C Value':c,
                                         'Confusion Matrix':cnf_matrix,
                                         'Accuracy':asc,
                                         'Training Time':trainTime,
                                         'Testing Time':testTime,
                                         'Total Time':elapsed,
                                         'Precision':prec,
                                         'Recall':recall,
                                         'F1': f1_value}, ignore_index=True)
# =============================================================================
    outputDF.to_csv(file)

#Reads in dataset, removing lines containing empty cells
df = pd.read_csv('tenth_combined_data.csv')
df = df.dropna()
'''
    Drops columns. Subscribed must be seperated from attributes. Others can be 
    dropped to test accuracy without them.
'''
df2 = df.drop(['Class'],1)
X = df2.as_matrix()
y = df['Class'].values 

SVMstart = time.time()
createSVM(X, y)
SVMend = time.time()
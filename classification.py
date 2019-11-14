import pandas as pd
import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
import warnings
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings("ignore", category=FutureWarning)
pd.set_option('display.max_rows',300000)
np.set_printoptions(threshold=sys.maxsize)

"""
@author: Talessil
Building and evaluating  classification Algorithms
input: fp_input_def.csv
output: results.csv
"""

""" CLASSIFICATION ALGORITHMS """

dados = pd.read_csv("fp_input_def.csv", sep=";", header=0)

X = dados
Y = dados['requested']
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.3, random_state=7)

models=[]
models.append(('LDA', LinearDiscriminantAnalysis()))
#models.append(('LR', LogisticRegression()))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC(gamma='scale')))


results=[]
names=[]
for name, model in models:
    
    model.fit(X_train, Y_train)
    kfold = model_selection.KFold(n_splits=10, random_state=7)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    preds = model.predict(X_test)
    precision, recall, fscore, support = score(Y_test, preds)
    print('precision: {}'.format(precision))
    print('recall: {}'.format(recall))
    print('fscore: {}'.format(fscore))
    print('support: {}'.format(support))
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    print(pd.crosstab(Y_test, preds, rownames=['Actual Result'], colnames=['Predicted Result'])) 
   

#save results
size = 0
for n in X_test.values:
    size = size + 1
aux = X_test.values
with open('result.csv', mode='w') as result:
    result = csv.writer(result, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
    result.writerow(['author_id', 'discussion', 'review', 'qntags', 'pull', 'preds'])
    for k in range(size):
        result.writerow([str(aux[k][0]),str(aux[k][1]),str(aux[k][2]),str(aux[k][3]),str(aux[k][4]),str(preds[k])])


#show false positives
dados = pd.read_csv("fp_input_def.csv", sep=";", header=0)
array = dados.values
dados2 = pd.read_csv("result.csv", sep=";", header=0)
array2 = dados2.values
size = 0
for n in array:
    size = size + 1
size2 = 0
for n in array2:
    size2 = size2 +1
for l in range(size2):
    for k in range(size):
        if array[k][0] == array2[l][0]: # if the id is the same
            if array2[l][5] == 0 and array[k][5] == 1: # if it is false positive
                print(array2[l][0])
               
                
                   
# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

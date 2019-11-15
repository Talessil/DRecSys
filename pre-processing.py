import pandas as pd
import numpy as np
import csv
from sklearn.utils import shuffle

"""
@author: Talessil
preprocessing code: outliers scale reduction, normalization, 
                        instance splitting - test and training (optional)
input: fp_input.csv
output: fp_input_def.csv
"""

# READING
data = pd.read_csv("fp_input.csv", sep=";", header=0)
array_all = data.values
array = data.values

size = 0
for n in array:
    size = size + 1

""" OUTLIERS SCALE REDUCTION : FOR EACH ATTRIBUTE """

# 3rd QUARTILE CALCULUS

q1, q3= np.percentile(data.discussion,[25,75])
iqr = q3 - q1
lower_bound_discussion = q1 -(1.5 * iqr) 
upper_bound_discussion = q3 +(1.5 * iqr) 
print(lower_bound_discussion)
print(upper_bound_discussion)

q1, q3= np.percentile(data.review,[25,75])
iqr = q3 - q1
lower_bound_review = q1 -(1.5 * iqr) 
upper_bound_review = q3 +(1.5 * iqr) 
print(lower_bound_review)
print(upper_bound_review)

q1, q3= np.percentile(data.qntags,[25,75])
iqr = q3 - q1
lower_bound_qntags = q1 -(1.5 * iqr) 
upper_bound_qntags = q3 +(1.5 * iqr) 
print(lower_bound_qntags)
print(upper_bound_qntags)

q1, q3= np.percentile(data.pull,[25,75])
iqr = q3 - q1
lower_bound_pull = q1 -(1.5 * iqr) 
upper_bound_pull = q3 +(1.5 * iqr) 
print(lower_bound_pull)
print(upper_bound_pull)

# RE-WRITTING WITH THE NEW CHANGES (TEMP FILE IS CREATED FOR TEMPORARY CHANGES)

# REMOVE TARGET ATTRIBUTE
k = 0
with open('temp.csv', mode='w') as reduct:
    reduct = csv.writer(reduct, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
    reduct.writerow(['discussion', 'review', 'qntags', 'pull'])
    for k in range(size):
        reduct.writerow([str(array[k][1]),str(array[k][2]),str(array[k][3]),str(array[k][4])])

# ATTRIBUTE DISCUSSION
data = pd.read_csv("temp.csv", sep=";", header=0)
array = data.values
k = 0
with open('temp.csv', mode='w') as reduct:
    reduct = csv.writer(reduct, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
    reduct.writerow(['discussion', 'review', 'qntags', 'pull'])
    for k in range(size):
        if(array[k][0]>upper_bound_discussion):
            coef = upper_bound_discussion/array[k][0]
            reduct.writerow([str(upper_bound_discussion),str("%.2f" % (coef*array[k][1])),str("%.2f" % (coef*array[k][2])),str("%.2f" % (coef*array[k][3]))])
        else:
            reduct.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3])])

# ATTRIBUTE REVIEW
data = pd.read_csv("temp.csv", sep=";", header=0)
array = data.values
k = 0
with open('temp.csv', mode='w') as reduct:
    reduct = csv.writer(reduct, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
    reduct.writerow(['discussion', 'review', 'qntags', 'pull'])
    for k in range(size):
        if(array[k][1]>upper_bound_review):
            coef = upper_bound_review/array[k][1]
            reduct.writerow([str("%.2f" % (coef*array[k][0])),str(upper_bound_review),str("%.2f" % (coef*array[k][2])),str("%.2f" % (coef*array[k][3]))])
        else:
            reduct.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3])])

# ATTRIBUTE QNTAGS
data = pd.read_csv("temp.csv", sep=";", header=0)
array = data.values
k = 0
with open('temp.csv', mode='w') as reduct:
    reduct = csv.writer(reduct, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
    reduct.writerow(['discussion', 'review', 'qntags', 'pull'])
    for k in range(size):
        if(array[k][2]>upper_bound_qntags):
            coef = upper_bound_qntags/array[k][2]
            reduct.writerow([str("%.2f" % (coef*array[k][0])),str("%.2f" % (coef*array[k][1])),str(upper_bound_qntags),str("%.2f" % (coef*array[k][3]))])
        else:
            reduct.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3])])

# ATTRIBUTE PULLREQUEST
data = pd.read_csv("temp.csv", sep=";", header=0)
array = data.values
k = 0
with open('temp.csv', mode='w') as reduct:
    reduct = csv.writer(reduct, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
    reduct.writerow(['discussion', 'review', 'qntags', 'pull'])
    for k in range(size):
        if(array[k][3]>upper_bound_pull):
            coef = upper_bound_pull/array[k][3]
            reduct.writerow([str("%.2f" % (coef*array[k][0])),str("%.2f" % (coef*array[k][1])),str("%.2f" % (coef*array[k][2])),str(upper_bound_pull)])
        else:
            reduct.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3])])

############################################################################################################################################################

""" NORMALIZATION """

aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
data = pd.read_csv("temp.csv", sep=";", header=0)
array = data.values
for k in range(size):
    if(aux1 < array[k][0]):
        aux1 = array[k][0]
    if(aux2 < array[k][1]):
        aux2 = array[k][1]
    if(aux3 < array[k][2]):
        aux3 = array[k][2]
    if(aux4 < array[k][3]):
        aux4 = array[k][3]

# NORMALIZE
with open('temp.csv', mode='w') as reduct:
    reduct = csv.writer(reduct, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
    reduct.writerow(['author_id', 'discussion', 'review', 'qntags', 'pull', 'requested'])
    for k in range(size):
        reduct.writerow([str(array_all[k][0]),str("%.2f" % (array[k][0]/aux1)),str("%.2f" % (array[k][1]/aux2)),str("%.2f" % (array[k][2]/aux3)),str("%.2f" % (array[k][3]/aux4)),str(array_all[k][5])])

############################################################################################################################################################

""" SPLIT INSTANCE : TEST AND TRAINING - OPTIONAL"""
"""
cont_req = 0
cont_n_req = 0
data = pd.read_csv("temp.csv", sep=";", header=0)
array = data.values
array = shuffle(array) #SHUFFLE INSTANCE
for k in range(size):
    if array[k][5]==1:
        cont_req = cont_req + 1
    if array[k][5]==0:
        cont_n_req = cont_n_req + 1
        
coef_test_req = 0.3 * cont_req
coef_test_n_req = 0.3 * cont_n_req

cont_req = 0
cont_n_req = 0
with open('test.csv', mode='w') as test:
    with open('training.csv', mode='w') as training:
        test = csv.writer(test, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
        test.writerow(['author_id', 'discussion', 'review', 'qntags', 'pull', 'requested'])
        training = csv.writer(training, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
        training.writerow(['author_id', 'discussion', 'review', 'qntags', 'pull', 'requested'])
        for k in range(size):
            if array[k][5]==1 and cont_req<coef_test_req:
                test.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3]),str(array[k][4]),str(0)])
                cont_req = cont_req + 1
            elif array[k][5]==0 and cont_n_req<coef_test_n_req:
                test.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3]),str(array[k][4]),str(1)])
                cont_n_req = cont_n_req + 1
            else:
                if array[k][5]==1:
                    training.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3]),str(array[k][4]),str(0)])
                else:
                    training.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3]),str(array[k][4]),str(1)])
"""
############################################################################################################################################################

""" WRITE DEFINITIVE FILE"""

data = pd.read_csv("temp.csv", sep=";", header=0)
array = data.values
array = shuffle(array) #SHUFFLE
cont = 0
for k in range(size):
    if array[k][5]==1:
        cont = cont + 1
              
with open('fp_input_def.csv', mode='w') as defi:   
    defi = csv.writer(defi, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONE,lineterminator = '\n')
    defi.writerow(['author_id', 'discussion', 'review', 'qntags', 'pull', 'requested'])
    for k in range(size):
        if array[k][5]==1:
            defi.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3]),str(array[k][4]),str(0)])
        else:
            defi.writerow([str(array[k][0]),str(array[k][1]),str(array[k][2]),str(array[k][3]),str(array[k][4]),str(1)])
            
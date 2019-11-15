import networkx as nx
import pandas as pd
import statistics

"""
@author: Talessil
Complex network building and calculus :
input: git-network.csv
output: degree_centrality.txt, degree.txt, closeness.txt, betweenness.txt, pagerank.txt, out_degree.txt
"""

G = nx.Graph()
Gd = nx.DiGraph()

dados =  pd.read_csv('git-network.csv', sep=";", header=0)
f = open("test.txt","w") 
array = dados.values

size = 0
for n in array:
    size = size + 1

k = 0
for k in range(size):
   G.add_weighted_edges_from([(array[k][0], array[k][1], array[k][2])])

k = 0
for k in range(size):
   Gd.add_weighted_edges_from([(array[k][0], array[k][1], array[k][2])])

""" PRINT RESULTS RELATED TO DIRECTED GRAPH """

print('----------------------- FIRST VALUES -----------------------')
print('Node number:')
print(Gd.number_of_nodes())
print('Edge number:')
print(Gd.number_of_edges())
print('Number of component:')
print(nx.number_connected_components(G))
print('--------Number of nodes per component:--------')
for k in list(nx.connected_components(G)):
    print(len(k))
    
print('----------------------- CONCENTRATION -----------------------')
print('Density: (non directed graph)')
print(nx.density(G))
print('Density: (directed graph)')
print(nx.density(Gd))
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
sum = 0
cont = 0
for n in degree_sequence:
    sum += n
    cont = cont + 1
print('Mean Degree:')
print(sum/cont)

print('----------------------- OUT DEGREE VALUES -----------------------')
#print each node outdegree
f = open("out_degree.txt","w") 
max = 0
cont = 0
sum = 0
array = []
for (v,k) in Gd.out_degree():
    f.write(str(v)+": "+str(k)+"\n")   
    if k>max:
        max = k
    cont = cont + 1
    sum = sum + k
    array.append(k)

print("Higher out degree")
print(max)
print("Mean out degree")
print(sum/cont)
print(statistics.median(array))
f.close() 

print('----------------------- WEIGHTED OUT DEGREE VALUES -----------------------')
cont = 0
sum = 0
max = 0
array2 = []
for (v,k) in Gd.out_degree(weight='weight'):
    if k>max:
        max = k
    cont = cont + 1
    sum = sum + k
    array2.append(k)
print("Higher out degree (weighted)")
print(max)
print("Mean out degree (weighted)")
print(sum/cont)
print(statistics.median(array2))

print('----------------------- IN DEGREE VALUES -----------------------')
max = 0
cont = 0
sum = 0
for (v,k) in Gd.in_degree():
    if k>max:
        max = k
    cont = cont + 1
    sum = sum + k
print("Higher in degree")
print(max)
print("Mean in degree")
print(sum/cont)

print('----------------------- WEIGHTED IN DEGREE VALUES -----------------------')
max = 0
cont = 0
sum = 0
for (v,k) in Gd.in_degree(weight='weight'):
    if k>max:
        max = k
    cont = cont + 1
    sum = sum + k
print("Higher in degree (weighted)")
print(max)
print("Mean in degree (weighted)")
print(sum/cont)


""" SAVE CENTRALITY VALUES """

f = open("degree_centrality.txt","w") 
degrees = nx.degree_centrality(G)
f.write(str(degrees))           
f.close() 

f = open("degree.txt","w") 
degrees = nx.degree(G)
f.write(str(degrees))           
f.close() 

f2 = open("closeness.txt","w") 
clo_cen = nx.closeness_centrality(G)
f2.write(str(clo_cen))
f2.close() 

f2 = open("betweenness.txt","w") 
bet_cen = nx.betweenness_centrality(G)
f2.write(str(bet_cen))
f2.close() 

f3 = open("pagerank.txt","w")
pag_ran = nx.pagerank(G)
f3.write(str(pag_ran))
f3.close() 

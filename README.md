# DRecSysDiversity-based Expert Recommendation Approach.
 *Process focused in non-common experts recommendation.

Finding experts to assist with project is a crucial task in the Global Software Development (GSD) context, where a variety of stakeholders is involved. Automatic recommendation approaches lead to recommendations of the same group of popular developers, who ends up overloaded with many tasks to solve. This project aims to detect and recommend appropriate and diversified experts in GSD context. To that end, some popular GitHub projects were modeled as a collaborative network. The proposed approach uses NetSCAN clustering algorithm to detect communities and their core nodes. Some known classification algorithms are executed over the found core nodes and its results are compared. A diversity-base recommendation system is used to find experts (true positives), but with the flexibility to find people with features similar to those of experts (false positives).



The full database can be downloaded in: https://drive.google.com/open?id=1zCclYWc5CIKpR-xqZDTEI0u2X7018gz3 

FILES:
  
	-pre-processing.py: pre-processing and data manipulation.
  
	-classification.py: classifying models.
  
	-complex-network.py: network modeling and centrality calculations.


FOLDERS:
	
	-instances: tests (example) data.
	
	-NetSCAN_result: netscan execution results.


EXECUTION:

	-The database is first modeled as graph. For the network analysis use 'complex-network.py'. 
	-NetSCAN algorithm [1] is used in order to find core nodes.
	-A new network is build using the core nodes. Many attributes can be extracted from the full database. The chosen attributes are: "author_id", "discussion", "review", "qntags", "pull", "requested". There are an example file inside the instances folder.
	-The Pre-processing.py file contains outliers scale reduction function, as well as normalization and instance splitting - test and training (optional).
	-The classification algorithms are in 'classification.py' file.


[1] Horta, V., Stroele, V., Braga, R., David, J.M.N. and Campos, F., 2018. Analyzing scientific context of researchers and communities by using complex network and semantic technologies. Future Generation Computer Systems, 89, pp.584-605.

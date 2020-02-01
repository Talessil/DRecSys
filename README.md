# DRecSys
Diversity-based Expert Recommendation Approach.

Process with focus in experts recommendation.

The full database can be downloaded in: https://drive.google.com/open?id=1zCclYWc5CIKpR-xqZDTEI0u2X7018gz3 

FILES:
  
	-pre-processing.py: data manipulation and pre processing step.
  
	-classification.py: models study and false positive selection.
  
	-complex-network.py: network representation and centrality calculus.


FOLDERS:
	
	-instances: tests data.
	
	-NetSCAN_result: results obtained by netscan execution.


EXECUTION:

	The database is first modeled as graph. Some initial network analysis can be done using 'complex-network.py'. 
	Instances with "author_id", "discussion", "review", "qntags", "pull", "requested" as columns are created. There's an example inside FOLDER 'instances'. Pre-processing.py is used for outliers scale reduction, normalization and instance splitting - test and training(optional).
	Classification algorithms are implemented in 'classification.py'.

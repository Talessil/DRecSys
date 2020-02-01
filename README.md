# DRecSys
Diversity-based Expert Recommendation Approach.

Process focused in non-common experts recommendation.

The full database can be downloaded in: https://drive.google.com/open?id=1zCclYWc5CIKpR-xqZDTEI0u2X7018gz3 

FILES:
  
	-pre-processing.py: pre-processing and data manipulation facilitator.
  
	-classification.py: classifying models.
  
	-complex-network.py: network structuring and centrality calculus.


FOLDERS:
	
	-instances: tests (example) data.
	
	-NetSCAN_result: results obtained by netscan execution.


EXECUTION:

	-The database is first modeled as graph. For network analysis use 'complex-network.py'. 
	-NetSCAN algorithm [1] is used in order to find core (important) nodes.
	-Instances based on core nodes are created. Many attributes can be extracted from full database. The used attributes are: "author_id", "discussion", "review", "qntags", "pull", "requested". There are example file inside instances (folder).
	-Pre-processing.py contains outliers scale reduction, normalization and instance splitting - test and training (optional).
	-Implemented Classification algorithms in 'classification.py'.


[1] Horta,  V.,  Stroele,  V.,  Braga,  R.,  David,  J.M.N.  and  Campos,  F., 2018.  Analyzing  scientific  context  of  researchers  and  communities  by using  complex  network  and  semantic  technologies.  Future  Generation Computer Systems, 89, pp.584-605.

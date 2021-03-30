# DRecSys.

<h1 align = "center"> DRecSys: Diversity-based Recommendation Approach </h1>


Finding developers to assist with project issues is essential in Global Software Development (GSD) contexts, where various individuals with distinct characteristics are involved. Several recommending approaches lead to identifying the same group of individuals who end up work overloaded. Aiming to diversify the recommendation process, we introduced **DRecSys: a diversity-based recommendation approach.** We seek to identify individuals with characteristics similar to those previously requested to collaborate. To that end, we proposed a hybrid process composed of supervised (classification) and unsupervised (clustering) techniques. We provided evidence that DRecSys is able to recommend suitable non-obvious developers to assist with project issues.

## Published Work
This work was published in the **CSCWD 2020 : International Conference on Computer Supported Cooperative Work in Design, CSCWD**.

## Database
The full database can be downloaded in: https://drive.google.com/open?id=1zCclYWc5CIKpR-xqZDTEI0u2X7018gz3 

## Files:
* pre-processing.py: pre-processing and data manipulation.
* classification.py: classifying models.
* complex-network.py: network modeling and centrality calculations.

## Folders
* instances: tests (example) data.
* NetSCAN_result: netscan execution results.

## Execution:
* The database is first modeled as graph. For the network analysis use 'complex-network.py'. 
* NetSCAN algorithm [1] is used in order to find core nodes.
* A new network is build using the core nodes. Many attributes can be extracted from the full database. The chosen attributes are: "author_id", "discussion", "review", "qntags", "pull", "requested". There are an example file inside the instances folder.
* The Pre-processing.py file contains outliers scale reduction function, as well as normalization and instance splitting - test and training (optional).
* The classification algorithms are in 'classification.py' file.

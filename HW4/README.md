# Wine Quality Classification Kaggle dataset 
This repo "wine quality classification" is a project to explore, explain and compare different classification algoritms at wine dataset.

## Key features from ordinary analyses
Wine is splitted into three groups with unbalanced sample count: 
	- class 0: low quality wines 250 samples
	- class 1: medium quality wines 4250 samples
	- class 2: high quality wines 5 samples


## Used strategy
Three approaches to increase samples in class 2 (high quality wines) were used :
	- increase class 2 weights
	- generate new samples by making mean of two samples from class 2
	- generate new samples from class 1 + unique feature values (special for class 2)

## Project Scope
1. Explore features ( folder notebooks/explore )
1. Explain features ( folder reports/preliminary)
1. Prepare missed values and dataset without class 2 samples
1. Prepare class 2 samples as per used strategy ( folder data/processed)
1. Define criteria and run algoritms ( folder models)
1. Algoritm comparison ( folder models/ comparison )
1. Results ( folder reports/ final )
 

## Folder content
|project
|__data
	|__external
		|__ script or csv files
	|__intermid
		|__ different feature results
	|__processed 
		|__ final dataset used for model train 
|__notebooks
   |__explore
      |__ notebooks during exploratory work
   |__explain
       |__ notebooks for reports 
|__scripts 
|__reports 
   |__ reports preliminary and final 
|__models
	|__ weights and models pickle
	|__comparison 
		|__ comparison model results		

## Used ML and NN algoritms
- Logistic Regression
- Support Vector Classifier
- Decision Tree Classifier
---
- Random Forest
- Bagging Classifier
- Stacking Classifier
- Light GBM
---
- Dense + Dense
- SimpleRNN + Dense + Dense
- LSTM + Dense + Dense
- 2directional SimpleRNN + Dense  + Dense
- 2directional LSTM + Dense + Dense
- LSTM + Conv1D + Dense + Dense
- LSTM + Conv1D + Conv1D + Dense + Dense
- 2directional LSTM + Conv1D + Conv1D + Dense + Dense

## URL:	
[1] : link to Kaggle dataset https://www.kaggle.com/rajyellow46/wine-quality
[2] : link to git 



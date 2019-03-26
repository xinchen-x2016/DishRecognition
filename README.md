# DishRecognition
INF583-Project-DishRecognition

This repository contains the code to train and evaluate models for the project INF583, Dish Recognition.

## VireoFood172 DataSet
dataset download: http://vireo.cs.cityu.edu.hk/VireoFood172/VireoFood172.zip
label and split download: http://vireo.cs.cityu.edu.hk/VireoFood172/SplitAndIngreLabel.zip


## Code
#### Make dataset: 'make_dataset.py'
Two methods of classification:
#### 1, VGG16, modify and train only last two classifier layers, "VGG_classification.ipynb"
#### 2, Cross model, using pretrained features layers of VGG16, construct and train embedding layers and pooling methods, taking ingredients and cutting informations into consideration, "Ingredient_recognition_4.ipynb"

## Implementation
##### VGG-feature
##### Pooling by region
##### Output dish name by calculating similarity



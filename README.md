# face-recognition
Haar-cascade based facial recognition system


Building a facial recognition system require 3 steps
1) Create the dataset
2) Train the recogniser
3) Build a detector

NOTE-Follow the steps precisely for the system to work

## CREATING DATABASE
NOTE- REQUIRES WEBCAM
Firstly you need to create a folder named dataSet(case sensitive so keep the name as shown) in same folder as code. It will contain all training images.
Creating dataset require running datasetCreator.py. It will ask you for the id name and age and launch the web cam to take pictures for dataset,
and create entries for all the people you want to recognize in the database.

## TRAINING RECOGNIZER
Create a folder named recognizer(case sensitive) in same folder as code. It will store the trained classifier.
Run trainer.py which will create a classifier using haar-cascade.

## Detector
Now run face detection.py and enjoy detecting the faces you trained in classifier.


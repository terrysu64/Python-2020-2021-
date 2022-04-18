#Date: July 18, 2021
#Author: Terry Su
#Purpose: using the imageai library to initialize an image regocnition program in python

from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd() #current working directory

prediction = ImagePrediction()

prediction.setModelTypeAsMobileNetV2() #we will be using he "Mobile Net V2" model
prediction.setModelPath(os.path.join(execution_path, 'mobilenet_v2.h5'))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, 'house.jpg'), result_count = 10 ) #producing 10 predictions for house.jpg
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , f'%{eachProbability}')
print()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, 'godzilla.jpg'), result_count = 10 ) #producing 10 predictions for house.jpg
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , f'%{eachProbability}')
print()

predictions, probabilities = prediction.classifyImage('https://imageai.readthedocs.io/en/latest/_images/image21.jpg'), result_count = 10 ) #producing 10 predictions for house.jpg
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , f'%{eachProbability}')
print()

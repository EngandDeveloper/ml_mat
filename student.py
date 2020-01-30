import tensorflow
import numpy
import sklearn
import pandas

filename = "file_name.csv" #name of the data's file

data = pandas.read_csv(filename, sep="seperator , or ; or something else?")

data = [["label1", "label2", "label3", "etc."]]

predict = "label which you want to predict"

X = numpy.array(data.drop[predict], 1) #drop the label which you want to predict so you dont plot the label in data axis
y = numpy.array(data[predict]) #y axis is our prediction label

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

model = linear_model.LinearRegression() #select the model as linear regression for now since it is the moset basic one
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test) #checks the test data and compares answers to find accuracy of the model
print("Accuracy is:", accuracy) #prints accuracy - a number between 0 and 1



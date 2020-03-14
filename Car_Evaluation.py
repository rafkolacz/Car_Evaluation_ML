import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import pickle
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")

# a lot of data is non numeric, so we need to convert it
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

# we want to predict car class
predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))
Y = list(cls)

# simple creation of model
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(x_train,y_train)

acc = model.score(x_test,y_test)

print(acc)

''' # loop for optimization (for better performance use Colab!)
best = 0
bestnei = 0
neighbors = 3
for i in range(5):
  for i in range(10000):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

    model = KNeighborsClassifier(n_neighbors=5)

    model.fit(x_train,y_train)

    acc = model.score(x_test,y_test)

    if acc > best: 
      best = acc
      bestnei = neighbors
      with open("carmodel.pickle", "wb") as f:
        pickle.dump(model, f) 
  neighbors = neighbors + 2
print("Best accuracy: ", best)
print("Best number of neighbors: ", bestnei)
'''

pickle_in = open("carmodel.pickle", "rb")   # instead of creating model all the time
model = pickle.load(pickle_in)


predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]


# check predicted values with actual ones
for x in range(len(predicted)):
    print("Predicted: ", predicted[x], "Data: ", x_test[x], "Actual: ", names[y_test[x]])


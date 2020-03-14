import Car_Evaluation_Model

def prediction(x):
    temp = [[1, 1, 1, 1, 1, 1]]
    temp.append(x)
    predicted = Car_Evaluation_Model.model.predict(temp)

    return predicted[1]

z = [3,2,3,4,1,2]
print(prediction(z))

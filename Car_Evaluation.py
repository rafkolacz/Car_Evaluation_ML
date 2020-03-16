import Car_Evaluation_Model


def prediction(x): # predict car class using model from Car_Evaluation_Model
    temp = [[1, 1, 1, 1, 1, 1]]
    temp.append(x)
    predicted = Car_Evaluation_Model.model.predict(temp)

    return predicted[1]


def input_val(data): # converting non numeric data into numeric
    # features = ["buying", "maint", "door", "persons", "lug_boot", "safety"]
    size = ["small", "med", "big"]  # lug_boot
    names =['low', 'med', 'high', 'vhigh']  # buying and maint
    values = [1,2,3,4]
    conv_data = []
    print(data)
    count = 0

    for i in data:
        if count == 0 or count == 1 or count == 5:    # for buying and maint
            flag = 0
            for l in names:
                if i == l:
                    conv_data.append(values[flag])
                    break
                flag = flag + 1
        elif count == 2 or count == 3:      # dont need to convert (door/persons)
            conv_data.append(i)
        elif count == 4:                    # for lug boot
            flag = 0
            for l in size:
                if i == l:
                    conv_data.append(values[flag])
                    break
                flag = flag + 1
        count = count + 1                   # increase with every loop
    return conv_data


def engine(non_numeric): # combine prediction and input val
    classVal = ["unacceptable", "acceptable", "good", "very good"]
    numeric = input_val(non_numeric)
    result = prediction(numeric)
    result = classVal[result]   # unacceptable, acceptable, good, very good

    return result


data = ["high", "med", 2, 2, "small", "high"]
print(engine(data))



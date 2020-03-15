import Car_Evaluation_Model


def prediction(x):
    temp = [[1, 1, 1, 1, 1, 1]]
    temp.append(x)
    predicted = Car_Evaluation_Model.model.predict(temp)

    return predicted[1]


def input_val(data):
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



#z = [3,2,3,4,1,2]
#print(prediction(z))

data = ["high", "med", 2, 2, "small", "high"]

x = input_val(data)


# Naive Bayes Classifier
# By: Jakob Lybarger

def read_meta_file(name):
    meta_data = {}
    with open(name) as file:
        lines = file.readlines()
        for line in lines:
            key, values = line.split(":")[0], line.split(":")[1]
            values = values.strip().split(",")
            meta_data[key] = values
        file.close()
    return meta_data

def train_data(meta_data, file_name):
    counts = {}
    keys = list(meta_data)
    results = meta_data[keys[-1]]
    total_count = 0
    total_counts = [1]*len(results)
    del keys[-1]

    for key in keys:
        counts[key] = {}
        for value in meta_data[key]:
            counts[key][value] = {}
            for result in results:
                counts[key][value][result] = 1

    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(",")
            result = data[-1]
            result_index = results.index(result)
            total_count = total_count + 1
            total_counts[result_index] += 1
            for i in range(len(keys)):
                key = keys[i]
                count = counts[key][data[i]][result]
                counts[key][data[i]][result] = count + 1
        file.close()
   
    return counts, total_counts

def calculate(data, results, counts, total_counts, meta, classify=False):
    correct = 0
    length = len(meta)-1
    output = []
    for item in data:
        res = [1]*len(results)
        for result in results:
            index = results.index(result)
            res[index] = res[index] / (sum(total_counts))
            for i in range(length):
                count = counts[meta[i]][item[i]][result]
                res[index] = res[index] * (count / total_counts[index])
        
        index = 0
        for i in range(len(results)):
            if res[i] > res[index]:
                index = i
        
        if classify:
            print("here")
            output.append(",".join(item) + "," + results[index])
        else:
            output.append(",".join(item) + " / " + results[index])
            if results[index] == item[-1]:
                correct += 1

    return output, correct

def test_data(meta_data, counts, total_counts, file_name):
    meta = list(meta_data)
    total = 0
    results = meta_data[meta[-1]]
    data = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.strip().split(","))
            total = total + 1
    output, correct = calculate(data, results, counts, total_counts, meta)

    for i in output:
        print(i)

    print()
    print(str(total) + " instances in test data")
    print(str(correct) + " correctly classified")
    print("Accuracy = " + str(correct) + "/" + str(total))
    print()


def classify_data(meta_data, counts, total_counts, file_name, output_file):
    meta = list(meta_data)
    results = meta_data[meta[-1]]
    data = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split(",")
            if len(meta) == len(line):
                del line[-1]
            data.append(line)

    output = calculate(data, results, counts, total_counts, meta, True)[0]

    string = ""
    for i in output:
        string = string + i +"\n"

    with open(output_file, 'w') as file:
        file.write(string)
    file.close()

meta_data = None
training_data = None
total_counts = 0
while True:
    choice = int(input("1) New Meta Data and Training Data Files\n2) Read in and test data\n3) Read in and classify data\n4) EXIT\n"))
    if choice == 1:
        meta_data = None
        training_data = None
        total_counts = []
        meta = input("Enter name of meta file: ")
        meta_data = read_meta_file(meta)
        training = input("Enter name of training data file: ")
        training_data, total_counts = train_data(meta_data, training)
    elif choice == 2:
        test_file = input("Enter name of test data file: ")
        test_data(meta_data, training_data, total_counts, test_file)
    elif choice == 3:
        classify_file = input("Enter the file to be classified: ")
        output_file = input("Enter the name of the output file: ")
        classify_data(meta_data, training_data, total_counts, classify_file, output_file)
    else:
        break

print("Exiting...")
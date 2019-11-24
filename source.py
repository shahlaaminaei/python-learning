import csv
# For the average
from statistics import mean
from collections import OrderedDict
from collections import Counter
output_file_name = OrderedDict()

def calculate_averages(input_file_name, output_file_name):
    result=[]
    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            score=[float(x)for x in row[1:]]
            my_mean=mean(score)
            result.append((name,my_mean))
    with open(output_file_name,"w") as f:
        [f.write(str(name)+","+str(my_mean)+"\n")for name,my_mean in result]
        f.close()



def calculate_sorted_averages(input_file_name, output_file_name):
    list = OrderedDict()
    with open(input_file_name) as f_sorted:
        reader = csv.reader(f_sorted)
        for row in reader:
            list[row[0]] = float(row[1])
            result_sorted= OrderedDict(sorted(list.items(), key=lambda t: (t[1],t[0]) ))
    with open(output_file_name,"w") as f_sorted:
        [f_sorted.write(str(name)+","+str(result_sorted[name])+"\n")for name in result_sorted]
        f_sorted.close()

    

def calculate_three_best(input_file_name, output_file_name):
     list = OrderedDict()
     result_sorted = OrderedDict()
     counter = 0
     with open(input_file_name) as f:
         reader = csv.reader(f)
         for row in reader:
             list[row[0]] = float(row[1])
             result_sorted= OrderedDict(sorted(list.items(), key=lambda t: (t[1],t[0]) ,reverse=True))
     with open(output_file_name,"w") as f:
        for row in result_sorted:
            counter += 1
            f.write(str(row)+","+str(result_sorted.get(row,0))+"\n")
            if counter >= 3:
                break
        f.close()



def calculate_three_worst(input_file_name, output_file_name):
    list = OrderedDict()
    result_sorted = OrderedDict()
    counter = 0
    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            list[row[0]] = float(row[1])
            result_sorted= OrderedDict(sorted(list.items(), key=lambda t: (t[1],t[0])))
    with open(output_file_name,"w") as f:
        for row in result_sorted:
            counter += 1
            f.write(str(row)+","+str(result_sorted.get(row,0))+"\n")
            if counter >= 3:
                break
        f.close()




def calculate_average_of_averages(input_file_name, output_file_name):
    averages=[]
    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            for x in row[1:]:
                averages.append(float(x))
            my_mean = mean(averages)
    with open(output_file_name,"w") as f:
        f.write(str(my_mean))
        f.close()
    

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_stats(list):
    enrollment_num = []
    tuition = []
    for i in list:
        enrollment_num.append(i[1])
        tuition.append(i[2])
    return [enrollment_num,tuition]

print(enrollment_stats(universities))

def mean(list):
    mean = []
    for i in range(len(list)):
        mean.append(sum(list[i])/len(list[i]))
    return mean
print(mean(enrollment_stats(universities)))

def median(list):
    median = []
    for i in range(len(list)):
        list[i].sort()
        if int(len(list[i])%2) != 0:
            median.append(list[i][int(((len(list[i])-1)/2)+1)])
        else:
            median.append(list[i][int(len(list[i])/2)])
            median.append(list[i][int(len(list[i])/2+1)])
    return median
print(median(enrollment_stats(universities)))

print(f"******************************\n Total students: {


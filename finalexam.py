"""
This program will presennt # of grades, average of grades, and % of grades above the average.
The raw grade data will be stripped from "Final.txt"
separate calculations will be done for counting the number of grades, average, and exceptional scores.
results will be printed to end user
"""
"""
def strip_list()
path final.txt
open path to filename
    scores = stripped scores from Final.txt
    return the list to buffer
def main 
scores = strip_list to call on previous func
print ("student scores are")
average = sum(scores) / len(scores)
for i in scores:
    if float is greater than avg:
        add 1
        percent average = counter / len(scores)
"""
def strip_list():
    file = open("Final.txt", "r")
    scores = [line.rstrip()for line in file]
    file.close()
    return
    #     scores = [[float(i) for i in scores.strip().split(',')] for scores in filename]
strip_list()


def main():
    counter = 0
    scores = strip_list()
    print("Student Scores Are:", scores)
    avg = sum(scores) / len(scores)
    for i in scores:
        if float(i) > avg:
            counter += 1
            percent_avg = counter/len(scores)
    print("The class average is: ", avg)
    print("The number of students is:", len(scores))
    print("The percentage of the class above the average is:", percent_avg, "%")

main()


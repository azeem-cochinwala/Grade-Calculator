'''
Azeem Cochinwala

Program Description: 
    This program is a grade calculator, but not just any grade calculator. Its purpose is for use during the semester. 
    The input for the program will be a grade sheet style file. With the course name, followed by all the assessments with 
    their weights and the grades if they have been completed till date, and lastly the desired average the student wants
    for the course. As for the assessments that are yet to be completed, they are indicated with "no-grade" instead. 
    The grades are in fractional form and the weights are in percentages. 
    The program then calculates the student's current average in the course, and determines whether the desired average is 
    achievable. 
    If achievable, it will also display the minimum average (%) they need to get in total across the remaining assessments. 
    If not, it will output the highest average that can be achieved in the course. 
    This is a re-visitable program. The input file can be adjusted along the way to get updated results.
    
    The text in the input file should be in the following format (assessments with grades and without grades):
        Course <#>: <Name>
        <Assessment Name>: weight <#>%, grade <#>/<#>
        .
        .
        .
        <Assessment Name>: weight <#>%, no-grade <#>/<#>
        .
        .
        Desired average: <#>%
        --- 
    The three dashes must be placed after the last course data to indicate the end of the document. 
    Output values will be rounded to a maximum of 2 decimal places. 
        
''' 

'''
(1) Take in the input from the file
'''
#Opens the file and is ready to be read:
inputFile = open("cps109_a1_input.txt") 

'''
(2) Go through the file and collect all the data for each course
'''
def get_data(inputFile):
    #The list below will store all the "data" in the file:
    data = list() 
    courseIndex = -1
    #For loop below will iterate through the lines in the file:
    for line in inputFile: 
        #Conditional creates sections (sublists) within the list for each course and keeps track of the index:
        if "Course" in line: 
            data.append([line[:len(line)-1],[]])
            courseIndex += 1
        #For each course, when the line that indicates the desired average is found, the conditional adds the percent firgue to the list:
        if "Desired average" in line: 
            data[courseIndex].append(line[len("Desired average")+2:len(line)-1])
        #For all other lines, conditional makes a sublist with each element being the a copy of the line containing all the details:
        if "Course" not in line and "Desired average" not in line: 
            data[courseIndex][1].append(line[:len(line)-1])
    return data
data = get_data(inputFile)

'''
(3) Go through the assessments per course and calculate the average for the grades available, then determine whether the desired average is achievable
'''
#Function determines the percent value of a grade total represented in the fraction form: 
def grade_percent(string):
    numerator = 0
    denominator = 0
    fraction = string
    #For loop iterates through each letter:
    for letter in fraction:
        #Conditional finds the divisor sign and picks out the numerator and denominator:
        if letter == '/':
            indexF = fraction.index(letter)
            numerator = float(fraction[:indexF])
            denominator = float(fraction[indexF+1:])
    return numerator / denominator * 100

#Function determines whether the desired average is achievable based on the values determined in the result function:
def desire(sumOfScores, sumOfWeightsCompleted, course):
    desiredPercent = course[2]
    length = len(desiredPercent)
    desiredScore = float(desiredPercent[:length-1])
    weightsRemaining = 100 - sumOfWeightsCompleted
    requiredAverage = ((desiredScore - sumOfScores) / weightsRemaining) * 100
    if requiredAverage > 100:
        return "NOT achievable :(, maximum average possible is " + str(round((weightsRemaining + sumOfScores), 2)) + "% across the remaining " + str(weightsRemaining) + "%"
    if requiredAverage <= 100:
        return "achievable with a minimum average of " + str(round(requiredAverage, 2)) + "% across the remaining " + str(weightsRemaining) + "%" 

#The result function calculates the current average and calls upon the two functions above to return the final output (done per course that is passed). 
def result(course):
    assessmentWordList = list()
    gradesList = list()
    sumOfScores = 0
    sumOfWeightsCompleted = 0
    #For loop takes each line that represents an assessment, creates a sublist and then proceeds to split the line into individual words:
    for assessment in course[1]:
        assessmentWordList.append(assessment.split())
    
    #For loop iterates through each assessment line:
    for assessmentLine in assessmentWordList: 
        #For loop iterates through each word in the assessment list generated above:
        for word in assessmentLine:
            #Conditional determines the weight value, a number in string type, and converts it into a float:
            if word == 'weight' and "no-grade" not in assessmentLine:
                indexW = assessmentLine.index(word)
                weightPercent = assessmentLine[indexW+1]
                weightNumber = float(weightPercent[:len(weightPercent)-2]) / 100
                sumOfWeightsCompleted += weightNumber * 100
            #Conditional converts grade in str type to float, and reduces its value in terms of its weight in the course:
            if word == 'grade' and "no-grade" not in assessmentLine:
                indexG = assessmentLine.index(word)
                grade = (grade_percent(assessmentLine[indexG+1])) * (weightNumber)
                #Adds the weighted grade value to the grades list:
                gradesList.append(grade)
                
    #For loop adds up all the weighted grades per assessment to calculate the student's average across the completed assessments:
    for score in gradesList:
        sumOfScores += score
    #Creates the first output statement for the current average:
    output1 = "Current average in" + " " + str(course[0][:len(course[0])]) + " => " + str(round((sumOfScores / sumOfWeightsCompleted * 100), 2)) + '%'
    #Calls on the desire function and creates second output statement:
    output2 = "***Desired average of " + course[2] + " is " + desire(sumOfScores, sumOfWeightsCompleted, course) + "***"
    return  output1 + "\n" + output2

'''
(4) Create an output file displaying the results
'''
step = 0
outputFile = open("cps109_a1_output.txt", "w")
#While loop iterates through the courses in the data list, passes it into the result function:
while step < len(data):
    output = result(data[step])
    print(output)
    #Output is written per course to the output file:
    outputFile.write(output + "\n" + " " + "\n")
    step += 1
    
outputFile.close()
inputFile.close()

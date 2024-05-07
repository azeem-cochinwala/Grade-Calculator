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

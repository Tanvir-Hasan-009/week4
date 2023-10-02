score=float (input("Enter your score: "))
def calculate_the_grade(score):
    if score >=90:
       grade= "A"
    if score >= 90:
        grade='A'
    elif score >= 80:
        grade= 'B'
    elif score >= 70:
        grade= 'C'
    elif score >= 60:
        grade= 'D'
    else:
        score <60
        grade= 'F'
        
    if score <0:
        grade= 'error_Please input between 0 to 100'
    return grade

grade=calculate_the_grade(score)
print("Grade: ",grade)
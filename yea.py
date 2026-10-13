#===================================================================================
# Name: Thea Margaux M. Fernando
# Section: 8 - Sampaguita
# Hands on Activity: Student Performance Evaluator
#===================================================================================

# Local Variable
def display_header():
    header = "Student Performance Evaluator"
    print(header)

display_header()

# Global Variable
name = input("Enter your name:")
score1 = int(input("Enter assessment 1: "))
score2 = int(input("Enter assessment 2: "))
score3 = int(input("Enter assessment 3: "))

def get_student_info(name, score1, score2, score3):
    print(name, score1, score2, score3)

def evaluate_performance(average):
    average = score1 + score2 + score3 / 3
    print(average)
    if 100 <= average >= 90:
        print("Outstanding")
    elif 90 > average >= 85:
        print("Very Satisfactory")
    elif 85 > average >= 80:
        print("Satisfactory")
    elif 80 > average >= 75:
        print("Fairly Satisfactory")
    else:
        print("Needs improvement")

def display_report():
    print()
display_header()

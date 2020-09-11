#Author: Karthik Madhav Jain kmj5614@psu.edu

def getGradePoint(grade):
  global gradepoint
  if grade == 'A':
    gradepoint = 4.0
  elif grade == 'A-':
    gradepoint = 3.67
  elif grade == 'B+':
    gradepoint = 3.33
  elif grade == 'B':
    gradepoint = 3.0
  elif grade == 'B-':
    gradepoint = 2.67
  elif grade == 'C+':
    gradepoint = 2.33
  elif grade == 'C':
    gradepoint = 2.0
  elif grade == 'D':
    gradepoint = 1.0
  else: gradepoint = 0.0
  return (gradepoint)

def run():
  grade1 = input('Enter your course 1 letter grade: ')
  cc1 = input('Enter your course 1 credit: ')
  lg1 = getGradePoint(grade1)
  print(f"Grade point for course 1 is: {lg1}")
  
  grade2 = input('Enter your course 2 letter grade: ')
  cc2 = input('Enter your course 2 credit: ')
  lg2 = getGradePoint(grade2)
  print(f"Grade point for course 2 is: {lg2}")
  
  grade3 = input('Enter your course 3 letter grade: ')
  cc3 = input('Enter your course 3 credit: ')
  lg3 = getGradePoint(grade3)
  print(f"Grade point for course 3 is: {lg3}")
  
  gpa = (((lg1*cc1)+(lg2*cc2)+(lg3*cc3))/(cc1+cc2+cc3))
  print(f"Your GPA is: {gpa}")

if __name__=="__main__":
  run()
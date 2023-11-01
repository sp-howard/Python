if __name__ == '__main__':
    
    # https://www.hackerrank.com/challenges/nested-list/problem

    python_students = []

    # Create list of students and their scores    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        python_students.append([name, score])
        
    scores = []    

    # Create list of scores     
    for student in python_students:
        score = student[1]
        scores.append(score)
        
    scores.sort()
    
    low_score = scores[0]
    
    # Get the second lowest score
    for score in scores:
        if score > low_score:
            runner_up = score
            break
    
    runners_up = []        
    
    # Find all instances of the second lowest score, and get the associated student 
    for student in python_students:
        if student[1] == runner_up:
            runners_up.append(student[0])
    
    runners_up.sort()
    
    for name in runners_up:
        print(name)
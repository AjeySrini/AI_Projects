# Task 1 – Process the Scores
def process_scores(students):
    averages = {}
    
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
        
    return averages


# Task 2 – Classify the Grades
def classify_grades(averages):
    
    result = {}
    
    for name, avg in averages.items():
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"
            
        result[name] = (avg, grade)
        
    return result


# Task 3 – Generate the Report
def generate_report(classified, passing_avg=70):

    passed = 0
    failed = 0
    
    print("----- Student Grade Report -----")
    
    for name, (avg, grade) in classified.items():
        
        if avg >= passing_avg:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1
        
        print(f"{name} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")
    
    print("\n===============================")
    print("Total Students :", len(classified))
    print("Passed         :", passed)
    print("Failed         :", failed)
    
    return passed


if __name__ == "__main__":
    
    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62],
        "Clara": [95, 97, 96]
    }
    
    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
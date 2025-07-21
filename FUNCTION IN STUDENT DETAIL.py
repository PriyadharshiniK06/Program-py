def student_detail(student1_name,student1_regno,student1_dept,student2_name,student2_regno,student2_dept,Tamil1,Tamil2,English1,English2,Maths1,Maths2,Science1,Science2,social1,social2):
    print("The student 1 name is :",student1_name)
    print("The student 1 register no is:",student1_regno)
    print("The student 1 department is:",student1_dept)
    print("The student 2 name is :",student2_name)
    print("The student 2 register no is:",student2_regno)
    print("The student 2 department is:",student2_dept)
    print("1ST STUDENT DETAILS: ")
    Tamil1=int(input("Enter your tamil mark:  "))
    English1=int(input("Enter your english mark: "))
    Maths1=int(input("Enter your maths mark: "))
    Science1=int(input("Enter your science mark: "))
    Social1=int(input("Enter your social mark: "))
    print("2ND STUDENT DETAILS:")
    Tamil1=int(input("Enter your tamil mark:  "))
    English1=int(input("Enter your english mark: "))
    Maths1=int(input("Enter your maths mark: "))
    Science1=int(input("Enter your science mark: "))
    Social1=int(input("Enter your social mark: "))
    TOTAL=Tamil1+English1+Maths1+ Science1+ social1
    TOTAL2=Tamil2+English2+Maths2+ Science2+ social2
    PERCENTAGE=TOTAL/5
    PERCENTAGE2=TOTAL2/5
    if PERCENTAGE>PERCENTAGE2:
        print("Priya's mark is first")
    else:
        print("Rose's mark is first")
    
    
               
    
student_detail("Priya","23JI0456","CSE","Rose","23JI0789","CSE",65,78,67,78,89,76,56,67,78,78)

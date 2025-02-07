def avgscore(lst):
    n=len(lst[0][1])# no of subjects
    maxi=0
    stu=""
    failed=[]
    #print(n)
    for student in lst:
        name=student[0]
        scores=student[1]       
        sum=0
        for score in scores:
            sum+=score
                          
        avg=sum/n
       
        if(avg>maxi):
            maxi=avg
            stu=name
        if(avg<40):
            failed.append(name)
        print(name+"Average score:",round(avg,2))
    print("Top Scorer:"+stu+"with an average score of",maxi)
    if(len(failed)>0):
        print("Students who failed:",end="")
        for student in failed:
            print(student)

students=[("student_a",[80,90,85]),
          ("student_b",[45,30,50]),
          ("student_c",[90,95,85]),
          ("student_d",[20,35,25])
          ]
avgscore(students)
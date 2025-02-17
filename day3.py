# def avgscore(lst):
#     n=len(lst[0][1])# no of subjects
#     maxi=0
#     stu=""
#     failed=[]
#     #print(n)
#     for student in lst:
#         name=student[0]
#         scores=student[1]       
#         sum=0
#         for score in scores:
#             sum+=score
                          
#         avg=sum/n
       
#         if(avg>maxi):
#             maxi=avg
#             stu=name
#         if(avg<40):
#             failed.append(name)
#         print(name+"Average score:",round(avg,2))
#     print("Top Scorer:"+stu+"with an average score of",maxi)
#     if(len(failed)>0):
#         print("Students who failed:",end="")
#         for student in failed:
#             print(student)

# students=[("student_a",[80,90,85]),
#           ("student_b",[45,30,50]),
#           ("student_c",[90,95,85]),
#           ("student_d",[20,35,25] )
#           ]
# avgscore(students)
def avgscore(lst):
    n = len(lst[0][1])

    
    results = [(name, round(sum(scores) / n, 2)) for name, scores in lst]

    
    max_avg = max(results, key=lambda x: x[1])[1]

    
    top_scorers = [name for name, avg in results if avg == max_avg]
    failed = [name for name, avg in results if avg < 40]

    
    results.sort(key=lambda x: x[1], reverse=True)

    
    for res in results:
        print(res)

    print("\nTop Scorer:", top_scorers)
    print("Students who failed:", failed)

students = [
    ("student_a", [80, 90, 85]),
    ("student_b", [45, 30, 50]),
    ("student_c", [90, 95, 85]),
    ("student_d", [20, 35, 25])
]

avgscore(students)

#print("aa,bb,cc,dd".title())
#name = input("Enter names:").split(",")
#assignments = input("Enter the number of assignments:").split(",")
#assignments = [int(x) for x in assignments]
#grades = input("Enter grades:").split(",")
#grades = [int(x) for x in grades]
#
#massage = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
#submit before you can graduate. You're current grade is {} and can increase \
#to {} if you submit all assignments before the due date.\n\n"
#
#for i in range(len(name)):
#    print(massage.format(name[i],assignments[i],grades[i],grades[i]+2*assignments[i]))
    
name1 = list(input("Enter names separately by comma:").title().split(','))
assignments1 = list(input("Enter number of assignments:").split(','))
grades1 = list(input("Enter the grades:").split(','))
massage1 = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
for i,j,k in zip(name1, assignments1, grades1):
    print(massage1.format(i,j,k,int(k)+2*int(j)))


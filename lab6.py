Total = 0
print "How many numbers do you want to add together?"
user_Input = int(raw_input())
for x in range(user_Input):
    print 'Enter a number'
    num = int(raw_input())
    Total = Total + num
print "The answer is"
print Total

Total = []
print "How many numbers do you want to add together?"
user_Input = int(raw_input())
for x in range(user_Input):
    print 'Enter a number'
    num = int(raw_input())
    Total.append(num)
print "The answer is"
print sum(Total)

total = 1
print 'What number would you like to factorial'
num1 = int(raw_input())
#[0,1,2,3,4,5]
#[1,2,3,4,5,6]
for x in range(num1):
    total = total * x


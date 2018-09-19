'''
ABCXYZ company has up to employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

    It must contain at least uppercase English alphabet characters.
    It must contain at least digits ( - ).
    It should only contain alphanumeric characters ( - , - & - ).
    No character should repeat.
    There must be exactly characters in a valid UID.

Input Format

The first line contains an integer , the number of test cases.
The next lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354

Sample Output

Invalid
Valid

Explanation

B1CD102354: is repeating → Invalid
B1CDEF2354: Valid
'''
import string
A=[]
N = int(input())
for i in range(N):
    X = input()
    A.append(X)


for j in range(N):    
    check=0
    b=0
    a=0
    # for atleast two  uppercase alphabet
    if len(set(string.ascii_uppercase).intersection(str(A[j]))) >= 2 :
        check += 1
        
    #for atleast 3 digits
    if len(set(string.digits).intersection(str(A[j]))) >= 3 :
        check += 1;
        
    #for alphanumeric character 
    for i in str(A[j]):
        if (i.isalnum() == False):
            b += 1
    if (b==0):
        check += 1
        

    #for exactly 10 characters 
    if (len(str(A[j]))) == 10:
        check+= 1
        

    #for no character should repeat
    for i in str(A[j]):
        X = str(A[j]).count(i)
        if (X != 1):
            a += 1
            break
    if (a == 0):
        check += 1
        

    if check == 5:
        print('Valid')
    else:
        print('Invalid')


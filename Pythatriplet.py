#python program to generate Pythongorean triplet
n=int(input("Enter the max value for generating Pythogorean Triplet:"))
for a in range(1,n-1):
    for b in range(a+1,n):
        for c in range(b+1,n+1):
            if(a*a + b*b==c*c):
                print(a,b,c)
m=[None]*4
count,fail=0,0
print("Enter marks")
for i in range(len(m)):
    m[i]=int(input())
    if m[i]>=40:
        count+=1
    else:
        fail+=1
print(f'''Number of subjects passed:{count}\n
Number of subjects failed:{fail}''')

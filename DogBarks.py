# Problem question:
# Suppose > is a dog moving in left to right direction and < is a dog moving in right to left direction. Each dog barks once meet other dogs. 
# Write a Python code to count the number of barks for the following scenario.
# <<->--<--<-<

question=input("Enter Question (e.g., <<->--<--<-<):")
a=list(question)
count=0
b=0
for i in a:
    b=b+1
    if i == '>':
        l = len(a)-b
        for j in range (l):
            if a[j+b] == '<':
                count = count + 1
print(count*2)

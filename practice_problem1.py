#একটি লিস্টে ১০টি সংখ্যা আছে। যে সংখ্যাগুলো ৫ এর চেয়ে বড়, শুধু তাদের বর্গ করে নতুন লিস্ট বানাও।
numbers = [2, 7, 3, 9, 1, 4, 6, 8, 5, 10]
larlist=[]
anslist=[]
for i in numbers:
    if i>5:
        larlist.append(i)


for i in larlist:
    anslist.append(i**2)
    print(i,"squere",i*i)
print(anslist)

i=1;sum=0;
for i in range(1,501):
   if(i%5==0 and i%7!=0):
       sum=sum+i;
print("sum is:");
print(sum);
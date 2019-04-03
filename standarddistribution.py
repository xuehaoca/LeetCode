import numpy as np
import matplotlib.pyplot as plt

def straight(a):
    x = (a+12.4)/2.8
    re = 10**x
    return re
def straight2(a):
    x = (a+4.75)/0.15
    re = 10**x
    return re
mu = -1.594
sigma = 0.375
num = 16776880
count = 0
rand_data = np.random.normal(mu, sigma, num)

retention_time = []
weak_cell = 336
mu2 = -2.719
sigma2 = 1.8
num2 = 336
rand_data2 = np.random.normal(mu2, sigma2, num2)
#count, bins, ignored = plt.hist(rand_data, 30, normed=True)
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2)), linewidth=1, color='r')
#plt.show()

for each in rand_data:
    #count +=1
    #print each
    #print "\n"

    retention_time.append((10**each)*1000)
for each in rand_data2:
    #count +=1
    #print each
    #print "\n"
    retention_time.append((10**each)*1000)  
np.random.shuffle(retention_time)
f = open("data.txt","w")
for each in retention_time:
    new = str(each)
    new2 = new[0:5]
    f.writelines(new2+"\n")
yx=[]
a1=a2=a3=a4=a5=a6=a7=a8=a9=a10=a11=a12=a13=a14=a15=a16=a17=a18=a19=a20=a21=a22=a23=a24=a0=0
for each in retention_time:
    if each >0 and each <= 2.5:
        a0 +=1
    if each >2.5 and each <= 5:
        a1 +=1
    if each >5 and each <=7.5 :
        a2 +=1
    if each >7.5 and each <= 10:
        a3 +=1
    if each >10 and each <= 12.5:
        a4 +=1
    if each >12.5 and each <= 15:
        a5 +=1 
    if each >15 and each <= 17.5:
        a6 +=1
    if each >17.5 and each <= 20:
        a7 +=1
    if each >20 and each <= 22.5:
        a8 +=1
    if each >22.5 and each <= 25:
        a9 +=1
    if each >25 and each <= 27.5:
        a10 +=1
    if each >27.5 and each <= 30:
        a11 +=1
    if each >30 and each <= 32.5:
        a12 +=1
    if each >32.5 and each <= 35:
        a13 +=1
    if each >35 and each <= 37.5:
        a14 +=1
    if each >37.5 and each <= 40:
        a15 +=1
    if each >40 and each <= 42.5:
        a16 +=1
    if each >42.5 and each <= 45:
        a17 +=1
    if each >45 and each <= 47.5:
        a18 +=1
    if each >47.5 and each <= 50:
        a19 +=1
    if each >50 and each <= 52.5:
        a20 +=1
    if each >52.5 and each <= 55:
        a21 +=1
    if each >55 and each <= 57.5:
        a22 +=1
    if each >57.5 and each <= 60:
        a23 +=1
    if each >60 and each <= 62.5:
        a24 +=1
yx.append(a0)
yx.append(a1)
yx.append(a2)
yx.append(a3)
yx.append(a4)
yx.append(a5)
yx.append(a6)
yx.append(a7)
yx.append(a8)
yx.append(a9)
yx.append(a10)
yx.append(a11)
yx.append(a12)
yx.append(a13)
yx.append(a14)
yx.append(a15)
yx.append(a16)
yx.append(a17)
yx.append(a18)
yx.append(a19)
yx.append(a20)
yx.append(a21)
yx.append(a22)
yx.append(a23)
yx.append(a24)
x = np.arange(0,65,2.6)
print x
y = yx
print y
plt.bar(x, y, color="r")
plt.xlabel("Retention_Time(ms)")
plt.ylabel("Number of Cells")

plt.show()
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

    retention_time.append(straight(each)/1000)
for each in rand_data2:
    #count +=1
    #print each
    #print "\n"
    retention_time.append(straight2(each)/1000)  
np.random.shuffle(retention_time)
a0=a1=a3=a2=a4=a5=a6=0
yx=[]
for each in retention_time:
    if each >0 and each < 2:
        a0 +=1
    if each >=2 and each < 5:
        a1 +=1
    if each >=5 and each < 10:
        a2 +=1
    if each >=10 and each < 15:
        a3 +=1
    if each >=15 and each < 20:
        a4 +=1
    if each >=20 and each < 25:
        a5 +=1 
    if each >=25 and each <= 30:
        a6 +=1
yx.append(a0)
yx.append(a1)
yx.append(a2)
yx.append(a3)
yx.append(a4)
yx.append(a5)
yx.append(a6)
x = np.arange(0,31,5)
print x
y = yx
print y
plt.bar(x, y, color="r")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
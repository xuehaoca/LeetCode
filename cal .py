#last modified by erhei
#if you want to draw a pitcure of the data, you can use python package(recommend)
# or you can adjust the output form and copy it to the excel app

def openfile(filename,dicc):
    writeenergy = open("energy.txt","wb") #energy.txt is the original data extracted from stats.txt
    file1 = open(filename) #open the energy.txt
    sum = 0 #sum saves the total energy for each benchmark
    index = 0 # index is the index of the dictionary for operation's energy consumption
    #######################################
    alist=[]
    blist=[]
    while 1: 
        line = file1.readline() #read each line in the txt file
        if not line:  # write the final data when the txt is at an end
            if sum != 0:
                #sum = sum + 2277555.2
                blist.append(str(sum)+"\n")
            break
        arr = line.split() # split the line with "space".   arr is a list
       # print sum
        if(len(arr)==1):   # when the line is a name for benchmark, write it to the result file
            if sum != 0:
               # sum = sum + 2277555.2
                blist.append(str(sum)+"\n")
            alist.append(line)
            sum = 0
            index = 0
        else:             
            print arr[1]
            if len(arr[1]) >= 2 and arr[1][1] == '.':
                #e1 = 1
                #print arr[1][0]
                #new = arr[1][2:]
                e1 = float(arr[1])
            elif len(arr[1]) >= 3 and arr[1][2] == '.':
                #e1 = 1
                #print arr[1][0]
                #new = arr[1][3:]
                e1 = float(arr[1])
            else:
                e1 = int(arr[1])
            # when the line is energy consumption data, calculate it
             # the number of hit or miss
            #print e1
            e2 = dicc[index]# the energy consumption of hit or miss which is already saved in the dictionary
            sum = sum + e1 * e2
            index = index + 1
            #print e1,e2,sum
            #print dicc[index]   
    #######################################
    for letter in alist:
        writeenergy.write(letter)
    #print blist
    for letter2 in blist:
        writeenergy.write(letter2)
dd = {0:15877902000,1:0.479,2:0.233,3:0.479,4:0.479,5:0.479,6:2.172045898}# dictionary saves energy consumption
openfile("test.txt",dd)

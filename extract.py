################################
#last modified by erhei
#this is a file to extract useful data from stats.txt
#set your rootDir to the file directory containning all benchmarks

import os
def test(rootDir):
    list_dirs = os.walk(rootDir) #get all file information using existing function
    file22 = open("test.txt","wb") #output file
    for root, dirs, files in list_dirs: #access all files in the directory
        for d in dirs:
            if d.split(".")[0] == "2006":  #find the correct benchmark dir
                    newlist = os.walk(os.path.join(rootDir,d))
                    for root1,dir2,file2 in newlist: # get in one specific benchmark dir
                        flag = True
                        for each2 in file2:       #find stats.txt
                            #print 2
                            if each2 == "stats.txt":
                                file3 = open(os.path.join(os.path.join(rootDir,d),each2))
                                while(1):           #find the useful line in stats.txt
                                    line = file3.readline()
                                    if not line:
                                        break
                                    arr = line.split("# ")
                                    arr11 = line.split(" ")
                                    if(flag == True):
                                        file22.write(d)
                                        file22.write("\n")
                                        flag = False
                                    #print arr
                                    #print arr11[0]
                                    if arr[-1] == "number of ReadReq hits\n":
                                        
                                        arr2 = arr[0]
                                        arr22 = arr2.split()
                                        arr3 = arr22[0][-5:]
                                        #print arr22,arr3
                                        if arr3 == "total":
                                            arr4 = arr2.split(".")[1]
                                            if arr4 == "l3":
                                            #print arr4
                                                file22.write(line)
                                    elif arr[-1] == "number of Writeback hits\n":
                                        arr2 = arr[0]
                                        arr22 = arr2.split()
                                        arr3 = arr22[0][-5:]
                                        #print arr22,arr3
                                        if arr3 == "total":
                                            arr4 = arr2.split(".")[1]
                                            if arr4 == "l3":
                                            #print arr4
                                                file22.write(line)
                                    elif arr[-1] == "number of ReadExReq hits\n":
                                        
                                        arr2 = arr[0]
                                        arr22 = arr2.split()
                                        arr3 = arr22[0][-5:]
                                        #print arr22,arr3
                                        if arr3 == "total":
                                            arr4 = arr2.split(".")[1]
                                            if arr4 == "l3":
                                            #print arr4
                                                file22.write(line)
                                    elif arr[-1] == "number of ReadExReq misses\n":
                                        
                                        arr2 = arr[0]
                                        arr22 = arr2.split()
                                        arr3 = arr22[0][-5:]
                                        #print arr22,arr3
                                        if arr3 == "total":
                                            arr4 = arr2.split(".")[1]
                                            if arr4 == "l3":
                                            #print arr4
                                                file22.write(line)
                                    elif arr[-1] == "number of ReadReq misses\n":
                                        
                                        arr2 = arr[0]
                                        arr22 = arr2.split()
                                        arr3 = arr22[0][-5:]
                                        #print arr22,arr3
                                        if arr3 == "total":
                                            arr4 = arr2.split(".")[1]
                                            if arr4 == "l3":
                                            #print arr4
                                                file22.write(line)
                                    elif arr[-1] == "Number of seconds simulated\n":
                                        
                                        arr2 = arr[0]
                                        arr22 = arr2.split()
                                        file22.write(line)
                                    elif arr[-1] == "number of refresh operations\n":
                                        
                                        arr2 = arr[0]
                                        arr22 = arr2.split()
                                        arr4 = arr2.split(".")[1]
                                        if arr4 == "l3":
                                            #print arr4
                                            file22.write(line)
                                    elif arr11[0] == "sim_seconds":
                                        file22.write(line)
                                    elif arr11[0] == "sim_insts":
                                        file22.write(line)
                                    elif arr11[0] == "system.l3.overall_misses::total":
                                        file22.write(line)
if __name__ == "__main__":
    test("/home/wang/parameter_40/ctrlsize/512_32_32_8_32_2_1_128_2/512_32_32_8_32_2_1_128_2")
    #test("/Users/xuehao/klab_gem5/test/results")

 # -*- coding: utf-8 -*-
import os
result = open("dataset.txt","w")
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
tar = "stats.txt"
dir="/Users/xuehao/klab_gem5/newgem/test/results"
dir2 = os.listdir(dir)
for each in dir2:
        newdir = dir + "/"+each
        
        dir3 = newdir+"/"+tar
        f = open(dir3,"r")
        a = f.readlines()
        if(len(a)>50):
                list1.append(each)
                count = 0 
                for each2 in a:
                        each3 = each2.split()
                        if(len(each3)>2):
                                if(each3[0] == "system.l3.tags.hitsleft"):
                                        #result.write("left")
                                        #result.write(each3[1])
                                        list2.append(each3[1])
                                        count = count + 1
                                if(each3[0] == "system.l3.tags.hitsright"):
                                        #result.write("right")
                                        #result.write(each3[1])
                                        list3.append(each3[1])
                                        count = count + 1
                                if(each3[0] == "sim_seconds"):
                                        #result.write("left")
                                        #result.write(each3[1])
                                        list4.append(each3[1])
                                        count = count + 1
                                if(each3[0] == "system.l3.overall_miss_latency::total"):
                                        #result.write("left")
                                        #result.write(each3[1])
                                        list5.append(each3[1])
                                        count = count + 1

                                if(count == 4):
                                        break


for each in list1:
        result.write(each)
        result.write("\n")
result.write("left")
result.write("\n")
for each in list2:
        result.write(each)
        result.write("\n")
result.write("right")
result.write("\n")
for each in list3:
        result.write(each)
        result.write("\n")
result.write("sim_seconds")
result.write("\n")
for each in list4:
        result.write(each)
        result.write("\n")
result.write("overall_misslatency")
result.write("\n")
for each in list5:
        result.write(each)
        result.write("\n")
        
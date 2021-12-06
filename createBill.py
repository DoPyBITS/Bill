"""
Generates the bill given the input folder and the photobooth folder.

The photo prices are hardcoded.
"""
import os, os.path, csv, re

inputFolder = "/home/favre49/Documents/Oasis"
photobooth = "/home/favre49/Documents/OasisPhotobooth"

sufile = csv.reader(open('SULIST - Copy.csv', 'rU'), dialect=csv.excel_tab) # The SU student list
lines = list(sufile)
billList = []

for dirName in os.listdir(inputFolder):
    subdirName=inputFolder + "/" + dirName
    if os.path.isdir(subdirName):
        for pic in os.listdir(subdirName):
            print(pic)
            id = re.split("[_.]", pic)[-2]
            if id.find('M')!=-1:
                id = id[1:]
            print(id)
            room = re.split("[_.]", pic)[0]+re.split("[_.]", pic)[1]
            name = ""
            for row in lines:
                if id==re.split("[,]",row[0])[1][2:4]+re.split("[,]",row[0])[1][-4:]:
                    idx = re.split("[,]",row[0])[1]
                    if idx.find('H')!=-1 or idx.find("PH")!=-1:
                        if not room == re.split("[,]",row[0])[4]+re.split("[,]",row[0])[5]:
                            continue
                    id = idx
                    name = re.split("[,]",row[0])[2]
                    break
            flag = 0
            for row in billList:
                if row[0] == id:
                    row[2]=row[2]+1
                    row[4]=row[4]+12
                    flag = 1
                    break
            if not flag and name!="":
                billList.append([id,name,1,0,12])

for dirName in os.listdir(photobooth):
    subdirName=photobooth + "/" + dirName
    if os.path.isdir(subdirName):
        for pic in os.listdir(subdirName):
            print(pic)
            id = re.split("[_.]", pic)[-2]
            if id.find('M')!=-1 or id.find('P')!=-1:
                id = id[1:]
            print(id)
            room = re.split("[_.]", pic)[0]+re.split("[_.]", pic)[1]
            print(room)
            name = ""
            for row in lines:
                if id==re.split("[,]",row[0])[1][2:4]+re.split("[,]",row[0])[1][-4:]:
                    idx = re.split("[,]",row[0])[1]
                    if idx.find('H')!=-1 or idx.find("PH")!=-1:
                        if not room == re.split("[,]",row[0])[4]+re.split("[,]",row[0])[5]:
                            continue
                    id = idx
                    name = re.split("[,]",row[0])[2]
                    break
            flag = 0
            for row in billList:
                if row[0] == id:
                    row[3]=row[3]+1
                    row[4]=row[4]+30
                    flag = 1
                    break
            if not flag and name!="":
                billList.append([id,name,0,1,30])

biller = csv.writer(open('bill.csv', 'w'))
biller.writerows(billList)
                

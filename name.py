import os

filePath = r'C:\Users\yinmo\Desktop\lunchbox\xml'
name = os.listdir(filePath)
print(name)
for item in name:
    f = open('C:\\Users\\yinmo\\Desktop\\lunchbox\\train.txt', 'a')

    f.writelines(['\n', str(item[:-4])])

f.close()
# print(item[:-5])

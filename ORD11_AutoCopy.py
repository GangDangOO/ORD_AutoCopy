import os
import clipboard

user = os.path.expanduser('~')
isDir = os.path.join(user, 'OneDrive', 'Documents', 'Warcraft III', 'CustomMapData', 'ORD11')
if os.path.isdir(isDir):
    dir = os.path.join(user, 'OneDrive', 'Documents', 'Warcraft III', 'CustomMapData', 'ORD11')
else:
    dir = os.path.join(user, 'Documents', 'Warcraft III', 'CustomMapData', 'ORD11')
os.chdir(dir)
print(os.getcwd())

file_list = os.listdir()
file_list.sort(key=os.path.getctime, reverse=True)
print(file_list)
file = open(file_list[0], 'r', encoding='UTF-8')

i = 0;
while True:
    file.readline()
    if i == 4:
        break
    i += 1
    
write = file.readline()
s = write.split("\"")
code = s[1]
print(code)
clipboard.copy(code)
file.close()

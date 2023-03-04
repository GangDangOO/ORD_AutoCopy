import os
import clipboard

user = os.path.expanduser('~')
local_txt = open("ordLocal.txt", 'r')
temp = local_txt.read()
local = temp.split("\"")
os.chdir(local[1])

file_list = os.listdir()
file_list.sort(key=os.path.getctime, reverse=True)
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

immutable_var=1,2,3,'F',[0,9,8,7]
print(immutable_var)
#immutable_var[2]=200 кортежи изменять нельзя
#print(immutable_var)
#Traceback (most recent call last):
# File "D:\Projects Inna\pythonProject1\.venv\module_1_5.py", line 3, in <module>
#   immutable_var[2]=200
#   ~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
muttable_list=["Петр","мышка","F",1]
print(muttable_list)
muttable_list[0]="персик"
muttable_list[-1]="апельсин"
print(muttable_list)
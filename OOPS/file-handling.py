# FILE HANDLING===>
# TYPES OF FILES====>
# 1.TEXT FILES==>String type data stored in it==>(.txt .pdf .doc)
# 2.Binary File===>(byte-strem)list,dict,tuple,set===>(.bin, .exe )
# 3.CSV File==>key value formate===>.csv
# FILE METHODS===>
# 1.open()
# Syntax=>open('file-with-extension','mode')

# f=open('n4.txt','x')  # x==> for creating file
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# f=open('n5.txt','w')  # w==> for writeing  file
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# f=open('n2.txt','r')  # r==> for reading existing  file
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

# 2.read/write()

#   1.write()=>single-line- data
# f=open('P2.txt','a')
# data='this is python class'
# f.write(data)
# f.close()

f=open('P2.text','a')
data="hello\n kartikey\n malviya"
f.writelines(data)
f.close()
# 3.close()

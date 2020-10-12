#obj = open("C:\A.txt",'r')

# print(obj.read())

# print(obj.readline())

# print(obj.read(5))

# for i in obj.read():
#     print(i)

# s = obj.readable()
# while(s):
#     print(s)
#    s = obj.readline()

obj = open("C:\A.txt",'w')
obj.write("Hello this is a new data")
obj.close()
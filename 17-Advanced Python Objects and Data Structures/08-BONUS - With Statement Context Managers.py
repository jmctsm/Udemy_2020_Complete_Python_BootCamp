#p = open('oops.txt', 'a')
#p.write('add more text')
##p.readlines()
#p.close()

#p = open('oops.txt', 'a')
#try:
#    p.readlines()
#except:
#    print("An exception was raised!")
#finally:
#    p.close()
#p.write('add more text')

with open('oops.txt', 'a') as p:
    p.readlines()

p.write('add more text')
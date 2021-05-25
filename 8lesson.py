import random
#print (random.random())
#for integer ranint and randrange
#print("printing random integer",random.randint(0,9))
#print("printing random integer",random.randrange(0,9,2))
#random.choice
"""name=["kaung","myat","thu","kMt"]
print("Selet element ",random.choice(name))"""
'''name=["kaung","myat","thu","kMt"]
print("Selet element ",random.sample(name,2))'''
'''random.seed(9)
print("random number from seed()",random.random())'''
'''name=["kaung","myat","thu","kMt"]
print("before shuffle",name)
random.shuffle(name)
print("After shuffle",name)'''
print("uniform",random.triangular(0.1,0.9,1.1))


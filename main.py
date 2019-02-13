from dog import Dog

d1 = Dog('fido', 3, 'male')
d2 = Dog('sally', 5, 'female')

#dogs = [d1, d2]
#dogdict = {d1.name: d1, d2.name: d2}

print('Before - ', d1.name, d1.weight)
d1.eat()
print('After eating -',  d1.name, d1.weight)
d1.play()
print('After playing -',  d1.name, d1.weight)

darray = []
avgage = 0

with open('dogs.txt') as f:
    for line in f:
        dogs = line.strip().split(',')
        print(dogs)
        d1 = Dog(dogs[0],int(dogs[1]),dogs[2])
        darray.append(d1)
        print(len(darray))
        avgage += d1.age

avgage = avgage/len(darray)
result = 0
for d in darray:
    result += (avgage - d.age)**2

print(result)
variance = result**0.5
stddev = variance**0.5
print('avg age - ', avgage)
print('std dev - ', stddev)


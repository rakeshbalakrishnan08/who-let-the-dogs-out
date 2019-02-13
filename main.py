from dog import Dog
from statistics import standard_deviation

dogs = []
with open('dogs.txt') as f:
    for line in f:
        name, age, sex = line.strip().split(',')
        age = float(age)
        dog = Dog(name, age, sex)
        dogs.append(dog)

ages = [dog.age for dog in dogs]
avgage = sum(ages) / len(ages)
stdage = standard_deviation(ages)
print(dogs, avgage, stdage)

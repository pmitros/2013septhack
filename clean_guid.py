# ~6000 users
# ~800 courses

import csv, itertools, random

last_names = open("names/names/dist.all.last").readlines()
first_names = open("names/names/dist.male.first").readlines()+open("names/names/dist.female.first").readlines()
names = itertools.product(first_names, last_names)
names = random.shuffle(names)
print len(names)

users = {}
courses = {}


with open('SakaiEvents.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        pass

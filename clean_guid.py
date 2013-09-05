# ~6000 users
# ~800 courses

import csv, itertools, random, os.path

if os.path.exists("names.txt"):
    n = open("names.txt").readlines()
else:
    import names
    n = set()
    while len(n) < 6000:
        n.add(names.get_full_name())
    n = list(n)
    random.shuffle(n)
    f = open("names.txt","w")
    f.writelines(n)
    f.close()

universities = ["MIT", "Harvard", "Berkeley", "Stanford", "IIT", "Udacity", "Kaplan"]
prefixes = ["Introductory", "Advanced", "Seminar on", "Quantum"]
courses = ["Chemistry", "Physics", "Biology", "Informatics", "Computation", "Poetry", "Philosophy", "Agriculture"]
suffixes = ["", "for Dummies", "for Inner City Youth", "On-Line Edition", "with Applications", "with Honors"]

n = itertools.product()
random.shuffle(n)

with open('../SakaiEvents.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        pass

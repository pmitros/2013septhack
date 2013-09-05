# ~6000 users
# ~1500 courses

import csv, itertools, random, os.path

if os.path.exists("names.txt"):
    with open("names.txt") as f:
        student_names = (item.strip() for item in f.readlines())
else:
    import names
    student_names = set()
    while len(student_names) < 6000:
        student_names.add(names.get_full_name())
    student_names = list(student_names)
    random.shuffle(student_names)
    with open("names.txt", "w") as f:
        f.writelines(item + "\n" for item in student_names)

def generate_course_name():
    universities = ["MIT", "Harvard", "Berkeley", "Stanford", "IIT", "Udacity", "Kaplan"]
    prefixes = ["Introductory", "Advanced", "Seminar on", "Quantum"]
    courses = ["Chemistry", "Physics", "Biology", "Informatics", "Computation", "Poetry", "Philosophy", "Agriculture"]
    suffixes = ["", "for Dummies", "for Inner City Youth", "On-Line Edition", "with Applications", "with Honors", "for the Determined"]

    n = list(itertools.product(universities, prefixes, courses, suffixes))
    random.shuffle(n)
    
    for item in n:
        yield " ".join(item)


student_generator = iter(student_names)
course_generator = generate_course_name()

user_names = {}
course_names = {}

with open("../SakaiEvents.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    first_row = reader.next()
    print "{},{},{},{}".format(*first_row)
    for row in reader:
        user = user_names.setdefault(row[0], student_generator.next())
        course = course_names.setdefault(row[3], course_generator.next())
        print "{},{},{},{}".format(user, row[1], row[2], course)

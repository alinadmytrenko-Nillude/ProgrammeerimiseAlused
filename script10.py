class Student:  # Klass õpilase jaoks
    def __init__(self, name, age, grade):  # Konstruktor: nimi, vanus, hinne (0–100)
        self.name = name  # Salvestame nime
        self.age = age  # Salvestame vanuse
        self.grade = grade  # Salvestame hinde

    def get_grade(self):  # Getter-meetod hinde jaoks
        return self.grade  # Tagastame õpilase hinde


class Course:  # Klass kursuse jaoks
    def __init__(self, name, max_students):  # Konstruktor: kursuse nimi ja max õpilaste arv
        self.name = name  # Kursuse nimi
        self.max_students = max_students  # Maksimaalne õpilaste arv
        self.students = []  # Tühi list kõigi kursusel olevate õpilaste jaoks

    def add_student(self, student):  # Meetod uue õpilase lisamiseks
        if len(self.students) < self.max_students:  # Kontrollime, kas on veel vabu kohti
            self.students.append(student)  # Lisame õpilase listi
            return True  # Tagastame True – lisamine õnnestus
        return False  # Tagastame False – kursus on täis

    def get_average_grade(self):  # Meetod kursuse keskmise hinde arvutamiseks
        if len(self.students) == 0:  # Kui kursusel pole ühtegi õpilast
            return 0  # Tagastame 0 (või võid visata vea)

        value = 0  # Algväärtustame summa
        for student in self.students:  # Käime läbi kõik õpilased
            value += student.get_grade()  # Liidame nende hinded kokku

        return value / len(self.students)  # Tagastame keskmise

# Loome õpilased
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

# Loome kursuse – nimi "Science", maksimaalselt 2 õpilast
course = Course("Science", 2)

# Lisame õpilasi kursusele
print(course.add_student(s1))  # True  → Tim lisati
print(course.add_student(s2))  # True  → Bill lisati
print(course.add_student(s3))  # False → Jill ei mahu, sest max on 2

# Arvutame ja väljastame keskmise hinde
print(course.get_average_grade())  # (95 + 75) / 2 = 85.0
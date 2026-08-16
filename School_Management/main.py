from school import School
from person import Student,Teacher
from subject import Subject
from classroom import ClassRoom

school = School('Abc School','Gulsan')

eight = ClassRoom('Eight')
nine = ClassRoom('Nine')
ten = ClassRoom('Ten')

# adding classroom
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding student 
rahim = Student('Rahim Khan',eight)
karim = Student('Karim Ahmed',nine)
abdulla = Student('Abdulla Jaber',ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(abdulla)

# adding teacher 
basar = Teacher('Bashar Mia')
monir = Teacher('Mango Monir')
taher = Teacher('Abu Taher')

school.add_teacher('Bangla',taher)
school.add_teacher('Math',basar)
school.add_teacher('English',monir)

# adding Subjects
bangla = Subject('Bangla',taher)
math = Subject('Math',basar)
physics = Subject('Physics',basar)
english = Subject('English',monir)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(math)
nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(math)
ten.add_subject(physics)

eight.semester_final_exam()
nine.semester_final_exam()
ten.semester_final_exam()

print(school)
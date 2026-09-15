class student:
  def __init__(self, sub, college, year):
    self.sub = sub
    self.college = college
    self.year = year
stu1 = student("python", "ABC", "3rd year")
stu2 = student("java", "XYZ", "2nd year")
print(stu1.sub, stu1.college, stu1.year)
print(stu2.sub, stu2.college, stu2.year)
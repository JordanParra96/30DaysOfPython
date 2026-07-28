"""Day 21: 30 Days of python programming"""


# Example of a class
class Person:
    """A class to represent a person."""

    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name


p = Person("Asabeneh")
print(p.name)
print(p)


class PersonwithDetails:
    """A class to represent a person with details."""

    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = PersonwithDetails("Asabeneh", "Yetayeh", 250, "Finland", "Helsinki")
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)


# Example of a class with methods
class PersonWithMethods:
    """A class to represent a person with methods."""

    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        """Return a string with the person's information."""
        return (
            f"{self.firstname} {self.lastname} is {self.age} years old. "
            f"He lives in {self.city}, {self.country}"
        )


p = PersonWithMethods("Asabeneh", "Yetayeh", 250, "Finland", "Helsinki")
print(p.person_info())


# Example of a class with default values
class PersonWithDefaultValues:
    """A class to represent a person with default values."""

    def __init__(
        self,
        firstname="Asabeneh",
        lastname="Yetayeh",
        age=250,
        country="Finland",
        city="Helsinki",
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        """Return a string with the person's information."""
        return {
            f"{self.firstname} {self.lastname} is {self.age} years old. "
            f"He lives in {self.city}, {self.country}."
        }


p1 = PersonWithDefaultValues()
print(p1.person_info())
p2 = PersonWithDefaultValues("John", "Doe", 30, "Nomanland", "Noman city")
print(p2.person_info())


# Example of a class with method to modify attributes
class PersonWithSkills:
    """A class to represent a person with skills."""

    def __init__(
        self,
        firstname="Asabeneh",
        lastname="Yetayeh",
        age=250,
        country="Finland",
        city="Helsinki",
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        """Return a string with the person's information."""
        return {
            f"{self.firstname} {self.lastname} is {self.age} years old. "
            f"He lives in {self.city}, {self.country}."
        }

    def add_skill(self, skill):
        """Add a skill to the person's skills list."""
        self.skills.append(skill)


p1 = PersonWithSkills()
print(p1.person_info())
p1.add_skill("HTML")
p1.add_skill("CSS")
p1.add_skill("JavaScript")
p2 = PersonWithSkills("John", "Doe", 30, "Nomanland", "Noman city")
print(p2.person_info())
print(p1.skills)
print(p2.skills)


# Example of inheritance
class Student(PersonWithSkills):
    """A class to represent a student, inheriting from PersonWithSkills."""


s1 = Student("Eyob", "Yetayeh", 30, "Finland", "Helsinki")
s2 = Student("Lidiya", "Teklemariam", 28, "Finland", "Espoo")
print(s1.person_info())
s1.add_skill("JavaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)

print(s2.person_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Marketing")
print(s2.skills)


# Example of overriding methods
class StudentWithGender(PersonWithSkills):
    """A class to represent a student with gender, inheriting from PersonWithSkills."""

    def __init__(
        self,
        firstname="Asabeneh",
        lastname="Yetayeh",
        age=250,
        country="Finland",
        city="Helsinki",
        gender="male",
    ):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = "He" if self.gender == "male" else "She"
        return {
            f"{self.firstname} {self.lastname} is {self.age} years old. "
            f"{gender} lives in {self.city}, {self.country}."
        }


s1 = StudentWithGender("Eyob", "Yetayeh", 30, "Finland", "Helsinki", "male")
s2 = StudentWithGender("Lidiya", "Teklemariam", 28, "Finland", "Espoo", "female")
print(s1.person_info())
s1.add_skill("JavaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)

print(s2.person_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Marketing")
print(s2.skills)

"""Day 21: 30 Days of python programming"""

from collections import Counter

# These classes intentionally have few public methods; they build up
# incrementally to illustrate class concepts one at a time.
# pylint: disable=too-few-public-methods


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

    # Extra "gender" argument on top of the inherited ones is intentional,
    # to show overriding a parent method with additional state.
    # pylint: disable-next=too-many-arguments,too-many-positional-arguments
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


# Level 1, exercise 1
class Statistics:
    """A class to calculate central tendency and variability measures of a sample."""

    def __init__(self, sample):
        self.data = sample

    def count(self):
        """Return the number of items in the sample."""
        return len(self.data)

    def sum(self):
        """Return the sum of the sample."""
        return sum(self.data)

    def min(self):
        """Return the smallest value in the sample."""
        return min(self.data)

    def max(self):
        """Return the largest value in the sample."""
        return max(self.data)

    def range(self):
        """Return the difference between the largest and smallest values."""
        return self.max() - self.min()

    def mean(self):
        """Return the average of the sample, rounded to the nearest integer."""
        return round(self.sum() / self.count())

    def median(self):
        """Return the middle value of the sorted sample."""
        sorted_data = sorted(self.data)
        mid = self.count() // 2
        if self.count() % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(self):
        """Return the most frequent value and how many times it occurs."""
        counts = Counter(self.data)
        max_count = max(counts.values())
        mode_value = next(
            value for value, count in counts.items() if count == max_count
        )
        return {"mode": mode_value, "count": max_count}

    def var(self):
        """Return the population variance of the sample, rounded to 1 decimal."""
        mean = self.sum() / self.count()
        squared_diffs = sum((value - mean) ** 2 for value in self.data)
        return round(squared_diffs / self.count(), 1)

    def std(self):
        """Return the population standard deviation, rounded to 1 decimal."""
        return round(self.var() ** 0.5, 1)

    def freq_dist(self):
        """Return (percentage, value) pairs sorted by frequency, then value, descending."""
        counts = Counter(self.data)
        distribution = sorted(counts.items(), key=lambda item: (-item[1], -item[0]))
        return [
            (round(count / self.count() * 100, 2), value)
            for value, count in distribution
        ]

    def describe(self):
        """Return a summary of all the statistical measures."""
        return (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {self.mean()}\n"
            f"Median: {self.median()}\n"
            f"Mode: {self.mode()}\n"
            f"Variance: {self.var()}\n"
            f"Standard Deviation: {self.std()}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )


ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]
data = Statistics(ages)
print("Count:", data.count())
print("Sum:", data.sum())
print("Min:", data.min())
print("Max:", data.max())
print("Range:", data.range())
print("Mean:", data.mean())
print("Median:", data.median())
print("Mode:", data.mode())
print("Standard Deviation:", data.std())
print("Variance:", data.var())
print("Frequency Distribution:", data.freq_dist())
print(data.describe())


# Level 2, exercise 1
class PersonAccount:
    """A class to represent a person's account with income and expenses."""

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description=""):
        """Add an income entry."""
        self.incomes.append({"amount": amount, "description": description})

    def add_expense(self, amount, description=""):
        """Add an expense entry."""
        self.expenses.append({"amount": amount, "description": description})

    def total_income(self):
        """Return the total income."""
        return sum(income["amount"] for income in self.incomes)

    def total_expense(self):
        """Return the total expense."""
        return sum(expense["amount"] for expense in self.expenses)

    def account_balance(self):
        """Return the account balance (total income - total expense)."""
        return self.total_income() - self.total_expense()

    def account_info(self):
        """Return a summary of the account information."""
        return {
            "Name": f"{self.firstname} {self.lastname}",
            "Total Income": self.total_income(),
            "Total Expense": self.total_expense(),
            "Account Balance": self.account_balance(),
            "Incomes": self.incomes,
            "Expenses": self.expenses,
        }

import random

class AthleteDetails:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def idx(self):
        y = self.height - self.weight + 10
        if y <= self.weight + 10:
            print("Your weight index is not normal")
        else:
            print("Your weight index is normal")


class HealthRecords:
    def __init__(self, test_results):
        self.test_results = test_results

    def get_health_results(self):
        return self.test_results


class FinancialDetails:
    def __init__(self):
        self.salary = 0
        self.bank_info = "4444 5555 6666 7777"

    def calculate_salary(self):
        self.salary = int(random.random() * 1000 + 4000)
        return self.salary

    def get_salary_with_taxes(self):
        return int(0.805 * self.salary)

    def get_bank_info(self):
        return self.bank_info


class Human:
    def __init__(self, name, age, height, weight, health_results, output_file):
        self.name = name
        self.athletics = AthleteDetails(age, height, weight)
        self.health = HealthRecords(health_results)
        self.finances = FinancialDetails()
        self.fout = open(output_file, "w")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.athletics.get_age()

    def get_height(self):
        return self.athletics.get_height()

    def get_weight(self):
        return self.athletics.get_weight()

    def show_index(self):
        self.athletics.idx()

    def health(self):
        if self.health.get_health_results() == "healthy":
            print("You don't need to get vaccinated")
            self.fout.write("You don't need to get vaccinated\n")
            self.fout.flush()
        elif self.health.get_health_results() == "unhealthy":
            print("You should get vaccinated")
            self.fout.write("You should get vaccinated\n")
            self.fout.flush()
        else:
            print("You entered incorrect values")
            self.fout.write("You entered incorrect values\n")
            self.fout.flush()

    def get_salary(self):
        return self.finances.calculate_salary()

    def get_salary_with_taxes(self):
        return self.finances.get_salary_with_taxes()

    def get_bank_info(self):
        return self.finances.get_bank_info()

    def dispose(self):
        self.fout.flush()
        self.fout.close()


class SecondClass:
    def MethodFromSecontClass(self):
        print("This is an additional method")


class Sportsman(Human, SecondClass):
    def __init__(self, name, age, height, weight, health_results, output_file):
        super().__init__(name, age, height, weight, health_results, output_file)

    def running(self, metres):
        print(f"Olympic running standards for sportsmen to run: {metres} metres")
        sec = metres / 7
        print(f"{self.get_name()} has to finish running in {sec} seconds")


if __name__ == "__main__":
    person = Sportsman("Сristiano", 25, 185, 7, "healthy", "Txt.txt")
    print(person.get_name() + " is: " + str(person.get_age()) + " years old")
    person.show_index()
    person.running(100)
    person.MethodFromSecontClass()
    person.dispose()
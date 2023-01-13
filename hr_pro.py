import subprocess


class Employee:
    # name = "bader"
    # age = 30
    # salary = 2000
    # employment_years = 10
    def __init__(self,name, age, salary,employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years

    def get_annual_salary(self):
        print(self.salary * 12)
        return self.salary * 12
Employee("Bader",30,2000,10).get_annual_salary()


   #Employee class here
class Manegar(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage
    
    def get_bonus(self):
        return self.bonus_percentage * self.salary
ana = Manegar(10)
print(ana.get_bonus())
    
# class Manager(Employee):
#     #Manager class here
        
# def main():
# 	# main code here

# if __name__ == '__main__':
# 	main()
# Employee()
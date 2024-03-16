#!/usr/bin/python3

"""
TODO: Define Person class with name, age, gender attributes. Implement introduce method. Instantiate and call introduce.
"""
class Person:
    def __init__(self, name: str, age: int, gender: str):
        """
        Constructor method to initialize attributes of the Person class.
        
        Args:
        name (str): The name of the person.
        age (int): The age of the person.
        gender (str): The gender of the person.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """
        Method to introduce the person.
        Prints a message with the person's name, age, and gender.
        """
        print(f"Hello my name is {self.name}. I am {self.age} years old and I am {self.gender}.")    


if __name__ == "__main__":
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your name: ")

    # Creating an instance of Person class
    person1 = Person(name, age, gender)

    # Calling the introduce method to display the person's information
    person1.introduce()

from Numerology import Numerology
import re


class Program:
    @staticmethod
    def main():
        __regex = r"^[\d]{2}-[\d]{2}-[\d]{4}$"

        sNameInput = input("Please input your name: ")

        while sNameInput == "" or not any(char.isalpha() for char in sNameInput):
            print("Empty name provided. Please enter again: ")
            sNameInput = input("Please input your name: ")

        sDobInput = input("Please input your birthdate (mm-dd-yyyy): ")

        while re.search(__regex, sDobInput) is None:
            print("Incorrect date format provided. Please enter again: ")
            sDobInput = input("Please input your birthdate (mm-dd-yyyy): ")

        num = Numerology(sNameInput, sDobInput)
        print("Name: " + num.getName())
        print("DOB: " + num.getBirthdate())
        print("Life Path Number: " + num.getLifePath())
        print("Birth Day Number: " + num.getBirthday())
        print("Attitude Day Number: " + num.getAttitude())
        print("Soul Number: " + num.getSoul())
        print("Personaility Number: " + num.getPersonality())
        print("Power Name Number: " + num.getPowerName())


if __name__ == '__main__':
    Program.main()

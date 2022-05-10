class Numerology:
    __sVowels = "aeiou"
    __dictLetterValues = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
                        "j": 1, "k": 2, "l": 3, "m": 4, "n": 5, "o": 6, "p": 7, "q": 8, "r": 9,
                        "s": 1, "t": 2, "u": 3, "v": 4, "w": 5, "x": 6, "y": 7, "z": 8, " ": 0}

    def __init__(self, sName, sDob):
        self.sName = sName
        self.sDob = sDob

    def getName(self):
        return self.sName

    def getBirthdate(self):
        return self.sDob

    def getLifePath(self):
        sLongDate = self.sDob.replace("-", "")
        return self.__getSingleDigit(sLongDate)

    def getBirthday(self):
        lst_date_split = self.sDob.split("-")
        return self.__getSingleDigit(lst_date_split[1])

    def getAttitude(self):
        lst_date_split = self.sDob.split("-")
        return self.__getSingleDigit(lst_date_split[0] + lst_date_split[1])

    def getSoul(self):
        iSoulTotal = 0
        for char in self.sName.lower():
            if char in self.__sVowels:
                iSoulTotal += self.__dictLetterValues[char]
        return self.__getSingleDigit(iSoulTotal)

    def getPersonality(self):
        iPersonalityTotal = 0
        for char in self.sName.lower():
            if char not in self.__sVowels:
                iPersonalityTotal += self.__dictLetterValues[char]
        return self.__getSingleDigit(iPersonalityTotal)

    def getPowerName(self):
        return self.__getSingleDigit(self.getSoul() + self.getPersonality())

    def __getSingleDigit(self, iLongNumber):
        while int(iLongNumber) > 9:
            result = [int(x) for x in str(iLongNumber)]
            iLongNumber = sum(result)
        return str(iLongNumber).strip("0")

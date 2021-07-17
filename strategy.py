from enum import Enum
import string
import random
from typing import List


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


class Interests(Enum):
    SPORT = 'sport'
    ART = 'art'
    TECH = 'tech'


class User(object):
    name: str
    age: int
    gender: Gender
    interests: Interests
    presents: List[str] = []

    def __init__(self, name: str, age: int, gender: Gender, interests: Interests) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests
        self.presents = []

    def setPresent(self, present: str) -> None:
        self.presents.append(present)

    def getLastPresent(self) -> str:
        return self.presents[len(self.presents) - 1]

    def getPresents(self) -> List[str]:
        return self.presents

    def getName(self) -> str:
        return self.name


class PresentStategy:
    @staticmethod
    def smart(user: User) -> None:
        if user.age >= 18:
            if user.gender == Gender.MALE:
                if user.interests == Interests.SPORT:
                    user.setPresent('ball')
                elif user.interests == Interests.TECH:
                    user.setPresent('keyboard')
                elif user.interests == Interests.ART:
                    user.setPresent('guitar')
                else:
                    user.setPresent('whiskey')
            else:
                if user.interests == Interests.SPORT:
                    user.setPresent('towel')
                elif user.interests == Interests.TECH:
                    user.setPresent('mouse')
                elif user.interests == Interests.ART:
                    user.setPresent('skirt')
                else:
                    user.setPresent('rose')
        else:
            if user.gender == Gender.MALE:
                user.setPresent('board game')
            else:
                user.setPresent('doll')

    @staticmethod
    def quick(user: User) -> None:
        if user.gender == Gender.MALE:
            user.setPresent('shirt')
        else:
            user.setPresent('parfume')

    @staticmethod
    def random(user: User) -> None:
        user.setPresent(''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(11)))


if __name__ == '__main__':
    user1 = User('John', 30, Gender.MALE, Interests.SPORT)

    PresentStategy.smart(user1)

    print(user1.getName(), ':', user1.getLastPresent())

    user2 = User('Delilah', 30, Gender.FEMALE, Interests.TECH)

    PresentStategy.smart(user2)

    PresentStategy.quick(user2)

    PresentStategy.random(user2)

    print(user2.getName(), ':', user2.getPresents())

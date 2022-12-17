from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History: str = 'History'
    Maths: str = 'Maths'
    Physics: str = 'Physics'


class Hobby(Enum):
    Sports: str = 'Sports'
    Reading: str = 'Reading'
    Music: str = 'Music'


class Gender(Enum):
    Male: str = 'Male'
    Female: str = 'Female'
    Other: str = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'Lukyanov'
    email: str = 'lukyanov@qaguru.com'
    mobile: str = '8911120121'
    birth_day: str = '04'
    birth_month: str = 'May'
    birth_year: str = '1990'
    subjects: Tuple[Subject] = (
        Subject.History,
        Subject.Maths,
    )
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    current_address: str = 'Russia Saint-P Moskovskaya 20'
    picture_file: str = 'photo.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


user = User(name='Evgeniy', gender=Gender.Male)

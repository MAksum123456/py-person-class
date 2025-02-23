from typing import List


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: List[dict]) -> List[Person]:
    for person_dict in people_data:
        person = Person(person_dict["name"], person_dict["age"])

        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
            person.wife.husband = person
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]
            person.husband.wife = person

    return list(Person.people.values())

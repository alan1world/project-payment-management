# TODO: Project -> project_id: str, title: str
# TODO: Portfolio, Programme, Package, Phase
# TODO: ???
# from faker import Faker
# fake = Faker('en_GB')
# 
# project
# faker.providers.misc.Provider -> uuid4()
# faker.providers.date_time.Provider -> date_between
# faker.providers.lorem.Provider -> text
# 
# user
# faker.providers.person.Provider -> name()
# faker.providers.job.Provider -> job()
# faker.providers.company.Provider -> company()
# 
# Custom provider
# Hubs and areas, frameworks, etc.
from typing import Iterator

import faker
# import project_payment_management as ppm
import project_payment_management.structures.projects as psp

# from faker import Faker

# from project_payment_management.structures.projects import Project


fake = faker.Faker('en_GB')
# fake.add_provider(internet)

def make_project() -> psp.Project:
    return psp.Project(
        project_id=fake.uuid4(), 
        title=" ".join(fake.words()),
        )


def make_projects(amount: int | None = None) -> Iterator[psp.Project]:
    amount = amount or fake.random_digit_above_two()
    for i in range(amount):
        yield make_project()


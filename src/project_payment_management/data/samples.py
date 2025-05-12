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
# from datetime import date

import faker
# import project_payment_management as ppm
import project_payment_management.structures.projects as psp
import project_payment_management.structures.contracts as psc

# from faker import Faker

# from project_payment_management.structures.projects import Project


fake = faker.Faker('en_GB')
# fake.add_provider(internet)

def make_contract() -> psc.Contract:
    ref_date = fake.date_between(start_date="-3y", end_date="+1y")
    return psc.Contract(
        contract_id=fake.uuid4(),
        title=" ".join(fake.words()),
        # amount=fake.random_number(digits=5, fix_len=True),
        amount=fake.random_int(min=10_000, max=10_000_000, step=5_000),
        start_date=ref_date,
        end_date=fake.date_between(start_date=ref_date, end_date="+5y"),
        )

def make_contracts(amount: int | None = None) -> Iterator[psc.Contract]:
    amount = amount or fake.random_digit_above_two()
    for _ in range(amount):
        yield make_contract()

def make_project() -> psp.Project:
    return psp.Project(
        project_id=fake.uuid4(), 
        title=" ".join(fake.words()),
        contracts=list(make_contracts()),
        )

def make_projects(amount: int | None = None) -> Iterator[psp.Project]:
    amount = amount or fake.random_digit_above_two()
    for _ in range(amount):
        yield make_project()


# @dataclass
# class Contract:
#     contract_id: str
#     title: str
#     amount: float  # Decimal
#     start_date: date
#     end_date: date
#     owner: Literal["programme", "package", "project", "phase"] = "project"
#     owner_id: str | None = None
#     # initial_start_date: str
#     # initial_end_date: str
#     # current_start_date: str
#     # current_end_date: str
#     option: str | None = None
#     stage: str | None = None
#     version: int = 1


# import uuid


from dataclasses import dataclass, field


@dataclass
class Phase:
    phase_id: str
    number: int
    title: str
    project_id: str
    description: str | None = None


@dataclass
class Project:
    project_id: str
    title: str
    version: int = 1
    description: str | None = None
    package_id: str | None = None
    programme_id: str | None = None
    phases: list[Phase] = field(default_factory=list)

    @property
    def number_of_phases(self):
        return len(self.phases)


@dataclass
class Package:
    package_id: str
    title: str
    version: int = 1
    description: str | None = None
    programme_id: str | None = None
    projects: list[Project] = field(default_factory=list)


@dataclass
class Programme:
    programme_id: str
    title: str
    version: int = 1
    description: str | None = None
    portfolio_id: str | None = None
    packages: list[Package] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)


@dataclass
class Portfolio:
    portfolio_id: str
    title: str
    version: int = 1
    description: str | None = None
    programmes: list[Programme] = field(default_factory=list)
    packages: list[Package] = field(default_factory=list)


# TODO: Forms -> for all
# TODO: Forms only for Client, not Supplier
# TODO: Soft delete
# TODO: internal IDs should be GUID -4?
# TODO: Programme should return list of all projects, including those in packages
# TODO: Project should return all contracts, including those in Phases
#
# TODO: versions, start and end dates, original and modified
# TODO: versions may need to copy the lists
# TODO: Faker to create samples
# uuid.uuid4() -> Generate a random UUID
#
# TODO: States Enum -> active, deleted, suspended, draft

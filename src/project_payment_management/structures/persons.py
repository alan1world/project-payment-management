from enums import Enum


class Role(Enum):
    pass


class Company(Enum):
    pass


class User:
    pass


# TODO: Forms -> Add User, Change user type, (soft) delete user
# TODO: Only Admin users should be able to change company or type
# TODO: type should be a flag -> master admin, admin, senior, user, read-only
# TODO: admin actions would be master | admin
# Each company can have a primary user that has admin for that company
# Or senior / superuser fills that role
# TODO: Forms -> Roles and Company
# Company needs to distinguish between client and supplier
# Only client can create project and contract
# Only supplier can create afp and cost line, transfer accrued to actual
# Only client can disallow cost
# Client can create afp forecasts
# AfP can only be added to a contract
# Contracts can be added to programme, package, project, phase

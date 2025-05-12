# from enum import Enum
from datetime import date
from dataclasses import dataclass
from typing import Literal
# from decimal import Decimal


# class DateType(Enum):
#     ORIGINAL = "Original"
    
# @dataclass
# class DateType:
#     type: Literal["Original", "Current"]
#     period: Literal["Actual", "Forecast"]


@dataclass
class Contract:
    contract_id: str
    title: str
    amount: float  # Decimal
    start_date: date
    end_date: date
    owner: Literal["programme", "package", "project", "phase"] = "project"
    owner_id: str | None = None
    # initial_start_date: str
    # initial_end_date: str
    # current_start_date: str
    # current_end_date: str
    option: str | None = None
    stage: str | None = None
    version: int = 1


"""Dummy employment records that can be imported and called from other programs."""

from dataclasses import asdict, dataclass
from datetime import date
import json
from typing import Any


@dataclass(frozen=True)
class EmploymentRecord:
    """A small, serializable employment record for demo and test data."""

    employee_id: int
    first_name: str
    last_name: str
    job_title: str
    department: str
    start_date: str
    salary: int
    employment_type: str = "Full-time"
    active: bool = True

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def create_employment_record(
    employee_id: int,
    first_name: str,
    last_name: str,
    job_title: str,
    department: str,
    start_date: str,
    salary: int,
    employment_type: str = "Full-time",
    active: bool = True,
) -> EmploymentRecord:
    """Create one dummy employment record."""
    date.fromisoformat(start_date)
    if salary < 0:
        raise ValueError("salary must be zero or greater")

    return EmploymentRecord(
        employee_id=employee_id,
        first_name=first_name,
        last_name=last_name,
        job_title=job_title,
        department=department,
        start_date=start_date,
        salary=salary,
        employment_type=employment_type,
        active=active,
    )


def generate_dummy_employees() -> list[EmploymentRecord]:
    """Return a repeatable set of dummy employee records."""
    return [
        create_employment_record(
            1001, "Ava", "Patel", "Software Engineer", "Engineering", "2021-04-12", 92000
        ),
        create_employment_record(
            1002, "Liam", "Garcia", "Product Manager", "Product", "2020-09-01", 105000
        ),
        create_employment_record(
            1003,
            "Mia",
            "Chen",
            "UX Designer",
            "Design",
            "2023-01-16",
            78000,
            "Part-time",
        ),
        create_employment_record(
            1004,
            "Noah",
            "Williams",
            "Data Analyst",
            "Finance",
            "2019-06-24",
            83000,
            active=False,
        ),
    ]


def find_employee(
    employee_id: int, records: list[EmploymentRecord] | None = None
) -> EmploymentRecord | None:
    """Find one employee by ID, returning None when there is no match."""
    records = generate_dummy_employees() if records is None else records
    return next((record for record in records if record.employee_id == employee_id), None)


def filter_by_department(
    department: str, records: list[EmploymentRecord] | None = None
) -> list[EmploymentRecord]:
    """Return employees in a department, using case-insensitive matching."""
    records = generate_dummy_employees() if records is None else records
    return [record for record in records if record.department.lower() == department.lower()]


def export_records_json(
    records: list[EmploymentRecord] | None = None, indent: int = 2
) -> str:
    """Convert employment records to JSON for use by another program or API."""
    records = generate_dummy_employees() if records is None else records
    return json.dumps([record.to_dict() for record in records], indent=indent)


def main() -> None:
    """Print the dummy records when this module is run directly."""
    print(export_records_json())


if __name__ == "__main__":
    main()

from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with ""M""")

        if not any(member.rank in (Rank.captain, Rank.commander)
                   for member in self.crew):
            raise ValueError("Must have at least one Commander or Captain")

        total = len(self.crew)
        experienced = 0
        for memeber in self.crew:
            if memeber.years_experience >= 5:
                experienced += 1
        if self.duration_days > 365 and experienced / total < 0.5:
            raise ValueError(" Long missions (> 365 days) need 50%% "
                             "experienced crew (5+ years)")

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="efvef",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=28,
                    specialization="Mission Command",
                    years_experience=6
                ),
                CrewMember(
                    member_id="abcdef",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=30,
                    specialization="Navigation",
                    years_experience=8
                ),
                CrewMember(
                    member_id="fedcba",
                    name=" Alice Johnson",
                    rank=Rank.officer,
                    age=32,
                    specialization="Engineering",
                    years_experience=3
                )
            ],
            budget_millions=2500.0
        )
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for memeber in mission.crew:
            print(f"- {memeber.name} ({memeber.rank.value}) "
                  f"- {memeber.specialization}")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])

    try:
        print("=========================================")
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="efvef",
                    name="Sarah Connor",
                    rank=Rank.cadet,
                    age=28,
                    specialization="Mission Command",
                    years_experience=6
                ),
                CrewMember(
                    member_id="abcdef",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=30,
                    specialization="Navigation",
                    years_experience=8
                ),
                CrewMember(
                    member_id="fedcba",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=32,
                    specialization="Engineering",
                    years_experience=3
                )
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for memeber in mission.crew:
            print(f"- {memeber.name} ({memeber.rank.value}) "
                  f"- {memeber.specialization}")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()

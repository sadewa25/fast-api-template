from typing import List, Optional

from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from repository.users_repository import UserRepository
from schemas.users_schema import UserInput, UserOutput


class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    # def create(self, data: UserInput) -> UserOutput:
    #     if self.repository.region_exists_by_name(data.name):
    #         raise HTTPException(status_code=400, detail="Region already exists")
    #     return self.repository.create(data)

    def get_all(self) -> List[Optional[UserOutput]]:
        return self.repository.get_all()
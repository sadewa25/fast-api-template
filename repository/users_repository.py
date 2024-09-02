from sqlalchemy.orm import Session
from models.users import Users
from schemas.users_schema import UserInput, UserOutput
from typing import List, Optional, Type
from pydantic import UUID4


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    # def create(self, data: UserInput) -> UserOutput:
    #     region = Users(**data.model_dump(exclude_none=True))
    #     self.session.add(region)
    #     self.session.commit()
    #     self.session.refresh(region)
    #     return UserOutput(id=region.id, name=region.name)

    def get_all(self) -> List[Optional[UserOutput]]:
        users = self.session.query(Users).all()
        return [UserOutput(**user.__dict__) for user in users]

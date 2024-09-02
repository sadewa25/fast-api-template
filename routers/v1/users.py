from typing import List

from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.users_schema import UserOutput, UserInput
from service.users_service import UserService


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# @router.post("", status_code=201, response_model=RegionOutput)
# def create_region(
#         data: RegionInput,
#         session: Session = Depends(get_db),
# ):
#     _service = RegionService(session)
#     return _service.create(data)


@router.get("", status_code=200, response_model=List[UserOutput])
def get_regions(session: Session = Depends(get_db)) -> List[UserOutput]:
    _service = UserService(session)
    return _service.get_all()
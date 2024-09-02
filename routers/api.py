from fastapi import APIRouter
from routers.v1 import users

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(users.router)
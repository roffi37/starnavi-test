from fastapi import APIRouter, Depends

from src.schemas.user import UserCreateSchema
from src.services.user import get_user_service, UserService

router = APIRouter(
    prefix="/user",
)

@router.get("/")
async def get_all_users(service: UserService = Depends(get_user_service)):
    return await service.get_all()


@router.post("/")
async def create_user(
        schema: UserCreateSchema,
        service: UserService = Depends(get_user_service),
    ):
    return await service.create_one(schema)

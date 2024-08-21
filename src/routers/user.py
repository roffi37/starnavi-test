from fastapi import APIRouter, Depends

from src.schemas.user import UserCreateSchema, UserSignInSchema
from src.services.user import get_user_service, UserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
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


@router.put("/{user_id}")
async def update_user(
        user_id: int,
        schema: UserCreateSchema,
        service: UserService = Depends(get_user_service),
):
    return await service.update_one(user_id, schema)


@router.delete("/{user_id}")
async def delete_user(
        user_id: int,
        service: UserService = Depends(get_user_service),
):
    return await service.delete(user_id)


@router.post("/signin")
async def signin_user(
        schema: UserSignInSchema,
        service: UserService = Depends(get_user_service),
):
    return await service.sign_in(schema)

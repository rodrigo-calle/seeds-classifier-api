from fastapi import APIRouter
from .services import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_users():
    users = UserService.get_users_service()
    return users

@router.get("/{user_id}")
def get_user_by_id(user_id: str):
    user = UserService.get_user_by_id_service(user_id)
    if user.exists:
        return user.to_dict()
    else:
        return {"error": "User not found"}

@router.get("/technical/all")
def get_technical_users():
    users = UserService.get_technical_users_service()
    return [user.to_dict() for user in users]
    # print(user)
    # technical_users = []
    # for user in users:
    #     print(user)
    #     if user.get("userType") == "technical":
    #         technical_users.append(user)
    # return technical_users

@router.post("/")
def create_user(user: dict):
    user = UserService.create_user_service(user)
    return user[1].get().to_dict()

    
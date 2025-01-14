from fastapi import APIRouter

router = APIRouter()


@router.post("/users", tags=["users"])
async def create_user():
    return {"message": "OK"}


@router.get("/users", tags=["users"])
async def get_users():
    return {"message": "OK"}


@router.get("/users/{id}", tags=["users"])
async def get_user():
    return {"message": "OK"}

from fastapi import APIRouter

router = APIRouter()


@router.post("/transactions", tags=["transactions"])
async def create_transaction():
    return {"message": "OK"}

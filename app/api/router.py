from fastapi import APIRouter
from . import user, store, auth, item

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user")
api_router.include_router(store.router, prefix="/store")
api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(item.router, prefix="/item")

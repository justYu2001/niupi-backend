from fastapi import APIRouter

from . import user, stores, auth, users, items, districts


api_router = APIRouter()

api_router.include_router(user.router, prefix="/user")
api_router.include_router(users.router, prefix="/users")
api_router.include_router(stores.router, prefix="/stores")
api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(items.router, prefix="/items")
api_router.include_router(districts.router, prefix="/districts")

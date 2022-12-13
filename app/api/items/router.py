from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from . import service
from .dependencies import get_db, validate_item_id
from .exceptions import ItemNotFound
from .schemas import Item, ItemUpdate


router = APIRouter()


@router.get("/{item_id}", response_model=Item)
def read_item(item: Item = Depends(validate_item_id)):
    return item


@router.get("/{item_id}/photos", response_model=list[UUID4])
def read_photos(item: Item = Depends(validate_item_id), db: Session = Depends(get_db)):
    photo_ids = service.get_photos_by_item_id(db, item.id)
    return photo_ids


@router.patch("/{item_id}", response_model=Item)
def update_item(
    payload: ItemUpdate,
    item: Item = Depends(validate_item_id),
    db: Session = Depends(get_db)
):
    updated_item = service.update_item(db, item.id, payload)

    return updated_item


@router.delete("/{item_id}", status_code=204)
def delete_item(item: Item = Depends(validate_item_id), db: Session = Depends(get_db)):
    service.delete_item_by_item_id(db, item.id)

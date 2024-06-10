from fastapi import APIRouter

router = APIRouter(
    prefix="/contacts",
    tags=["contacts"],
)


@router.get("/")
async def get_contact_all():
    pass


@router.post("/")
async def create_contact():
    pass


@router.get("/{id}")
async def get_contact():
    pass


@router.put("/{id}")
async def update_contact():
    pass


@router.delete("/{id}")
async def delete_contact():
    pass

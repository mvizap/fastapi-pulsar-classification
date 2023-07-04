from fastapi import APIRouter
#from controllers.todo_controller import router as todos_router
from controllers.pulsar_controller import router as pulsar_router

router = APIRouter()

router.include_router(pulsar_router)

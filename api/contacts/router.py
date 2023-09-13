from fastapi import UploadFile, Depends
from fastapi.routing import APIRouter
from fastapi.responses import FileResponse
from typing import Union

from config import logger, HTTPStatus
from api.contacts.response_schemas import (
    ErrorResponse,
    UploadFileResponse,
    GetContactsByDateResponse,
    DeleteFileResponse,
    ContactsFileInDBResponse,
)
from api.contacts.request_schemas import (
    GetContactsByDateQuery,
    GetContactsByUIDQuery,
    DeleteContactsByUIDQuery,
)


contacts_router = APIRouter(prefix="/contacts", tags=["Contacts"])


@contacts_router.post(
    "/",
    summary="Upload contacts",
    description="This endpoint takes contacts from an user in form of a CSV file",
    responses={
        HTTPStatus.ACCEPTED: {"model": UploadFileResponse},
        HTTPStatus.BAD_REQUEST: {"model": ErrorResponse},
    },
)
async def upload_csv(csv_file: UploadFile):
    return {}


@contacts_router.get(
    "/",
    summary="Get contacts from date",
    description="This endpoint returns contacts files uploaded on the date or the range specified",
    responses={
        HTTPStatus.OK: {"model": GetContactsByDateResponse},
        HTTPStatus.BAD_REQUEST: {"model": ErrorResponse},
    },
)
async def get_contacts_by_date(
    request: GetContactsByDateQuery = Depends(GetContactsByDateQuery),
):
    logger.debug(request)
    return {}


@contacts_router.get(
    "/{contacts_file_uid}",
    summary="Get contacts from file uid",
    description="This endpoint returns contacts files or their structured data of the given file uid",
    responses={
        HTTPStatus.OK: {"model": ContactsFileInDBResponse},
        HTTPStatus.NOT_FOUND: {"model": ErrorResponse},
    },
)
async def get_contacts_by_uid(
    request: GetContactsByUIDQuery = Depends(GetContactsByUIDQuery),
):
    logger.debug(request)
    return {}


@contacts_router.delete(
    "/{contacts_file_uid}",
    summary="Delete contacts from file uid",
    description="This endpoint deletes contacts files of the given file uid",
    responses={
        HTTPStatus.ACCEPTED: {"model": DeleteFileResponse},
        HTTPStatus.NOT_FOUND: {"model": ErrorResponse},
    },
)
async def delete_contacts(
    request: DeleteContactsByUIDQuery = Depends(DeleteContactsByUIDQuery),
):
    logger.debug(request)
    return {}

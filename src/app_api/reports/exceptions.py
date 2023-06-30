from fastapi import HTTPException
from fastapi import status

filters_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Some filters are missing or invalid.",
)

report_not_exists_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Requested report does not exist."
)

limit_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="You exceeded the possible limit in one or more filters."
)

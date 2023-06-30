from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from pydantic import BaseModel


class ReportFilter(BaseModel):
    name: str
    is_mandatory: bool
    default_value: Any
    limit: Optional[Union[int, float]]


class Report(BaseModel):
    id: Optional[int]
    report_name: str
    description: Optional[str]
    is_active: Optional[int]
    exec_string: Optional[str]
    db_type: Optional[str]
    connection_id: Optional[str]
    filters: Optional[Dict[str, ReportFilter]]

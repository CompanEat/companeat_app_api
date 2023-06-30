from fastapi import APIRouter
from fastapi import Request
reports_app = APIRouter()
from .utils import get_api_report
@reports_app.get("/report/{report_name}", tags=["Reports"])
async def dynamic_report(request: Request, report_name=None):
    params = dict(request.query_params)
    reports = []
    if report_name is not None:
        reports = get_api_report(params, report_name)
        # Create a new client and connect to the server
    return reports

# from fastapi import APIRouter, Depends
# from pypika.functions import Date
# from rearq import ReArq, constants
# from starlette.requests import Request
# from tortoise.functions import Count, Function
# from app.api.depends.depends_ import get_rearq
# from rearq.server.models import JobResult, Job
#
# router = APIRouter()
#
#
# class ToDate(Function):
#     database_func = Date
#
#
# async def index(request: Request, rearq: ReArq = Depends(get_rearq), ):
#     task_map = rearq.task_map
#     task_num = len(task_map)
#     workers_info = await rearq.redis.hgetall(constants.WORKER_KEY)
#     worker_num = len(workers_info)
#     result_num = await JobResult.all().count()
#     job_num = await Job.all().count()
#     result = (
#         await Job.all()
#             .annotate(count=Count("id"), date=ToDate("enqueue_time"))
#             .group_by("date", "status")
#             .order_by("date")
#             .values("date", "status", "count")
#     )
#     x_axis = []
#     series = [
#         {
#             "name": "Deferred",
#             "type": "line",
#             "data": [],
#             "stack": "total",
#             "label": {"show": "true"},
#         },
#         {
#             "name": "Queued",
#             "type": "line",
#             "stack": "total",
#             "data": [],
#             "label": {"show": "true"},
#         },
#         {
#             "name": "InProgress",
#             "type": "line",
#             "stack": "total",
#             "data": [],
#             "label": {"show": "true"},
#         },
#         {
#             "name": "Success",
#             "type": "line",
#             "stack": "total",
#             "data": [],
#             "label": {"show": "true"},
#         },
#         {
#             "name": "Failed",
#             "type": "line",
#             "stack": "total",
#             "data": [],
#             "label": {"show": "true"},
#         },
#         {
#             "name": "Expired",
#             "type": "line",
#             "stack": "total",
#             "data": [],
#             "label": {"show": "true"},
#         },
#     ]
#     for item in result:
#         date = str(item.get("date"))
#         if date not in x_axis:
#             x_axis.append(date)
#         count = item.get("count")
#         status = item.get("status")
#         if status == "deferred":
#             series[0]["data"].append(count)
#         elif status == "queued":
#             series[1]["data"].append(count)
#         elif status == "in_progress":
#             series[2]["data"].append(count)
#         elif status == "success":
#             series[3]["data"].append(count)
#         elif status == "failed":
#             series[4]["data"].append(count)
#         elif status == "expired":
#             series[5]["data"].append(count)
#     return {
#         "code": 20000,
#         "page_title": "dashboard",
#         "worker_num": worker_num,
#         "task_num": task_num,
#         "job_num": job_num,
#         "result_num": result_num,
#         "x_axis": x_axis,
#         "series": series,
#     }
#
#
# async def get_status(request: Request, ):
#     status_ = [
#         {
#             "name": "deferred",
#             "type": "line",
#             "label": {"show": "true"},
#         },
#         {
#             "name": "queued",
#             "type": "line",
#             "label": {"show": "true"},
#         },
#         {
#             "name": "in_progress",
#             "type": "line",
#             "label": {"show": "true"},
#         },
#         {
#             "name": "success",
#             "type": "line",
#             "label": {"show": "true"},
#         },
#         {
#             "name": "failed",
#             "type": "line",
#             "label": {"show": "true"},
#         },
#         {
#             "name": "expired",
#             "type": "line",
#             "label": {"show": "true"},
#         },
#     ]
#     return {
#         "code": 20000,
#         "all_status": status_,
#     }
#
#
# router.add_api_route(methods=['GET'], path="/index", endpoint=index, summary="全局信息")
# router.add_api_route(methods=['GET'], path="/status", endpoint=get_status, summary="状态信息")

from enum import Enum
from typing import Optional, List

from fastapi import APIRouter, Path, Query

app03 = APIRouter()

"""Path Parameters and Number Validations 路径参数和数字验证"""


@app03.get('/path/{parameters}')
def get_params01(parameters: str):
    return {
        "message": parameters
    }


class CityName(str, Enum):
    Beijing = "Beijing China"
    Shanghai = "Shanghai China"


@app03.get("/enum/{city}")
async def latest(city: CityName):
    if city == CityName.Shanghai:
        return {
            "city_name": city,
            "confirmed": 1499,
            "death": 7
        }
    if city == CityName.Beijing:
        return {
            "city_name": city,
            "confirmed": 971,
            "death": 9
        }
    return {
        "city_name": city,
        "latest": "unknown"
    }


@app03.get("/files/{file_path:path}")
def file_path(file_path: str):
    return f"The file path is {file_path}"


@app03.get("/path/{num}")
def path_params_validate(num: int = Path(None, title="Your number", description="不可描述", ge=1, le=10)):
    return num


"""Query Parameters and String Validations 查询参数和字符串验证"""


def page_limit(page: int = 1, limit: Optional[int] = None):
    if limit:
        return {
            "page": page,
            "limit": limit
        }
    return {
        "page": page
    }


@app03.get("/query/bool/convention")
def type_convention(param: bool = False):
    return param


@app03.get("/query/validations")
def query_params(value: str = Query(..., min_length=8, max_length=16, regex="^a"),
                 values: List[str] = Query(default=["v1", "v2"], alias="alias_name")):
    return value, values

from typing import Literal, TypeAlias, TypedDict

from drf_spectacular.utils import OpenApiParameter, OpenApiResponse
from drf_yasg import openapi

# 必要な際に適宜追加してください
StatusCode: TypeAlias = Literal[200, 400, 401, 403, 404, 500]



# class NewsListSwaggerParamsType(TypedDict):
#     summary: str
#     description: str
#     parameters: list[OpenApiParameter]
#     responses: dict[StatusCode, OpenApiResponse]


PUBLISHER_CODE_PARAM = OpenApiParameter(
    name="publisher_code",
    description="パブリッシャーコード",
    type=str,
    required=False,
)
EMAIL_PARAM = OpenApiParameter(
    name="email",
    description="Email Address",
    type=str,
    required=True,
)
PASSWORD_PARAM = OpenApiParameter(
    name="password",
    description="Password",
    type=str,
    required=True
)
RegisterSwaggerParams = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['email','password', 'username'],
        properties={
            'email':openapi.Schema(type=openapi.TYPE_STRING),
            'password':openapi.Schema(type=openapi.TYPE_STRING),
            'username':openapi.Schema(type=openapi.TYPE_STRING),
        },
        operation_description='Register a new user', 
    )
RegisterSwaggerResponse = {
    200: 'Register successful!', 
    400: 'This email has already exist!'
}
LoginSwaggerParams = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['email','password', 'username'],
        properties={
            'email':openapi.Schema(type=openapi.TYPE_STRING),
            'password':openapi.Schema(type=openapi.TYPE_STRING),
        },
        operation_description='Register a new user', 
)
# NewsListSwaggerParams: NewsListSwaggerParamsType = {
#     "summary": "記事一覧",
#     "description": "記事一覧を取得します",
#     "parameters": [PUBLISHER_CODE_PARAM],
#     "responses": {200: OpenApiResponse(response=NewsSerializer, description="成功時のレスポンス")},
# }

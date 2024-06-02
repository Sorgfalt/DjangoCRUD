from drf_yasg import openapi


request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['title', 'content'],
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='제목 입력'),
        'content': openapi.Schema(type=openapi.TYPE_STRING, description='내용 입력'),
    },
)
from django.shortcuts import render

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from board.api_params import request_body
from board.services.board_service import BoardService
from board.serializer import BoardSerializer

import json


@swagger_auto_schema(
    method='post',
    operation_id='게시판 등록',
    operation_description='게시판을 등록합니다',
    tags=['Board'],
    request_body=request_body,
)
@api_view(['POST'])
def create_board(request):
    data = BoardSerializer.from_body(request)

    print("board_data12:", data["title"])
    print("board_data43:", data["content"])

    board_data = {"title": data["title"], "content": data["content"]}

    # Create a board using the BoardService
    board = BoardService.create_board(json.dumps(board_data))

    # Return board_data as JsonResponse
    return JsonResponse(board, safe=False)


@swagger_auto_schema(
    method='get',
    operation_id='게시판 조회',
    operation_description='게시판을 조회합니다',
    tags=['Board'],
)
@api_view(['GET'])
def select_board_list(request):
    board = BoardService.select_board_list()
    serializer = BoardSerializer(board)
    return JsonResponse(serializer.data, safe=False)

@swagger_auto_schema(
    method='put',
    operation_id='게시판 수정',
    operation_description='게시판을 수정합니다',
    tags=['Board'],
    request_body=request_body,
)
@api_view(['PUT'])
def update_board(request):
    data = BoardSerializer.from_body(request)
    board_data = {"title": data["title"], "content": data["content"]}
    board = BoardService.create_board(json.dumps(board_data))
    return JsonResponse(board, safe=False)
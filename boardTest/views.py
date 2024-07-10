from drf_yasg import openapi
from rest_framework.response import Response

from .models import BoardTest
from rest_framework import serializers, status

from django.shortcuts import render

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import api_view
from boardTest.board_service import BoardService
from boardTest.serializer import BoardSerializer

import json


@swagger_auto_schema(
    method='post',
    operation_id='게시판 등록',
    operation_description='게시판을 등록합니다',
    tags=['Board'],
    request_body=BoardSerializer,
)
@api_view(['POST'])
def create_board(request):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        board_json = serializer.create(serializer.validated_data)
        board_result = BoardService.create_board(board_json)
        return Response(board_result, status=status.HTTP_201_CREATED, content_type='application/json')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    operation_id='게시판 조회',
    operation_description='게시판을 조회합니다',
    tags=['Board'],
)
@api_view(['GET'])
def select_board_list(request):
    board = BoardService.select_board_list()
    serializer = BoardSerializer(board, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='put',
    operation_id='게시판 수정',
    operation_description='게시판을 수정합니다',
    tags=['Board'],
    manual_parameters=[
        openapi.Parameter(
            name='id',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description='ID of the board to update',
            required=True,
        ),
    ],
    request_body=BoardSerializer,
)
@api_view(['PUT'])
def update_board(request):
    board_id = request.query_params.get('id')
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        board_json = serializer.create(serializer.validated_data)
        print("id = " + board_id)
        board_result = BoardService.update_board(board_id, board_json)
        return Response(board_result, status=status.HTTP_201_CREATED, content_type='application/json')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='delete',
    operation_id='게시판 삭제',
    operation_description='게시판을 삭제합니다',
    tags=['Board'],
    manual_parameters=[
        openapi.Parameter(
            name='id',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description='ID of the board to update',
            required=True,
        ),
    ],
)
@api_view(['DELETE'])
def delete_board(request):
    board_id = request.query_params.get('id')

    board_result = BoardService.delete_board(board_id)
    return Response(board_result, status=status.HTTP_201_CREATED, content_type='application/json')

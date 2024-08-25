from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BFHLAPIView(APIView):
    def post(self, request):
        data = request.data.get('data', [])

        if not isinstance(data, list):
            return Response(
                {"is_success": False, "message": "Invalid input"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_lowercase = (
            max([char for char in alphabets if char.islower()], default=None)
        )

        user_info = {
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
        }

        return Response(
            {
                "is_success": True,
                **user_info,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
            }
        )

class OperationCodeView(APIView):
    def get(self, request):
        return Response({"operation_code": 1})


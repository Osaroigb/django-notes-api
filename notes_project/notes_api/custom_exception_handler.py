from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # DRF's default exception handler
    response = exception_handler(exc, context)

    if isinstance(exc, NotFound):
        custom_response_data = {
            "message": "Note not found.",
            "data": {},
            "status": 404
        }

        return Response(custom_response_data, status=404)

    # If the exception is not handled above, use the default response
    return response
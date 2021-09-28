from rest_framework import status

errors = {
    status.HTTP_406_NOT_ACCEPTABLE: {
        "data": {"detail": "Data sent is not acceptable"},
        "status": status.HTTP_406_NOT_ACCEPTABLE
    }
}
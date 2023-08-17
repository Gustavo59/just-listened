class JustListenedCoreBaseException(Exception):
    message = None
    http_status = 500

    def __init__(self, message=None, http_status=None, *args):
        self.message = message or self.message
        self.http_status = http_status or self.http_status
        super().__init__(self.message, *args)


class DataNotFoundError(JustListenedCoreBaseException):
    message = "Data not found in our records"
    http_status = 404


class UserInvalidToken(JustListenedCoreBaseException):
    message = "Invalid token"
    http_status = 403

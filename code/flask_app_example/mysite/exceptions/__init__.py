"""
接口异常类
"""
ERR_NO_ERROR = 0         # 成功
ERR_INTERNALSERVER = 1   # 未知错误
ERR_PARAM = 3            # 参数错误


class APIBaseException(Exception):
    """接口异常基类"""
    error_code = ERR_INTERNALSERVER
    msg = '服务器内部错误'
    data = None
    status = 500

    def __init__(self, msg=None, status=None, error_code=None, data=None):
        super().__init__()
        if msg is not None:
            self.msg = msg
        if status is not None:
            self.status = status
        if data is not None:
            self.data = data
        if error_code is not None:
            self.error_code = error_code


class InternalServerError(APIBaseException):
    """服务器内部错误"""
    error_code = ERR_INTERNALSERVER
    msg = '服务器内部错误'
    status = 500


class ParamError(APIBaseException):
    """参数错误"""
    error_code = ERR_PARAM
    msg = '参数错误'
    status = 400

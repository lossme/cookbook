import functools

from flask import current_app, request
import jsonschema.exceptions
import werkzeug.exceptions

from ..exceptions import APIBaseException, InternalServerError, ERR_NO_ERROR, ParamError


def error_handler(func):
    """API错误异常捕获"""
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            return {'status': ERR_NO_ERROR, 'desc': '成功', 'data': data}
        except APIBaseException as ex:
            return {'status': ex.error_code, 'desc': ex.msg}
        except Exception as ex:
            current_app.logger.error('服务器内部未知错误：%s', ex, exc_info=True)
            return {'status': InternalServerError.error_code, 'desc': InternalServerError.msg}
    return decorator


def verify_json_payload(schema):
    """通过jsonschema校验参数
    """
    try:
        payload = request.get_json()
    except werkzeug.exceptions.BadRequest:
        raise ParamError(msg='BadRequest: The browser (or proxy) \
            sent a request that this server could not understand.')
    return check_data(data=payload, schema=schema)


def check_data(data, schema):
    """"通过jsonschema校验参数，并为不存在的字段设置默认值
    :param data: 待校验数据
    :param schema: jsonschema
    :setdefault: 若字段不存在则设置默认值，如 setdefault = {'key1': 'default_value'}
    """
    try:
        jsonschema.validate(data, schema)
    except jsonschema.exceptions.ValidationError as ex:
        raise ParamError(msg='参数错误：{}'.format(ex.message))
    setdefault = schema.get('setdefault')
    if setdefault and isinstance(data, dict):
        for key, value in setdefault.items():
            data.setdefault(key, value)
    return data

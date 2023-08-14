import decimal
import json

import simplejson
from fastapi.encoders import jsonable_encoder


def deserializer_adapter_function(*args, **kwargs):
    return json.loads(*args, parse_float=decimal.Decimal, **kwargs)


def serializer_adapter_function(*args, **kwargs):
    default = kwargs.pop("default", jsonable_encoder)
    return simplejson.dumps(*args, use_decimal=True, default=default, **kwargs)

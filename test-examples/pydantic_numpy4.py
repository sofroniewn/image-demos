from typing import Generic, TypeVar

import numpy as np
from pydantic.fields import ModelField

JSON_ENCODERS = {
    np.ndarray: lambda arr: arr.tolist()
}

DType = TypeVar('DType')


class TypedArray(np.ndarray, Generic[DType]):
    """Wrapper class for numpy arrays that stores and validates type information.
    This can be used in place of a numpy array, but when used in a pydantic BaseModel
    or with pydantic.validate_arguments, its dtype will be *coerced* at runtime to the
    declared type.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, val, field: ModelField):
        dtype_field = field.sub_fields[0]
        actual_dtype = dtype_field.type_.__args__[0]
        # If numpy cannot create an array with the request dtype, an error will be raised
        # and correctly bubbled up.
        np_array = np.array(val, dtype=actual_dtype)
        return np_array



from typing_extensions import Literal

import numpy as np
import pydantic
import pytest


def make_array():
    return np.zeros((3, 2))

# class Model(pydantic.BaseModel):
#     x: TypedArray[Literal['float32']] = pydantic.Field(default_factory=make_array)

#     class Config:
#         json_encoders = JSON_ENCODERS


# model = Model(x=[1, 2])

# print(model)

# model = Model()
# print(model)

class Config:
    json_encoders = JSON_ENCODERS

# @pydantic.dataclasses.dataclass(config=Config)
# class Model:
#     x: TypedArray[Literal['float32']] = pydantic.Field(default_factory=make_array)


from dataclasses import field


@pydantic.dataclasses.dataclass(config=Config)
class Model:
    x: TypedArray[Literal['float32']] = field(default_factory=make_array)

model = Model(x=[1, 2])

print(model)

model = Model()
print(model)
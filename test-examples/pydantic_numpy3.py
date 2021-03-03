from typing_extensions import Literal
from typing import Generic, TypeVar, Tuple

import numpy as np
from pydantic.fields import ModelField

JSON_ENCODERS = {
    np.ndarray: lambda arr: arr.tolist()
}

# DType = TypeVar('DType')


# class TypedArray(np.ndarray, Generic[DType]):
#     """Wrapper class for numpy arrays that stores and validates type information.
#     This can be used in place of a numpy array, but when used in a pydantic BaseModel
#     or with pydantic.validate_arguments, its dtype will be *coerced* at runtime to the
#     declared type.
#     """

#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, val, field: ModelField):
#         if field.sub_fields and len(field.sub_fields) > 0:
#             dtype_field = field.sub_fields[0]
#             if len(dtype_field.type_.__args__) == 0:
#                 dtype = None
#                 shape = tuple()
#             elif len(dtype_field.type_.__args__) == 1:
#                 dtype = dtype_field.type_.__args__[0]
#                 shape = tuple()
#             else:
#                 dtype = dtype_field.type_.__args__[0]
#                 shape = dtype_field.type_.__args__[1]
#         else: 
#             dtype = None
#             shape = tuple()

#         result = np.array(val, dtype=dtype, copy=False, ndmin=len(shape))
#         assert not shape or len(shape) == len(result.shape)  # ndmin guarantees this

#         if any((shape[i] != -1 and shape[i] != result.shape[i]) for i in range(len(shape))):
#             result = result.reshape(shape)
#         return result

# class SingleColor(TypedArray, Generic[DType]):
#     @classmethod
#     def __get_validators__(cls):
#         print('ppprrrrrrp')
#         yield cls.validate

#     @classmethod
#     def validate(cls, val, field: ModelField):
#         print('hiiiiii')
#         return super().validate(val, field=pydantic.Field(type_=Literal[int]))


DType = TypeVar('DType')
ShapeType = TypeVar('Shape')


class Array(np.ndarray, Generic[DType, ShapeType]):
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
        if field.sub_fields and len(field.sub_fields) == 1:
            dtype = field.sub_fields[0].type_
            shape = tuple()
        elif field.sub_fields and len(field.sub_fields) == 2:
            dtype = field.sub_fields[0].type_
            shape = field.sub_fields[1].type_.__args__
            if shape[0] is None:
                shape = tuple()
        else: 
            dtype = None
            shape = tuple()

        result = np.array(val, dtype=dtype, copy=False, ndmin=len(shape))
        assert not shape or len(shape) == len(result.shape)  # ndmin guarantees this

        if any((shape[i] != -1 and shape[i] != result.shape[i]) for i in range(len(shape))):
            result = result.reshape(shape)
        return result

class SingleColor(Array, Generic[DType, ShapeType]):
    @classmethod
    def __get_validators__(cls):
        print('ppprrrrrrp')
        yield cls.validate

    @classmethod
    def validate(cls, val, field: ModelField):
        print('hiiiiii')
        return super().validate(val, field=field)


# [Literal['float32'], Literal[(-1, 4)]]

import numpy as np
import pydantic


def make_array():
    return np.zeros((3, 9))


class Model(pydantic.BaseModel):
    int_values: Array[int, Literal[None]]
    any_values: Array
    shaped1_values: Array[float, Literal[(-1, )]]
    shaped2_values: Array[int, Literal[(2, 1)]]
    shaped3_values: Array[float, Literal[(4, -1)]]
    shaped4_values: Array[float, Literal[(-1, 4)]]

    class Config:
        json_encoders = JSON_ENCODERS


m = Model(
    int_values=[1, 2, 3],
    any_values=[1, 'hello'],
    shaped1_values=np.array([1.1, 2.0]),
    shaped2_values=np.array([1.1, 2.0]),
    shaped3_values=np.array([1.1, 2.0, 2.0, 3.0]),
    shaped4_values=np.array([1.1, 2.0, 2.0, 3.0]),
)

print(m)


print(m.dict())

print(m.json(exclude={'shaped3_values'}))

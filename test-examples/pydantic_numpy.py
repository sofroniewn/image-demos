from dataclasses import field

import numpy as np
from pydantic.dataclasses import dataclass


def make_zeros():
    return np.zeros((32, 32), dtype=int)


class _ArrayMeta(type):
    def __getitem__(self, t):
        return type('Array', (Array,), {'__dtype__': t})


class Array(np.ndarray, metaclass=_ArrayMeta):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_type

    @classmethod
    def validate_type(cls, val):
        dtype = getattr(cls, '__dtype__', None)
        if isinstance(dtype, tuple):
            dtype, shape = dtype
        else:
            shape = tuple()

        result = np.array(val, dtype=dtype, copy=False, ndmin=len(shape))
        assert not shape or len(shape) == len(
            result.shape
        )  # ndmin guarantees this

        if any(
            (shape[i] != -1 and shape[i] != result.shape[i])
            for i in range(len(shape))
        ):
            result = result.reshape(shape)
        return result


class Config:
    validate_assignment = True
    arbitrary_types_allowed = True


# @dataclass(config=Config)
# class User:
#     id: int
#     name: str = 'John Doe'
#     image: Array[int, (32, 32)] = field(default_factory=make_zeros)

# user = User(id='42')
# print(user)

from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str = 'John Doe'
    image: Array[int, (32, 32)] = make_zeros()


user = User(id='42')
print(user)


user.image = np.ones((2, 2))
print(user)

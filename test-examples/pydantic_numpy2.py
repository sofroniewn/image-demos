import pydantic
import numpy


class _ArrayMeta(type):
    def __getitem__(self, t):
        return type('Array', (Array,), {'__dtype__': t})


class Array(numpy.ndarray, metaclass=_ArrayMeta):
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

        result = numpy.array(val, dtype=dtype, copy=False, ndmin=len(shape))
        assert not shape or len(shape) == len(result.shape)  # ndmin guarantees this

        if any((shape[i] != -1 and shape[i] != result.shape[i]) for i in range(len(shape))):
            result = result.reshape(shape)
        return result


def make_array():
    return np.zeros((2, 1))

class Model(pydantic.BaseModel):
    int_values: Array[float]
    any_values: Array
    shaped1_values: Array[float, (-1, )]
    shaped2_values: Array[int, (2, 1)]=pydantic.Field(default_factory=make_array)
    shaped3_values: Array[float, (4, -1)]
    shaped4_values: Array[float, (-1, 4)]

    class Config:
        validate_assignment = True


m = Model(
    int_values=[1, 2, 3],
    any_values=[1, 'hello'],
    shaped1_values=numpy.array([1.1, 2.0]),
    shaped2_values=numpy.array([1.1, 2.0]),
    shaped3_values=numpy.array([1.1, 2.0, 2.0, 3.0]),
    shaped4_values=numpy.array([1.1, 2.0, 2.0, 3.0]),
)
print(m.shaped2_values)

m.shaped2_values = numpy.random.random((2, 1))
print(m.shaped2_values)

print(m)

print(m.__fields__)





# class _ColorArraySingleMeta(type):
#     def __getitem__(self, t):
#         return type('ColorArraySingle', (ColorArraySingle,), {'__dtype__': t})


# class ColorArraySingle(Array, metaclass=_ColorArraySingleMeta):
#     @classmethod
#     def __get_validators__(cls):
#         print('pppp')
#         yield cls.validate_type

#     @classmethod
#     def validate_type(cls, val):
#         print('hiiiiii')
#         val = transform_single_color(val)
#         return super().validate_type(val)

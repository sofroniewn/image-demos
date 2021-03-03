import pydantic


class Base(pydantic.BaseModel):

    field: str

    class Config:
        allow_mutation = False
        use_enum_values = True
        extra = pydantic.Extra.forbid


class Mixin(pydantic.BaseModel):

    another_field: int = 0


class SubClass(Mixin, Base):

    yet_another_field: float = 0.1


assert pydantic.BaseModel.__config__.allow_mutation is True
assert pydantic.BaseModel.__config__.use_enum_values is False
assert pydantic.BaseModel.__config__.extra == pydantic.Extra.ignore

assert Base.__config__.allow_mutation is False
assert Base.__config__.use_enum_values is True
assert Base.__config__.extra == pydantic.Extra.forbid

assert SubClass.__config__.allow_mutation is False
assert SubClass.__config__.use_enum_values is True
assert SubClass.__config__.extra == pydantic.Extra.forbid  # FAILS HERE; RESET TO `ignore`
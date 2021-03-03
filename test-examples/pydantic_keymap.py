from typing import ClassVar, Any, Set, Dict, List

from pydantic import BaseModel, Field, PrivateAttr

from napari.utils.events import EventedModel
# from napari.utils.key_bindings import KeymapProvider
# from napari.utils.mouse_bindings import MousemapProviderMixin
from napari.utils.events.event import EmitterGroup, Event
from napari.utils.key_bindings import make_bind_key

class EventedModel(BaseModel):

    # add private attributes for event emission
    _events: EmitterGroup = PrivateAttr(default_factory=EmitterGroup)
    #__equality_checks__: Dict = PrivateAttr(default_factory=dict)
    __slots__: ClassVar[Set[str]] = {"__weakref__"}

    # pydantic BaseModel configuration.  see:
    # https://pydantic-docs.helpmanual.io/usage/model_config/
    class Config:
        # whether to allow arbitrary user types for fields (they are validated
        # simply by checking if the value is an instance of the type). If
        # False, RuntimeError will be raised on model declaration
        arbitrary_types_allowed = True
        # whether to perform validation on assignment to attributes
        validate_assignment = True
        # whether to treat any underscore non-class var attrs as private
        # https://pydantic-docs.helpmanual.io/usage/models/#private-model-attributes
        underscore_attrs_are_private = True
        # whether to populate models with the value property of enums, rather
        # than the raw enum. This may be useful if you want to serialise
        # model.dict() later
        use_enum_values = True
        # whether to validate field defaults (default: False)
        validate_all = True
        # a dict used to customise the way types are encoded to JSON
        # https://pydantic-docs.helpmanual.io/usage/exporting_models/#modeljson
        # allow extra attributes during model initialization, useful for mixins
        extra = 'allow'


class MousemapProviderMixin(EventedModel):
    """Mix-in to add mouse binding functionality.

    Attributes
    ----------
    mouse_move_callbacks : list
        Callbacks from when mouse moves with nothing pressed.
    mouse_drag_callbacks : list
        Callbacks from when mouse is pressed, dragged, and released.
    mouse_wheel_callbacks : list
        Callbacks from when mouse wheel is scrolled.
    """

    # Hold callbacks for when mouse moves with nothing pressed
    _mouse_move_callbacks: List = PrivateAttr(default_factory=list)
    # Hold callbacks for when mouse is pressed, dragged, and released
    _mouse_drag_callbacks: List = PrivateAttr(default_factory=list)
    # Hold callbacks for when mouse wheel is scrolled
    _mouse_wheel_callbacks: List = PrivateAttr(default_factory=list)

    _persisted_mouse_event: Dict = PrivateAttr(default_factory=dict)
    _mouse_drag_gen: Dict = PrivateAttr(default_factory=dict)
    _mouse_wheel_gen: Dict = PrivateAttr(default_factory=dict)


class KeymapProviderModel(MousemapProviderMixin):
    """Mix-in to add mouse binding functionality.

    Attributes
    ----------
    mouse_move_callbacks : list
        Callbacks from when mouse moves with nothing pressed.
    mouse_drag_callbacks : list
        Callbacks from when mouse is pressed, dragged, and released.
    mouse_wheel_callbacks : list
        Callbacks from when mouse wheel is scrolled.
    """

    keymap: Set = Field(default_factory=set)
    _class_keymap: ClassVar[Set] = PrivateAttr(default_factory=set)
    _bind_key: Any = PrivateAttr(default_factory=make_bind_key)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if 'class_keymap' not in cls.__dict__:
            # if in __dict__, was defined in class and not inherited
            cls._class_keymap = {}


class Axes(KeymapProviderModel):
    """Axes indicating world coordinate origin and orientation.

    Attributes
    ----------
    visible : bool
        If axes are visible or not.
    labels : bool
        If axes labels are visible or not. Not the actual
        axes labels are stored in `viewer.dims.axes_labels`.
    colored : bool
        If axes are colored or not. If colored then default
        coloring is x=cyan, y=yellow, z=magenta. If not
        colored than axes are the color opposite of
        the canvas background.
    dashed : bool
        If axes are dashed or not. If not dashed then
        all the axes are solid. If dashed then x=solid,
        y=dashed, z=dotted.
    arrows : bool
        If axes have arrowheads or not.
    """

    # fields
    visible: bool = False
    labels: bool = True
    colored: bool = True
    dashed: bool = False
    arrows: bool = True

a = Axes()
b = Axes()

print(a)
print(b)
print('a pre', a._mouse_drag_callbacks)
print('b post', b._mouse_drag_callbacks)
a._mouse_drag_callbacks.append(0)
print('a pre', a._mouse_drag_callbacks)
print('b post', b._mouse_drag_callbacks)

print('b post', b.keymap)

print(a.dict())
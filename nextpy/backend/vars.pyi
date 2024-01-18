# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Manually edited, do not regen."""
from dataclasses import dataclass
from _typeshed import Incomplete
from nextpy import constants as constants
from nextpy.base import Base as Base
from nextpy.backend.state import State as State
from nextpy.backend.state import BaseState as BaseState
from nextpy.utils import console as console, format as format, types as types
from nextpy.frontend.imports import ReactImportVar
from types import FunctionType
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Type,
    Union,
    _GenericAlias,  # type: ignore
)

USED_VARIABLES: Incomplete

def get_unique_variable_name() -> str: ...
def _encode_var(value: Var) -> str: ...
def _decode_var(value: str) -> tuple[VarData, str]: ...
def _extract_var_data(value: Iterable) -> list[VarData | None]: ...

class VarData(Base):
    state: str
    imports: dict[str, set[ReactImportVar]]
    hooks: set[str]
    @classmethod
    def merge(cls, *others: VarData | None) -> VarData | None: ...

class Var:
    _var_name: str
    _var_type: Type
    _var_is_local: bool = False
    _var_is_string: bool = False
    _var_full_name_needs_state_prefix: bool = False
    _var_data: VarData | None = None
    @classmethod
    def create(
        cls, value: Any, _var_is_local: bool = False, _var_is_string: bool = False
    ) -> Optional[Var]: ...
    @classmethod
    def create_safe(
        cls, value: Any, _var_is_local: bool = False, _var_is_string: bool = False
    ) -> Var: ...
    @classmethod
    def __class_getitem__(cls, type_: Type) -> _GenericAlias: ...
    def _replace(self, merge_var_data=None, **kwargs: Any) -> Var: ...
    def equals(self, other: Var) -> bool: ...
    def to_string(self) -> Var: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __getitem__(self, i: Any) -> Var: ...
    def __getattribute__(self, name: str) -> Var: ...
    def operation(
        self,
        op: str = ...,
        other: Optional[Var] = ...,
        type_: Optional[Type] = ...,
        flip: bool = ...,
        fn: Optional[str] = ...,
    ) -> Var: ...
    def compare(self, op: str, other: Var) -> Var: ...
    def __invert__(self) -> Var: ...
    def __neg__(self) -> Var: ...
    def __abs__(self) -> Var: ...
    def length(self) -> Var: ...
    def __eq__(self, other: Var) -> Var: ...
    def __ne__(self, other: Var) -> Var: ...
    def __gt__(self, other: Var) -> Var: ...
    def __ge__(self, other: Var) -> Var: ...
    def __lt__(self, other: Var) -> Var: ...
    def __le__(self, other: Var) -> Var: ...
    def __add__(self, other: Var) -> Var: ...
    def __radd__(self, other: Var) -> Var: ...
    def __sub__(self, other: Var) -> Var: ...
    def __rsub__(self, other: Var) -> Var: ...
    def __mul__(self, other: Var) -> Var: ...
    def __rmul__(self, other: Var) -> Var: ...
    def __pow__(self, other: Var) -> Var: ...
    def __rpow__(self, other: Var) -> Var: ...
    def __truediv__(self, other: Var) -> Var: ...
    def __rtruediv__(self, other: Var) -> Var: ...
    def __floordiv__(self, other: Var) -> Var: ...
    def __mod__(self, other: Var) -> Var: ...
    def __rmod__(self, other: Var) -> Var: ...
    def __and__(self, other: Var) -> Var: ...
    def __rand__(self, other: Var) -> Var: ...
    def __or__(self, other: Var) -> Var: ...
    def __ror__(self, other: Var) -> Var: ...
    def __contains__(self, _: Any) -> Var: ...
    def contains(self, other: Any) -> Var: ...
    def reverse(self) -> Var: ...
    def foreach(self, fn: Callable) -> Var: ...
    @classmethod
    def range(
        cls,
        v1: Var | int = 0,
        v2: Var | int | None = None,
        step: Var | int | None = None,
    ) -> Var: ...
    def to(self, type_: Type) -> Var: ...
    def as_ref(self) -> Var: ...
    @property
    def _var_full_name(self) -> str: ...
    def _var_set_state(self, state: Type[BaseState] | str) -> Any: ...

@dataclass(eq=False)
class BaseVar(Var):
    _var_name: str
    _var_type: Any
    _var_is_local: bool = False
    _var_is_string: bool = False
    _var_full_name_needs_state_prefix: bool = False
    _var_data: VarData | None = None
    def __hash__(self) -> int: ...
    def get_default_value(self) -> Any: ...
    def get_setter_name(self, include_state: bool = ...) -> str: ...
    def get_setter(self) -> Callable[[BaseState, Any], None]: ...

@dataclass(init=False)
class ComputedVar(Var):
    _var_cache: bool
    fget: FunctionType
    @property
    def _cache_attr(self) -> str: ...
    def __get__(self, instance, owner): ...
    def _deps(self, objclass: Type, obj: Optional[FunctionType] = ...) -> Set[str]: ...
    def mark_dirty(self, instance) -> None: ...
    def _determine_var_type(self) -> Type: ...
    def __init__(self, func) -> None: ...

def cached_var(fget: Callable[[Any], Any]) -> ComputedVar: ...

class CallableVar(BaseVar):
    def __init__(self, fn: Callable[..., BaseVar]): ...
    def __call__(self, *args, **kwargs) -> BaseVar: ...

from __future__ import annotations

from typing import Any, Dict

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

PossibleValue: TypeAlias = "bool | int | str | list[bool | int | str]"
ModulePath: TypeAlias = "LocalModulePath | BicepRegistryModulePath | TemplateSpecModulePath"
LoopType: TypeAlias = "LoopIndex | LoopArray | LoopArrayIndex | LoopObject"


class _ParameterAttributes(TypedDict):
    type: str
    default: PossibleValue | None
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Parameters(TypedDict):
    __name__: str
    __attrs__: _ParameterAttributes


class ParamResponse(TypedDict):
    parameters: _Parameters


class _VariableAttributes(TypedDict):
    value: PossibleValue
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Variables(TypedDict):
    __name__: str
    __attrs__: _VariableAttributes


class VarResponse(TypedDict):
    variables: _Variables


class _OutputAttributes(TypedDict):
    type: str
    value: PossibleValue
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Outputs(TypedDict):
    __name__: str
    __attrs__: _OutputAttributes


class OutputResponse(TypedDict):
    outputs: _Outputs


class _ResourceAttributes(TypedDict):
    type: str
    api_version: str
    config: Dict[str, Any]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Resources(TypedDict):
    __name__: str
    __attrs__: _ResourceAttributes


class ResourceResponse(TypedDict):
    resources: _Resources


class _ModuleAttributes(TypedDict):
    type: Literal["local"] | Literal["bicep_registry"] | Literal["template_spec"]
    detail: _LocalModulePathDetail | _BicepRegistryModulePathDetail | _TemplateSpecModulePathDetail
    config: Dict[str, Any]
    __start_line__: NotRequired[int]
    __end_line__: NotRequired[int]


class _Modules(TypedDict):
    __name__: str
    __attrs__: _ModuleAttributes


class ModuleResponse(TypedDict):
    modules: _Modules


class ApiTypeVersion(TypedDict):
    type: str
    api_version: str


####################
#
# Module Paths
#
####################


class _LocalModulePathDetail(TypedDict):
    full: str
    path: str


class LocalModulePath(TypedDict):
    type: Literal["local"]
    detail: _LocalModulePathDetail


class _BicepRegistryModulePathDetail(TypedDict):
    full: str
    registry_name: str
    path: str
    tag: str


class BicepRegistryModulePath(TypedDict):
    type: Literal["bicep_registry"]
    detail: _BicepRegistryModulePathDetail


class _TemplateSpecModulePathDetail(TypedDict):
    full: str
    subscription_id: str
    resource_group_id: str
    name: str
    version: str


class TemplateSpecModulePath(TypedDict):
    type: Literal["template_spec"]
    detail: _TemplateSpecModulePathDetail


####################
#
# Loops
#
####################


class _LoopIndexDetail(TypedDict):
    index_name: str
    start_index: str
    count: str


class LoopIndex(TypedDict):
    type: Literal["index"]
    detail: _LoopIndexDetail


class _LoopArrayDetail(TypedDict):
    item_name: str
    array_name: str


class LoopArray(TypedDict):
    type: Literal["array"]
    detail: _LoopArrayDetail


class _LoopArrayIndexDetail(TypedDict):
    item_name: str
    index_name: str
    array_name: str


class LoopArrayIndex(TypedDict):
    type: Literal["array_index"]
    detail: _LoopArrayIndexDetail


class _LoopObjectDetail(TypedDict):
    item_name: str
    object_name: str


class LoopObject(TypedDict):
    type: Literal["object"]
    detail: _LoopObjectDetail


class Loop(TypedDict):
    loop_type: LoopType
    condition: None
    config: Dict[str, Any]
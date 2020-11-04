from django.contrib.gis.geos.base import GEOSBase as GEOSBase
from typing import Any, Tuple, Union

PointType = Tuple[float, ...]

class GEOSCoordSeq(GEOSBase):
    ptr_type: Any = ...
    def __init__(self, ptr: Any, z: bool = ...) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def __getitem__(self, index: Any): ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def getOrdinate(self, dimension: int, index: int) -> float: ...
    def setOrdinate(self, dimension: int, index: int, value: float) -> None: ...
    def getX(self, index: int) -> float: ...
    def setX(self, index: int, value: float) -> None: ...
    def getY(self, index: int) -> float: ...
    def setY(self, index: int, value: float) -> None: ...
    def getZ(self, index: int): ...
    def setZ(self, index: int, value: float) -> None: ...
    @property
    def size(self) -> int: ...
    @property
    def dims(self) -> int: ...
    @property
    def hasz(self) -> bool: ...
    def clone(self) -> "GEOSCoordSeq": ...
    @property
    def kml(self) -> str: ...
    @property
    def tuple(self) -> Union[PointType, Tuple[PointType, ...]]: ...
    @property
    def is_counterclockwise(self) -> bool: ...

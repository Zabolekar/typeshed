# Stubs for multiprocessing

from typing import Any, Callable, Iterable, Mapping, Optional, Dict, List, Union, TypeVar

from logging import Logger
from multiprocessing.context import BaseContext
from multiprocessing.managers import SyncManager
from multiprocessing.pool import AsyncResult
from multiprocessing.process import current_process as current_process
import sys
import queue

_T = TypeVar('_T')

class Lock():
    def acquire(self, block: bool = ..., timeout: int = ...) -> None: ...
    def release(self) -> None: ...
    def __enter__(self) -> 'Lock': ...
    def __exit__(self, exc_type, exc_value, tb) -> None: ...

class Event(object):
    def __init__(self, *, ctx: BaseContext) -> None: ...
    def is_set(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def wait(self, timeout: Optional[int] = ...) -> bool: ...

class Pool():
    def __init__(self, processes: Optional[int] = ...,
                 initializer: Optional[Callable[..., None]] = ...,
                 initargs: Iterable[Any] = ...,
                 maxtasksperchild: Optional[int] = ...,
                 context: Optional[Any] = None) -> None: ...
    def apply(self,
              func: Callable[..., Any],
              args: Iterable[Any] = ...,
              kwds: Dict[str, Any]=...) -> Any: ...
    def apply_async(self,
                func: Callable[..., Any],
                args: Iterable[Any] = ...,
                kwds: Dict[str, Any] = ...,
                callback: Optional[Callable[..., None]] = None,
                error_callback: Optional[Callable[[BaseException], None]] = None) -> AsyncResult: ...
    def map(self,
            func: Callable[..., Any],
            iterable: Iterable[Any] = ...,
            chunksize: Optional[int] = ...) -> List[Any]: ...
    def map_async(self, func: Callable[..., Any],
                  iterable: Iterable[Any] = ...,
                  chunksize: Optional[int] = ...,
                  callback: Optional[Callable[..., None]] = None,
                  error_callback: Optional[Callable[[BaseException], None]] = None) -> AsyncResult: ...
    def imap(self,
             func: Callable[..., Any],
             iterable: Iterable[Any] = ...,
             chunksize: Optional[int] = None) -> Iterable[Any]: ...
    def imap_unordered(self,
                       func: Callable[..., Any],
                       iterable: Iterable[Any] = ...,
                       chunksize: Optional[int] = None) -> Iterable[Any]: ...
    def starmap(self,
                func: Callable[..., Any],
                iterable: Iterable[Iterable[Any]] = ...,
                chunksize: Optional[int] = None) -> List[Any]: ...
    def starmap_async(self,
                      func: Callable[..., Any],
                      iterable: Iterable[Iterable[Any]] = ...,
                      chunksize: Optional[int] = ...,
                      callback: Optional[Callable[..., None]] = None,
                      error_callback: Optional[Callable[[BaseException], None]] = None) -> AsyncResult: ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...
    def join(self) -> None: ...
    def __enter__(self) -> 'Pool': ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

class Process():
    name: str
    daemon: bool
    pid: Optional[int]
    exitcode: Optional[int]
    authkey: bytes
    sentinel: int
    # TODO: set type of group to None
    def __init__(self,
                 group: Any = ...,
                 target: Optional[Callable] = ...,
                 name: Optional[str] = ...,
                 args: Iterable[Any] = ...,
                 kwargs: Mapping[Any, Any] = ...,
                 *,
                 daemon: Optional[bool] = ...) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def terminate(self) -> None: ...
    def is_alive(self) -> bool: ...
    def join(self, timeout: Optional[float] = ...) -> None: ...

class Queue(queue.Queue[_T]):
    def __init__(self, maxsize: int = ...) -> None: ...
    def get(self, block: bool = ..., timeout: Optional[float] = ...) -> _T: ...
    def put(self, item: _T, block: bool = ..., timeout: Optional[float] = ...) -> None: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def put_nowait(self, item: _T) -> None: ...
    def get_nowait(self) -> _T: ...
    def close(self) -> None: ...
    def join_thread(self) -> None: ...
    def cancel_join_thread(self) -> None: ...

class Value():
    value: Any = ...
    def __init__(self, typecode_or_type: str, *args: Any, lock: bool = ...) -> None: ...

# ----- multiprocessing function stubs -----
def active_children() -> List[Process]: ...
def allow_connection_pickling() -> None: ...
def cpu_count() -> int: ...
def freeze_support() -> None: ...
def get_logger() -> Logger: ...
def log_to_stderr(level: Optional[Union[str, int]] = ...) -> Logger: ...
def Manager() -> SyncManager: ...
def set_forkserver_preload(module_names: List[str]) -> None: ...
if sys.platform == 'win32' or sys.version_info >= (3, 4):
    def set_executable(executable: str) -> None: ...
if sys.version_info >= (3, 4):
    def get_all_start_methods() -> List[str]: ...
    def get_context(method: Optional[str] = ...) -> BaseContext: ...
    def get_start_method(allow_none: Optional[bool]) -> Optional[str]: ...
    def set_start_method(method: str, force: Optional[bool] = ...) -> None: ...

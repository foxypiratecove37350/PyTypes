"""PyTypes: Enhanced Python with static/runtime type checking and new language features

Author: foxy pirate cove / Fnaf
License: GNU General Public License v2.0 only (GPL-2.0)
Version: 3.13.1

User API
"""

from collections.abc import Callable
from typing import Any, NoReturn


class _AutoMeta(type):
	"""Metaclass for Auto"""

	def __instancecheck__(self, obj: object) -> NoReturn:
		raise TypeError('Auto cannot be used with isinstance()')
	
	def __subclasscheck__(self, cls: type) -> NoReturn:
		raise TypeError('Auto cannot be used with issubclass()')
	
	def __repr__(self) -> str:
		return 'Auto'


class Auto(metaclass=_AutoMeta):
	"""Special type indicating automatic detection of the type"""

	def __new__(cls, *args, **kwargs) -> NoReturn:
		raise TypeError('Auto cannot be instantiated')


def disable_type_enforcement(func: Callable) -> Callable:
	"""Disable runtime type enforcement for a function"""
	
	def wrapper(*args: Any, **kwargs: Any) -> Any:
		return func(*args, **kwargs)

	return wrapper


def enable_type_enforcement(func: Callable) -> Callable:
	"""Enable runtime type enforcement for a function"""
	
	def wrapper(*args: Any, **kwargs: Any) -> Any:
		return func(*args, **kwargs)

	return wrapper


def weaken_type_enforcement(func: Callable) -> Callable:
	"""Weaken runtime type enforcement for a function"""
	
	def wrapper(*args: Any, **kwargs: Any) -> Any:
		return func(*args, **kwargs)

	return wrapper

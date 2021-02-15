import inspect
from typing import Union


class ARBool(int):

	def __init__(self, x):
		if isinstance(x, int):
			super().__init__(x)
		elif isinstance(x, str):
			if x.upper() == 'TRUE':
				super().__init__(1)
			elif x.upper() == 'FALSE':
				super().__init__(0)

		super().__init__(x)


class DynamicType:

	def __init__(self, *arg, **kwargs):
		for k in kwargs:
			target_type = get_type(self, k)
			if not issubclass(target_type, DynamicType):
				setattr(self, k, target_type(kwargs[k]))
			else:
				setattr(self, k, target_type(**kwargs[k]))


def get_type(obj: Union[object, type], attr_name):
	if isinstance(obj, object):
		return inspect.getmembers(obj.__class__, lambda a: not (inspect.isroutine(a)))[0][1].get(attr_name, None)
	return inspect.getmembers(obj, lambda a: not (inspect.isroutine(a)))[0][1].get(attr_name, None)

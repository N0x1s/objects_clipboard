from collections import deque
import pyperclip
import pickle
import sys

class ObjectsClipboard:
	def __init__(self, capacity=None, obj_maxsize=None):
		self.storage = deque(maxlen=capacity)
		self.obj_maxsize = obj_maxsize

	def store(self, item, copy=False):
		if self.obj_maxsize is not None:
			if sys.getsizeof(item) > self.obj_maxsize:
				raise ValueError('The Object size is larger than the max size')
		self.storage.append(item)
		if copy:
			self.copy()

	def copy(self, item=-1):
		if self.storage:
			data = pickle.dumps(self.storage[item])
			pyperclip.copy(data.hex())
			return True
		return False

	@staticmethod
	def paste():
		data = pyperclip.paste()
		try:
			return pickle.loads(bytes.fromhex(data))
		except:
			e = 'The object is not valid make sure you copied the right data'
			raise ValueError(e)

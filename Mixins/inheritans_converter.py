"""https://dzen.ru/video/watch/67efb94979635210ae4012ea"""
class TempMixin:
	"""Convert temperature from metric to impterial and revert."""
	@staticmethod
	def f_to_c(f:float) -> float:
		"""Convert from imperial to metric."""
		return (f - 32) / 1.8

	@staticmethod
	def c_to_f(c: float) -> float:
		"""Convert metric to inmperial."""
		return (c * 1.8) + 32

class DigitalStoreMixin:
	"""Convert digital valies."""
	@staticmethod
	def gb_to_mb(gb: int) -> int:
		return gb * 1000

	@staticmethod
	def mb_to_gb(mb: int) -> float:
		return mb / 1000

class HardDrive(TempMixin, DigitalStoreMixin):
	"""Computer hard drive."""
	def __init__(self, space: int, celsius:int) -> None:
		"""Inintialize drive status."""
		self._space = space
		self._celsius = celsius


	def status(self, metric=True) -> None:
		"""Display drive status."""
		temp = self._celsius if metric else self.c_to_f(self._celsius)
		space = self.mb_to_gb(self._space)

		print(f'Space: {space} GB, Temp: {temp} {'C' if metric else 'F'}')

hd = HardDrive(8000000, 22)
hd.status()
hd.status(metric = False)

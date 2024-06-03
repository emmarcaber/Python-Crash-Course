class Employee:
	"""A class for Employee."""

	def __init__(self, first, last, annual_salary):
		"""Initialize the attributes of an employee."""
		self.first = first
		self.last = last
		self.annual_salary = annual_salary

	def give_raise(self, raise_amount=5000):
		"""Raise the annual salary."""
		self.annual_salary += raise_amount
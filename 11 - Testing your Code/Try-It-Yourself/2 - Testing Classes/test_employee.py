import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee."""

	def setUp(self):
		"""Create an employee to use on all test methods."""
		self.employee = Employee("Emmar", "Caber", 15000)

	def test_give_default_raise(self):
		"""Test that the annual salary will increase 5000."""
		self.employee.give_raise()
		self.assertEqual(20000, self.employee.annual_salary)

	def test_give_custom_raise(self):
		"""Test that the annual salary will increase by a given value."""
		self.employee.give_raise(10000)
		self.assertEqual(25000, self.employee.annual_salary)


if __name__ == '__main__':
	unittest.main()
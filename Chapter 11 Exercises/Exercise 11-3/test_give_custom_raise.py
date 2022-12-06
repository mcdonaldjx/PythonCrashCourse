def test_give_custom_raise(self):
  employee = Employee('jared','m','88000')
  pre_bonus = employee.salary
  print(f"Salary before raise: {pre_bonus}")
  employee.give_raise(32000)
  assert employee.salary == (pre_bonus+32000)

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.white_box import *

class TestFunctions(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(100))
        self.assertFalse(is_even(-3))

    def test_divide(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(8, 1), 8)
        self.assertEqual(divide(9, 3), 3)

    def test_get_grade(self):
        self.assertEqual(get_grade(90), "A")
        self.assertEqual(get_grade(80), "B")
        self.assertEqual(get_grade(70), "C")
        self.assertEqual(get_grade(69), "F")

    def test_is_triangle(self):
        self.assertEqual(is_triangle(6, 8, 10), "Yes, it's a triangle!")
        self.assertEqual(is_triangle(1, 1, 2), "No, it's not a triangle.")

    def test_check_number_status(self):
        self.assertEqual(check_number_status(50), "Positive")
        self.assertEqual(check_number_status(-15), "Negative")
        self.assertEqual(check_number_status(0), "Zero")

    def test_validate_password(self):
        self.assertTrue(validate_password("FuerteP@ss1"))
        self.assertFalse(validate_password("solopassword"))
        self.assertFalse(validate_password("ALLUPPERCASE1!"))

    def test_calculate_total_discount(self):
        self.assertEqual(calculate_total_discount(99), 0)
        self.assertEqual(calculate_total_discount(200), 20)
        self.assertEqual(calculate_total_discount(1000), 200)

    def test_calculate_order_total(self):
        items = [{"quantity": 10, "price": 15}]
        self.assertEqual(calculate_order_total(items), 142.5)

    def test_validate_email(self):
        self.assertEqual(validate_email("correo.valido@dominio.com"), "Valid Email")
        self.assertEqual(validate_email("sin_arroba.com"), "Invalid Email")

class TestClasses(unittest.TestCase):
    def test_vending_machine(self):
        vm = VendingMachine()
        self.assertEqual(vm.insert_coin(), "Coin Inserted. Select your drink.")
        self.assertEqual(vm.insert_coin(), "Invalid operation in current state.")
        self.assertEqual(vm.select_drink(), "Drink Dispensed. Thank you!")
        self.assertEqual(vm.select_drink(), "Invalid operation in current state.")

    def test_traffic_light(self):
        tl = TrafficLight()
        self.assertEqual(tl.get_current_state(), "Red")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Green")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Yellow")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Red")

    def test_bank_account(self):
        account = BankAccount("12345", 0)
        self.assertEqual(account.account_number, "12345")
        self.assertEqual(account.balance, 0)
        account = BankAccount("67890", 9999999)
        self.assertEqual(account.balance, 9999999)

    def test_shopping_cart(self):
        cart = ShoppingCart()
        product1 = Product("Laptop", 1200)
        product2 = Product("Mouse", 25)
        cart.add_product(product1, 1)
        cart.add_product(product2, 5)
        self.assertEqual(len(cart.items), 2)
        self.assertEqual(cart.items[1]["quantity"], 5)
        cart.remove_product(product2, 3)
        self.assertEqual(cart.items[1]["quantity"], 2)

if __name__ == "__main__":
    unittest.main()

from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):

        if not self.pesel.isdigit() or len(self.pesel) != 11:
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        digits = [int(d) for d in str(self.pesel)]

        # print("cyfry z peselu", digits)

        control_I = []
        for i in range(0, 10):
            control_I.insert(i, weights[i] * digits[i])

        # print("control_I", control_I)

        control_S = sum(control_I)
        control_M = control_S % 10

        # print("control_S", control_S)
        # print("control_M", control_M)

        if control_M == 0:
            control_number = 0
        else:
            control_number = 10 - control_M;

        if control_number == digits[10]:
            return True
        return False

    def field_name(self):
        return RegisterFormFields.PESEL
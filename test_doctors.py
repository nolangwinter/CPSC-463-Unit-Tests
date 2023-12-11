import odoo
from odoo.tests import TransactionCase


# @odoo.tests.tagged("-standard", "hospital")
class TestDoctor(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestDoctor, cls).setUpClass()

        cls.doctor = cls.env['hospital.doctor'].create({
            "doctor_name": "Nolan Winter",
            "age": 50
        })

    def test_create_doctor(self):
        self.assertEqual(self.doctor.doctor_name, "Nolan Winter")
        self.assertEqual(self.doctor.age, 50)
        # checking if the default values are working correctly
        self.assertEqual(self.doctor.gender, "male")
        self.assertTrue(self.doctor.active)

    def test_copying_doctor(self):
        copy_doctor = self.doctor.copy()
        # checking the default values for copying a doctor's record
        self.assertEqual(copy_doctor.doctor_name, "Nolan Winter (Copy)")
        self.assertEqual(copy_doctor.note, "Copied Record")

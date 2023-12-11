import odoo
from odoo.tests import TransactionCase


class TestPatients(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestPatients, cls).setUpClass()

        cls.patient = cls.env['hospital.patient'].create({
            "name": "Nolan Winter",
            "age": 23,
        })

    def test_create_patient(self):
        self.assertEqual(self.patient.name, "Nolan Winter")
        self.assertEqual(self.patient.age, 23)
        # checking the default values
        self.assertEqual(self.patient.gender, "male")

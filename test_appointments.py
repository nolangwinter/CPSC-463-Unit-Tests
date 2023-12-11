import odoo
from odoo.tests import TransactionCase


class TestAppointments(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestAppointments, cls).setUpClass()

        cls.doctor = cls.env['hospital.doctor'].create({
            'doctor_name': "Test Doctor",
            'age': 50,
        })

        cls.patient = cls.env['hospital.patient'].create({
            'name': "Test Patient",
            'age': 25
        })

    def test_create_appointments(self):
        patient_id = self.patient.id
        doctor_id = self.doctor.id

        created_appointment = self.env["hospital.appointment"].create({
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'name': "Test Appointment",
            'note': "Note",
            'date_appointment': "2023-12-10",
        })

        self.assertEqual(created_appointment.patient_id, self.patient)
        self.assertEqual(created_appointment.doctor_id, self.doctor)
        self.assertEqual(created_appointment.name, "Test Appointment")

    def test_confirm_appointment(self):
        patient_id = self.patient.id
        doctor_id = self.doctor.id

        created_appointment = self.env["hospital.appointment"].create({
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'name': "Test Appointment",
            'note': "Note",
            'date_appointment': "2023-12-10",
        })

        created_appointment.action_confirm()
        self.assertEqual(created_appointment.state, "confirm")
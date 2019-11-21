import unittest

class test_Patient(unittest.TestCase):
    
    def test_parse_patients_from_file(self):

        # Create new objects to be passed on to the function to test
        filename = "features_filt_3.csv"

        # Use the function to test
        patients = parse_patients_from_file(filename)

        # Assert the values returned by the function to test
        assertIsInstance(patients, Patient, msg="Returned object patients is not an instance of a Patient class")
        assertEqual(len(patients.get_features()), 9)

    def test_get_outcome(self):
        
        # Create new objects to be passed on to the function to test
        patient = Patient(50, 0, 1, 62, 50.33, 0, 1.75, 27.3,3,2,6152,38.81,3,28766)

        # Use the function to test
        patient_outcome = get_outcome(patient)

        # Assert the values returned by the function to test
        assertEqual(patient_outcome, 0, msg = "Patient outcome is not correctly matched")

    def test_get_features(self):
        
        # Create new objects to be passed on to the function to test
        patient = Patient(50, 0, 1, 62, 50.33, 0, 1.75, 27.3,3,2,6152,38.81,3,28766)

        # Use the function to test
        patient_features = get_features(patient)

        # Assert the values returned by the function to test
        assertEqual(patient_features[0], 50.33, msg = "Patient age is not correctly matched")
        assertEqual(patient_features[1], 0, msg = "Patient sex is not correctly matched")
        assertEqual(patient_features[2], 1.75, msg = "Patient los is not correctly matched")
        assertEqual(patient_features[3], 27.3, msg = "Patient bmi is not correctly matched")
        assertEqual(patient_features[4], 3, msg = "Patient comorbidity is not correctly matched")
        assertEqual(patient_features[5], 3, msg = "Patient additives is not correctly matched")
        assertEqual(patient_features[6], 2, msg = "Patient procedures is not correctly matched")
        assertEqual(patient_features[7], 6152, msg = "Patient duration of medications is not correctly matched")
        assertEqual(patient_features[8], 38.831, msg = "Patient percentage of lab events is not correctly matched")

    def test_get_feature(self):

         # Create new objects to be passed on to the function to test
        patient = Patient(50, 0, 1, 62, 50.33, 0, 1.75, 27.3,3,2,6152,38.81,3,28766)

        # Use the function to test
        patient_id = patient.get_feature(patient_id)
        outcome = patient.get_feature(outcome)
        icustay_sequence = patient.get_feature(icustay_sequence)
        icustay_id = patient.get_feature(icustay_id)
        age = patient.get_feature(age)
        sex = patient.get_feature(sex)
        length_of_hospital = patient.get_feature(length_of_hospital)
        bmi = patient.get_feature(bmi)
        number_of_additives = patient.get_feature(number_of_additives)
        number_of_procedures = patient.get_feature(number_of_procedures)
        duration_of_medications = patient.get_feature(duration_of_medications)
        percentage_of_abnormal_lab_events = patient.get_feature(percentage_of_abnormal_lab_events)
        comorbidity_score = patient.get_feature(comorbidity_score)
        hospital_admission_id = patient.get_feature(hospital_admission_id)

        # Assert the values returned by the function to test       
        assertEqual(patient_id, 50, msg = "Patient patient_id is not correctly matched")
        assertEqual(outcome, 0, msg = "Patient outcome is not correctly matched")
        assertEqual(icustay_sequence, 1, msg = "Patient icustay_sequence is not correctly matched")
        assertEqual(icustay_id, 62, msg = "Patient icustay_id is not correctly matched")
        assertEqual(age, 50.33, msg = "Patient age is not correctly matched")
        assertEqual(sex, 0, msg = "Patient sex is not correctly matched")
        assertEqual(length_of_hospital, 1.75, msg = "Patient length_of_hospital is not correctly matched")
        assertEqual(bmi, 27.3, msg = "Patient bmi is not correctly matched")
        assertEqual(number_of_additives, 3, msg = "Patient number_of_additives is not correctly matched")
        assertEqual(number_of_procedures, 2, msg = "Patient number_of_procedures is not correctly matched")
        assertEqual(duration_of_medications, 6152, msg = "Patient duration_of_medications is not correctly matched")
        assertEqual(percentage_of_abnormal_lab_events, 38.81, msg = "Patient percentage_of_abnormal_lab_events is not correctly matched")
        assertEqual(comorbidity_score, 3, msg = "Patient comorbidity_score is not correctly matched")
        assertEqual(hospital_admission_id, 28766, msg = "Patient hospital_admission_id is not correctly matched")


        items = [
            ('patient_id', 50),
            ('icustay_sequence', 1),
            ...
        ]

        for item in items:
            message = item[0] + ' is not equal'
            self.assertEqual(item[0], item[1], msg=message)


    def test_has_feature(self):

         # Create new objects to be passed on to the function to test
        patient = Patient(50, 0, 1, 62, 50.33, 0, 1.75, 27.3,3,2,6152,38.81,3,28766)

        # Use the function to test
        patient_id = patient.has_feature(patient_id)
        outcome = patient.get_feature(outcome)
        icustay_sequence = patient.get_feature(icustay_sequence)
        icustay_id = patient.get_feature(icustay_id)
        age = patient.get_feature(age)
        sex = patient.get_feature(sex)
        length_of_hospital = patient.get_feature(length_of_hospital)
        bmi = patient.get_feature(bmi)
        number_of_additives = patient.get_feature(number_of_additives)
        number_of_procedures = patient.get_feature(number_of_procedures)
        duration_of_medications = patient.get_feature(duration_of_medications)
        percentage_of_abnormal_lab_events = patient.get_feature(percentage_of_abnormal_lab_events)
        comorbidity_score = patient.get_feature(comorbidity_score)
        hospital_admission_id = patient.get_feature(hospital_admission_id)

        # Assert the values returned by the function to test       
        assertTrue(patient_id, msg = "Patient patient_id is not correctly matched")
        assertTrue(outcome, msg = "Patient outcome is not correctly matched")
        assertTrue(icustay_sequence, msg = "Patient icustay_sequence is not correctly matched")
        assertTrue(icustay_id, msg = "Patient icustay_id is not correctly matched")
        assertTrue(age, msg = "Patient age is not correctly matched")
        assertTrue(sex, msg = "Patient sex is not correctly matched")
        assertTrue(length_of_hospital, msg = "Patient length_of_hospital is not correctly matched")
        assertTrue(bmi, msg = "Patient bmi is not correctly matched")
        assertTrue(number_of_additives, msg = "Patient number_of_additives is not correctly matched")
        assertTrue(number_of_procedures, msg = "Patient number_of_procedures is not correctly matched")
        assertTrue(duration_of_medications, msg = "Patient duration_of_medications is not correctly matched")
        assertTrue(percentage_of_abnormal_lab_events, msg = "Patient percentage_of_abnormal_lab_events is not correctly matched")
        assertTrue(comorbidity_score, msg = "Patient comorbidity_score is not correctly matched")
        assertTrue(hospital_admission_id, msg = "Patient hospital_admission_id is not correctly matched")

    def test_compute_distance(self):

        # Create new objects to be passed on to the function to test
        patient1 = Patient(50, 0, 1, 62, 50.33, 0, 1.75, 27.3,3,2,6152,38.81,3,28766)
        patient2 = Patient(78, 1, 1, 89, 48.63, 1, 1.33, 23.3,2,1,2125,35.75,3,15161)

        # Use the function to test           
        distance = patient1.compute_distance(patient2)

        # Assert the values returned by the function to test  
        assertEqual(distance, 2.2674392697169483, msg = "The distance between both patients is incorrect")

if __name__ == '__main__':
    unittest.main()
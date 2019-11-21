import unittest
from patients import Patient
from KDTree import KDTree

class test_Patient(unittest.TestCase):
    
    def setUp(self):
        self._patient = Patient(3,0,1,4,0.405688678794769,0,-0.060390322941387,-0.058097454503978,10,6,-0.063210369053854,-1.36630588799408,2,2075,2)
        self._features_values = (3,0,1,4,0.405688678794769,0,-0.060390322941387,-0.058097454503978,10,6,-0.063210369053854,-1.36630588799408,2,2075,2)
        self._features_names = ['patient_id', 'outcome', 'icustay_sequence', 'icustay_id', 'age', 'sex', 'length_of_hospital', 'bmi', 'number_of_additives', 
        'number_of_procedures', 'duration_of_medications', 'percentage_of_abnormal_lab_events', 'comorbidity_score', 'hospital_admission_id', 'medication_count']
        self._10_features_values = (0.405688678794769, 0, -0.060390322941387, -0.058097454503978, 10, 6, -0.063210369053854, -1.36630588799408, 2, 2)
        self._10_features_names = ['age', 'sex', 'length_of_hospital', 'bmi', 'number_of_additives', 'number_of_procedures', 'duration_of_medications', 
        'percentage_of_abnormal_lab_events', 'comorbidity_score', 'medication_count']
        self._patient2 = Patient(12,1,1,13,0.142910335491309,0,0.112248064759934,0,3,10,-0.092820258686727,0.823508270528826,2,12532,2)
    
    def test_parse_patients_from_file(self):

        # Create new objects to be passed on to the function to test
        filename = "test_patients.csv"

        # Use the function to test
        patients = Patient.parse_patients_from_file(filename)

        # Assert the values returned by the function to test
        self.assertIsInstance(patients[0], Patient, msg="Returned object patients is not an instance of a Patient class")
        self.assertEqual(len(patients[0].get_features()), 10)

    def test_get_outcome(self):

        patient_outcome = self._patient.get_outcome()
        self.assertEqual(patient_outcome, 0, msg = "Patient outcome is not correctly matched")

    def test_get_features(self):
        
        patient_features = self._patient.get_features()

        # Make tuple of: ("feature name", obtained feature value, expected feature value)
        tuple_of_features = tuple(zip(self._10_features_names,patient_features,self._10_features_values))
        # Assert if values are correct
        for feature in tuple_of_features:
            message = 'Patient ' + feature[0] + ' is not equal'
            self.assertEqual(feature[1],feature[2], msg=message)

    def test_get_feature(self):

        #print(self._patient.get_feature("hospital_admission_id"))
        # Somehow hospital_admission_id feature is a tuple?????????????? (2075,)
        
        # Obtain feature values from patient and store them
        list_of_features = []
        for feature in self._features_names:
            if feature == 'hospital_admission_id':
                list_of_features.append(self._patient.get_feature(feature)[0])
            else:
                feat = self._patient.get_feature(feature)
                list_of_features.append(feat)
        # Make tuple of: ("feature name", obtained feature value, expected feature value)
        tuple_of_features = tuple(zip(self._features_names,list_of_features,self._features_values))
        # Assert if values are correct
        for feature in tuple_of_features:
            message = 'Patient ' + feature[0] + ' is not equal'
            self.assertEqual(feature[1],feature[2], msg=message)

    def test_has_feature(self):

        for feature in self._features_names:
            has_feature = self._patient.has_feature(feature)
            message = 'Patient ' + feature + ' is not equal'

        self.assertTrue(has_feature, msg = message)


    def test_compute_distance(self):
          
        distance = self._patient.compute_distance(self._patient2)
        self.assertEqual(distance, 8.36052597503702, msg = "The distance between both patients is incorrect")

if __name__ == '__main__':
    unittest.main()
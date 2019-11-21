import unittest

class test_KDTree(unittest.TestCase):
    
    def test_build(self):

        # Create new objects to be passed on to the function to test
        patients = [ 
                Patient(50, 0, 1, 62, 50.33, 0, 1.75, 27.3,3,2,6152,38.81,3,28766)
                Patient(78, 1, 1, 89, 48.63, 1, 1.33, 23.3,2,1,2125,35.75,3,15161)
                Patient(23, 0, 1, 33, 38.23, 1, 2.31, 30.1,1,3,1231,33.75,2,17231)
                Patient(15, 1, 1, 45, 48.63, 1, 1.89, 29.8,1,1,4533,39.11,1,37273)
                     ]

        patients.append(patient1)
        patients.append(patient2)

        # Use the function to test
        kdtree = build(patients)

        #kdtree.get_left_tree()
        #kdtree.get_right_tree()
        median_index = 4 // 2
        median_patient = patients[median_index]

        # Assert the values returned by the function to test
        self.assertEqual(median_patient, kdtree.get_value())

    def test_predict_outcome(self):

        # Create new objects to be passed on to the function to test
        patient = Patient(50, 0, 1, 62, 50.33, 0, 1.75, 27.3,3,2,6152,38.81,3,28766)
        max_distance = 10000
        max_distance_in_grouping = 1000

        # Use the function to test
        outcome = predict_outcome(patient,max_distance, max_patients_in_grouping)

        # We cannot assert if this is correct (because it is a prediction), but we will assert the object type
        self.assertIn(outcome, [0,1])


    def create_grouping(self):
        self. 

    def _create_grouping(self):
        self.
    def _get_branches(self):
        self.
    def _should_check_unchosen_branch(self):
        self.


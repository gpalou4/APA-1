import unittest
from Patient import Patient
from KDTree import KDTree

class test_KDTree(unittest.TestCase):
    def setUp(self):
        self._patient = Patient(1, 48, 0, 1.51, 28.1, 2, 2, 3, 1010, 37.99, 2)

        self._patient1 = Patient(0, 50.33, 0, 1.75, 27.3, 3, 3, 2, 6152, 38.81, 3)
        self._patient2 = Patient(1, 48.63, 1, 1.33, 23.3, 2, 1, 2, 2125, 35.75, 3)
        self._patient3 = Patient(1, 38.23, 1, 2.31, 30.1, 1, 3, 1, 1231, 33.75, 2)
        self._patient4 = Patient(1, 48.63, 1, 1.89, 29.8, 1, 1, 2, 4533, 39.11, 1)

        patients = [
            self._patient1,
            self._patient2,
            self._patient3,
            self._patient4
        ]

        self._kd_tree = KDTree.build(patients)


    def test_build(self):
        self.assertEqual(self._kd_tree.get_value(), self._patient4)
        self.assertEqual(self._kd_tree.get_index(), 0)

        left_tree = self._kd_tree.get_left_tree()
        left_tree_value = left_tree.get_value()
        self.assertEqual(left_tree_value, self._patient2)
        self.assertEqual(left_tree.get_index(), 1)
        self.assertIsNone(left_tree.get_right_tree())

        left_tree_leaf = left_tree.get_left_tree()
        self.assertTrue(left_tree_leaf.is_leaf())
        self.assertEqual(left_tree_leaf.get_index(), 2)
        self.assertEqual(left_tree_leaf.get_value(), self._patient3)

        right_tree = self._kd_tree.get_right_tree()
        right_tree_value = right_tree.get_value()
        self.assertTrue(right_tree.is_leaf())
        self.assertEqual(right_tree.get_index(), 1)
        self.assertEqual(right_tree_value, self._patient1)

    def test_build_without_patients(self):
        kd_tree = KDTree.build([])
        self.assertIsNone(kd_tree)

    def test_create_grouping_with_0_max_distance(self):
        grouping = self._kd_tree.create_grouping(self._patient, 0, 3)
        self.assertEqual(grouping, [])

    def test_create_grouping_with_0_max_patients_in_grouping(self):
        grouping = self._kd_tree.create_grouping(self._patient, 10, 0)
        self.assertEqual(grouping, [])

    def test_create_grouping_with_large_max_distance_and_large_max_patients_in_grouping(self):
        grouping = self._kd_tree.create_grouping(self._patient, 10000, 5)
        self.assertEqual(len(grouping), 4)

    def test_get_chosen_and_unchosen_branches_value_is_less_than(self):
        left_tree = KDTree()
        right_tree = KDTree()
        kd_tree = KDTree(self._patient1, 0, left_tree, right_tree)

        chosen_tree, unchosen_tree = kd_tree._get_chosen_and_unchosen_branches(self._patient)
        self.assertEqual(chosen_tree, left_tree)
        self.assertEqual(unchosen_tree, right_tree)

    def test_get_chosen_and_unchosen_branches_value_is_greater_than(self):
        left_tree = KDTree()
        right_tree = KDTree()
        kd_tree = KDTree(self._patient3, 0, left_tree, right_tree)

        chosen_tree, unchosen_tree = kd_tree._get_chosen_and_unchosen_branches(self._patient)
        self.assertEqual(chosen_tree, right_tree)
        self.assertEqual(unchosen_tree, left_tree)

    def test_should_check_unchosen_branch_with_no_nearest_patients(self):
        self.assertTrue(
            self._kd_tree._should_check_unchosen_branch(self._patient, [], (), 5)
        )

    def test_should_check_unchosen_branch_with_region_closer_than_farthest_nearest_patient(self):
        self.assertTrue(
            self._kd_tree._should_check_unchosen_branch(self._patient, [(2, self._patient3)], (), 1)
        )

    def test_add_nearest_patient_no_nearest_patients(self):
        distance = 1
        nearest_patients = []
        self._kd_tree._add_nearest_patient(distance, nearest_patients, 2)
        self.assertEqual(nearest_patients, [(-distance, self._patient4)])

    def test_add_nearest_patient_with_farther_distance(self):
        distance = 2
        nearest_patients = [(-1, self._patient3)]
        self._kd_tree._add_nearest_patient(distance, nearest_patients, 3)
        self.assertEqual(nearest_patients, [(-distance, self._patient4), (-1, self._patient3)])

    def test_add_nearest_patient_with_max_patients_and_farther_distance(self):
        distance = 2
        nearest_patients = [(-1, self._patient3), (0, self._patient2)]
        self._kd_tree._add_nearest_patient(distance, nearest_patients, 2)
        self.assertEqual(nearest_patients, [(-1, self._patient3), (0, self._patient2)])

    def test_add_nearest_patient_with_max_patients_and_closer_distance(self):
        distance = 0.5
        nearest_patients = [(-1, self._patient3), (0, self._patient2)]
        self._kd_tree._add_nearest_patient(distance, nearest_patients, 2)
        self.assertEqual(nearest_patients, [(-0.5, self._patient4), (0, self._patient2)])

if __name__ == '__main__':
    unittest.main()
import bisect

class KDTree:
  def __init__(self, value=None, index=None, left_tree=None, right_tree=None):
    self._value = value
    self._index = index
    self._left_tree = left_tree
    self._right_tree = right_tree


  def get_value(self):
    return self._value


  def get_left_tree(self):
    return self._left_tree


  def get_right_tree(self):
    return self._right_tree


  def get_index(self):
    return self._index


  def is_leaf(self):
    return self._left_tree is None and self._right_tree is None


  @staticmethod
  def build(patients, depth=0):
    if len(patients) <= 0:
      return None

    index_to_split = depth % len(patients[0].get_features())
    patients.sort(key=lambda patient: patient.get_features()[index_to_split])

    median_index = len(patients) // 2
    median_patient = patients[median_index]
    left_tree = KDTree.build(patients[:median_index], depth + 1)
    right_tree = KDTree.build(patients[median_index + 1:], depth + 1)

    return KDTree(median_patient, index_to_split, left_tree, right_tree)


  def predict_outcome(self, patient, max_distance, max_patients_in_grouping, *features):
    nearest_patients = self.create_grouping(patient, max_distance, max_patients_in_grouping, *features)
    outcomes = [patient.get_outcome() for patient in nearest_patients]
    return max(set(outcomes), key=outcomes.count)


  def create_grouping(self, patient, max_distance, max_patients_in_grouping, *features):
    if max_distance <= 0 or max_patients_in_grouping < 1:
      return []

    nearest_patients = self._create_grouping(patient, max_distance, max_patients_in_grouping, features)
    return list(map(lambda nearest_patient: nearest_patient[1], nearest_patients))


  def _create_grouping(self, patient, max_distance, max_patients_in_grouping, features, nearest_patients=[]):
    distance = self._value.compute_distance(patient, *features)
    if distance <= max_distance:
      self._add_nearest_patient(distance, nearest_patients, max_patients_in_grouping)

    chosen_branch, unchosen_branch = self._get_chosen_and_unchosen_branches(patient)

    if chosen_branch is not None:
      nearest_patients = chosen_branch._create_grouping(
        patient,
        max_distance,
        max_patients_in_grouping,
        features,
        nearest_patients
      )

    if self._should_check_unchosen_branch(patient, nearest_patients, features, max_patients_in_grouping):
      if unchosen_branch is not None:
        nearest_patients = unchosen_branch._create_grouping(
          patient,
          max_distance,
          max_patients_in_grouping,
          features,
          nearest_patients
        )

    return nearest_patients


  # Insert the distance and current pivot patient into nearest_patients
  # When the distance is farther than the farthest nearest patient,
  # replace it at the front of the list for future comparisons.
  def _add_nearest_patient(self, distance, nearest_patients, max_patients_in_grouping):
    nearest_patient = (-distance, self._value)
    if len(nearest_patients) < max_patients_in_grouping:
      bisect.insort(nearest_patients, nearest_patient)
    elif nearest_patients[0][0] < -distance:
      nearest_patients[0] = nearest_patient


  # Choose the left branch when the patient has a smaller
  # value than the current pivot patient value and the
  # right branch when the value is greater than or equal.
  def _get_chosen_and_unchosen_branches(self, patient):
    comparision_value = self._value.get_features()[self._index]
    patient_value = patient.get_features()[self._index]

    if patient_value < comparision_value:
      chosen_branch = self._left_tree
      unchosen_branch = self._right_tree
    else:
      chosen_branch = self._right_tree
      unchosen_branch = self._left_tree

    return chosen_branch, unchosen_branch


  # Determine if the unchosen region is intersected by the radius
  # from the farthest nearest patient so far. Distance to the region
  # is simply the absolute value between the pivot axis and the other
  # branch axis value. If there are less than max_patients_in_grouping
  # patients found, check both branches.
  def _should_check_unchosen_branch(self, patient, nearest_patients, features, max_patients_in_grouping):
    if len(nearest_patients) < max_patients_in_grouping:
      return True

    comparision_value = self._value.get_features()[self._index]
    patient_value = patient.get_features()[self._index]

    distance_from_patient_to_farthest_node = patient.compute_distance(nearest_patients[0][1], *features)
    distance_from_patient_to_unchosen_region = abs(patient_value - comparision_value)

    return distance_from_patient_to_unchosen_region <= distance_from_patient_to_farthest_node
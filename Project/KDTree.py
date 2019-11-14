class KDTree:
  def __init__(self, value=None, index=None, left_tree=None, right_tree=None):
    self._value = value
    self._index = index
    self._left_tree = left_tree
    self._right_tree = right_tree


  @staticmethod
  def build(patients, depth=0):
    points = [patient.get_features() for patient in patients]

    if len(points) <= 0:
      return None

    index_to_split = depth % len(points[0])
    points.sort(key=lambda point: point[index_to_split])

    median_index = len(points) // 2
    median_patient = patients[median_index]
    left_tree = KDTree.build(patients[:median_index], depth + 1)
    right_tree = KDTree.build(patients[median_index + 1:], depth + 1)

    return KDTree(median_patient, index_to_split, left_tree, right_tree)


  def is_leaf(self):
    return self._left_tree is None and self._right_tree is None


  def get_value(self):
    return self._value


  def get_left_tree(self):
    return self._left_tree


  def get_right_tree(self):
    return self._right_tree


  def predict_outcome(self, patient, max_distance, max_patients_in_grouping, *features):
    nearest_patients = self.create_grouping(patient, max_distance, max_patients_in_grouping, *features)
    outcomes = [patient.get_outcome() for patient in nearest_patients]
    return max(set(outcomes), key=outcomes.count)


  def create_grouping(self, patient, max_distance, max_patients_in_grouping, *features):
    if max_distance <= 0 or max_patients_in_grouping < 1:
      return []

    nearest_patients = self._create_grouping(patient, max_distance, max_patients_in_grouping, features)
    return sorted(nearest_patients, key=lambda p: p.compute_distance(patient, *features))[:max_patients_in_grouping]


  def _create_grouping(self, patient, max_distance, max_patients_in_grouping, features, farthest_distance=None):
    nearest_patients = []
    distance = self._value.compute_distance(patient, *features)

    if distance <= max_distance:
      nearest_patients.append(self._value)
      if farthest_distance is None or distance > farthest_distance:
        farthest_distance = distance

    comparision_value = self._value.get_features()[self._index]
    patient_value = patient.get_features()[self._index]
    chosen_branch, unchosen_branch = self._get_branches(comparision_value, patient_value)

    if chosen_branch is not None:
      nearest_patients += chosen_branch._create_grouping(
        patient,
        max_distance,
        max_patients_in_grouping,
        features,
        farthest_distance
      )

    patient_distance = patient_value - comparision_value
    if self._should_check_unchosen_branch(farthest_distance, patient_distance, nearest_patients, max_patients_in_grouping):
      if unchosen_branch is not None:
        nearest_patients += unchosen_branch._create_grouping(
          patient,
          max_distance,
          max_patients_in_grouping,
          features,
          farthest_distance
        )

    return nearest_patients


  def _get_branches(self, comparision_value, patient_value):
    if patient_value < comparision_value:
      chosen_branch = self._left_tree
      unchosen_branch = self._right_tree
    else:
      chosen_branch = self._right_tree
      unchosen_branch = self._left_tree

    return chosen_branch, unchosen_branch


  def _should_check_unchosen_branch(self, farthest_distance, patient_distance, nearest_patients, max_patients_in_grouping):
    return (farthest_distance is not None and patient_distance <= farthest_distance) \
      or len(nearest_patients) < max_patients_in_grouping


  def print(self, indentation=0):
    if self.is_leaf():
      print(' ' * indentation, 'value for index', self._index, ':', self._value)
    else:
      print(' ' * indentation, 'median value for index', self._index, ':', self._value)
      print(' ' * indentation, 'left')
      if self._left_tree is None:
        print(' ' * (indentation + 2), None)
      else:
        self._left_tree.print(indentation + 2)

      print(' ' * indentation, 'right')
      if self._right_tree is None:
        print(' ' * (indentation + 2), None)
      else:
        self._right_tree.print(indentation + 2)
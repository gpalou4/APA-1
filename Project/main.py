from Patient import Patient
from KDTree import KDTree

if __name__ == '__main__':
  patient = Patient.parse_patients_from_file('test_patients.csv')[0]

  patients = Patient.parse_patients_from_file('patient_data.csv')
  kd_tree = KDTree.build(patients)

  print(kd_tree.predict_outcome(patient, 3, 7))
  print(kd_tree.create_grouping(patient, 3, 7))
import csv
import math

class Patient:

  def __init__(
    self,
    patient_id,
    outcome,
    icustay_sequence,
    icustay_id,
    age,
    sex,
    length_of_hospital,
    bmi,
    number_of_additives,
    number_of_procedures,
    duration_of_medications,
    percentage_of_abnormal_lab_events,
    comorbidity_score,
    hospital_admission_id,
    medication_count
  ):
    self._patient_id= patient_id
    self._outcome = outcome
    self._icustay_sequence = icustay_sequence
    self._icustay_id = icustay_id
    self._age = age
    self._sex = sex
    self._length_of_hospital = length_of_hospital
    self._bmi = bmi
    self._number_of_additives = number_of_additives
    self._number_of_procedures = number_of_procedures
    self._duration_of_medications = duration_of_medications
    self._percentage_of_abnormal_lab_events = percentage_of_abnormal_lab_events
    self._comorbidity_score = comorbidity_score
    self._hospital_admission_id = hospital_admission_id,
    self._medication_count = medication_count

    self._features = (
      self._age,
      self._sex,
      self._length_of_hospital,
      self._bmi,
      self._number_of_additives,
      self._number_of_procedures,
      self._duration_of_medications,
      self._percentage_of_abnormal_lab_events,
      self._comorbidity_score,
      self._medication_count
    )

  @staticmethod
  def parse_patients_from_file(filename):
    with open(filename,"r") as features:
      features.readline()
      features_csv = csv.reader(features, delimiter=',')
      patients = []
      for parsed_line in features_csv:
        patient_id = parsed_line[0]
        outcome = int(parsed_line[1])
        icustay_sequence = float(parsed_line[2])
        icustay_id = int(parsed_line[3])
        age = float(parsed_line[4])
        sex = int(parsed_line[5])
        length_of_hospital = float(parsed_line[6])
        bmi = float(parsed_line[7])
        number_of_additives = float(parsed_line[8])
        number_of_procedures = float(parsed_line[9])
        duration_of_medications = float(parsed_line[10])
        percentage_of_abnormal_lab_events = float(parsed_line[11])
        comorbidity_score = float(parsed_line[12])
        hospital_admission_id = float(parsed_line[13])
        medication_count = int(parsed_line[14])
        patient = Patient(patient_id, outcome, icustay_sequence, icustay_id, age, sex, length_of_hospital, bmi,
          number_of_additives, number_of_procedures, duration_of_medications, percentage_of_abnormal_lab_events, comorbidity_score, 
          hospital_admission_id, medication_count)
        patients.append(patient)
      return patients

  def get_outcome(self):
    return self._outcome

  def get_features(self):
    return self._features

  def get_feature(self, feature):
    if self.has_feature(feature):
      return getattr(self, '_' + feature)
    return None

  def has_feature(self, feature):
    return hasattr(self, '_' + feature)

  def compute_distance(self, patient, *features):
    features_1 = []
    features_2 = []
    for feature in features:
      if not self.has_feature(feature):
        raise NameError('Feature not found')
      features_1.append(self.get_feature())
      features_2.append(patient.get_feature())
    list_of_features_1 = features_1 or self.get_features()
    list_of_features_2 = features_1 or patient.get_features()
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(list_of_features_1, list_of_features_2)]))


  #### LAST VERSIONS ####
    
  # def compute_distance(self, patient, *features):
  #   features_1 = []
  #   features_2 = []
  #   for feature in features:
  #     if not self.has_feature(feature):
  #       raise NameError('Feature not found')
  #     list_of_features_1 = features_1.append(self.get_feature())
  #     list_of_features_2 = features_2.append(patient.get_feature())
  #   list_of_features_1 = list_of_features_1 or self.get_features()
  #   list_of_features_2 = list_of_features_2 or patient.get_features()
  #   return math.sqrt(sum([(a - b) ** 2 for a, b in zip(list_of_features_1, list_of_features_1)]))

  # def parse_patients_from_file(filename):
  #   with open(filename,"r") as features:
  #     patients = []
  #     for line in features.readlines()[1:]:
  #       parsed_line = line.strip().split(",")
  #       patient_id = parsed_line[0]
  #       outcome = int(parsed_line[1])
  #       icustay_sequence = float(parsed_line[2])
  #       icustay_id = int(parsed_line[3])
  #       age = float(parsed_line[4])
  #       sex = int(parsed_line[5])
  #       length_of_hospital = float(parsed_line[6])
  #       bmi = float(parsed_line[7])
  #       number_of_additives = float(parsed_line[8])
  #       number_of_procedures = float(parsed_line[9])
  #       duration_of_medications = float(parsed_line[10])
  #       percentage_of_abnormal_lab_events = float(parsed_line[11])
  #       comorbidity_score = float(parsed_line[12])
  #       hospital_admission_id = float(parsed_line[13])
  #       medication_count = int(parsed_line[14])
  #       patient = Patient(patient_id, outcome, icustay_sequence, icustay_id, age, sex, length_of_hospital, bmi,
  #         number_of_additives, number_of_procedures, duration_of_medications, percentage_of_abnormal_lab_events, comorbidity_score, 
  #         hospital_admission_id, medication_count)
  #       patients.append(patient)
  #     return patients
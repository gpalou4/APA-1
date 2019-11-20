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
    number_of_medications,
    number_of_additives,
    number_of_procedures,
    duration_of_medications,
    percentage_of_abnormal_lab_events,
    comorbidity_score,
    hospital_admission_id
  ):
    self._patient_id= patient_id
    self._outcome = outcome
    self._icustay_sequence = icustay_sequence
    self._icustay_id = icustay_id
    self._age = age
    self._sex = sex
    self._length_of_hospital = length_of_hospital
    self._bmi = bmi
    self._number_of_medications = number_of_medications
    self._number_of_additives = number_of_additives
    self._number_of_procedures = number_of_procedures
    self._duration_of_medications = duration_of_medications
    self._percentage_of_abnormal_lab_events = percentage_of_abnormal_lab_events
    self._comorbidity_score = comorbidity_score
    self._hospital_admission_id = hospital_admission_id

    self._features = (
      self._age,
      self._sex,
      self._length_of_hospital,
      self._bmi,
      self._number_of_medications,
      self._comorbidity_score,
      self._number_of_additives,
      self._number_of_procedures,
      self._duration_of_medications,
      self._percentage_of_abnormal_lab_events
    )

  @staticmethod
  def parse_patients_from_file():
    with open("features.csv","r") as features:
      patients = []
      for line in features:
        parsed_line = line.strip().split(",")
        patient_id = parsed_line[0]
        outcome = parsed_line[1]
        icustay_sequence = parsed_line[2]
        icustay_id = parsed_line[3]
        age = parsed_line[4]
        sex = parsed_line[5]
        length_of_hospital = parsed_line[6]
        bmi = parsed_line[7]
        number_of_medications = parsed_line[8]
        number_of_additives = parsed_line[9]
        number_of_procedures = parsed_line[10]
        duration_of_medications = parsed_line[11]
        percentage_of_abnormal_lab_events = parsed_line[12]
        comorbidity_score = parsed_line[13]
        hospital_admission_id = parsed_line[14]
        patient = Patient(patient_id, outcome, icustay_sequence, icustay_id, age, sex, length_of_hospital, bmi, number_of_medications,
          number_of_additives, number_of_procedures, duration_of_medications, percentage_of_abnormal_lab_events, comorbidity_score, 
          hospital_admission_id)
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
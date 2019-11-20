class Patient:
  def __init__(
    self,
    outcome,
    age,
    sex,
    days_in_icu,
    bmi,
    number_of_medications,
    comorbidity_score,
    number_of_additives,
    number_of_procedures,
    duration_of_medications,
    percentage_of_abnormal_lab_events
  ):
    self._outcome = outcome
    self._age = age
    self._sex = sex
    self._days_in_icu = days_in_icu
    self._bmi = bmi
    self._number_of_medications = number_of_medications
    self._comorbidity_score = comorbidity_score
    self._number_of_additives = number_of_additives
    self._number_of_procedures = number_of_procedures
    self._duration_of_medications = duration_of_medications
    self._percentage_of_abnormal_lab_events = percentage_of_abnormal_lab_events

    self._features = (
      self._age,
      self._sex,
      self._days_in_icu,
      self._bmi,
      self._number_of_medications,
      self._comorbidity_score,
      self._number_of_additives,
      self._number_of_procedures,
      self._duration_of_medications,
      self._percentage_of_abnormal_lab_events
    )

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
# KDTree with patient data

Using MIMIC-II data, we compiled 2994 patients of the following features:

  Outcome = dying in the hospital during the stay
  Age
  Sex (0 = M, 1 = F)
  Length of the hospital stay
  BMI
  Number of additives in medications
  Number of procedures during the stay
  Amount of time taking the medications
  % of lab events marked as abnormal
  Sum of comorbidities
  Number of medications

Some of these features have been scaled to more accurately calculate Euclidean distance.

---

Using these patients, we construct a [KD Tree](https://en.wikipedia.org/wiki/K-d_tree) that we can then use to create groups / k nearest neighbors (compute_grouping). And further, we can predict a patient's outcome by majority vote from the nearest neighbors (predict_outcome).

However, the prediction is very poor (likely due to the data being a small subset of the entire MIMIC-II database). Using all ten features, we only see an accuracy of 45% using the 5 nearest neighbors.

---

To run an example of parsing the patients, building the KD Tree, and creating a grouping as well as predicting:

```{python}
python main.py
```

---

To run tests:

```{python}
python test_KDTree.py; python test_Patient.py
```
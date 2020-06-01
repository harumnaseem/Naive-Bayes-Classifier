# Naive-Bayes-Classifier

This repository contains the implementation of  Naïve Bayes Classifier. 
I used the Bernoulli naïve Bayes model for the classification task. Bernoulli model requires that all attributes value is binary as a result the dataset of SPECT contains only binary values.

Explanation of dataset:
Each patient is classified into two categories: Normal and Abnormal, depending on the number of medical tests he/she passes. The database contains 267 patients’ data, every person underwent 22 medical tests and each test was either pass or fail. As a result, for each patient 22 binary values were extracted.
1
There are two files, Spect_train and Spect_test. Spect_train has a total 80 data points and Spect_test has 187 data points.
Spect_train patient data will be used to train the naïve Bayes classifier and Spect_test to test it.
A single patient in the dataset is described as a single line of the file. So, each line has 23 values, the first value of each line describes whether the person was described as normal (value of 1) or abnormal (value of 0). All other 22 values define which test number the patient failed and which he/she passed.

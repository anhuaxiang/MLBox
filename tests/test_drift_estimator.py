#!/usr/bin/env python
# coding: utf-8
# Author: Axel ARONIO DE ROMBLAY <axelderomblay@gmail.com>
# License: BSD 3 clause
import pytest
import pandas as pd
import numpy as np

from mlbox.preprocessing.drift.drift_estimator import DriftEstimator
from mlbox.preprocessing.reader import Reader


def test_init_drift_estimator():
    drift_estimator = DriftEstimator()
    assert drift_estimator.n_folds == 2
    assert drift_estimator.stratify
    assert drift_estimator.random_state == 1
    assert not drift_estimator._DriftEstimator__cv
    assert not drift_estimator._DriftEstimator__pred
    assert not drift_estimator._DriftEstimator__target
    assert not drift_estimator._DriftEstimator__fitOK


def test_get_params_drift_estimator():
    drift_estimator = DriftEstimator()
    dict = {'estimator': drift_estimator.estimator,
            'n_folds': 2,
            'stratify': True,
            'random_state': 1}
    assert drift_estimator.get_params() == dict


def test_set_params_drift_estimator():
    drift_estimator = DriftEstimator()
    dict = {'estimator': drift_estimator.estimator,
            'n_folds': 3,
            'stratify': False,
            'random_state': 2}
    drift_estimator.set_params(**dict)
    assert drift_estimator.get_params() == dict


def test_fit_drift_estimator():
    df_train = pd.read_csv("data_for_tests/clean_train.csv")
    df_test = pd.read_csv("data_for_tests/clean_test.csv")
    drift_estimator = DriftEstimator()
    drift_estimator.fit(df_train, df_test)
    assert drift_estimator._DriftEstimator__fitOK


def test_score_drift_estimator():
    df_train = pd.read_csv("data_for_tests/clean_train.csv")
    df_test = pd.read_csv("data_for_tests/clean_test.csv")
    drift_estimator = DriftEstimator()
    with pytest.raises(ValueError):
        drift_estimator.score()
    drift_estimator.fit(df_train, df_test)
    assert drift_estimator.score() > 0


def test_predict_drift_estimator():
    df_train = pd.read_csv("data_for_tests/clean_train.csv")
    df_test = pd.read_csv("data_for_tests/clean_test.csv")
    drift_estimator = DriftEstimator()
    with pytest.raises(ValueError):
        drift_estimator.predict()
    drift_estimator.fit(df_train, df_test)
    results = drift_estimator.predict()
    assert len(results) == 1309

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

from nose.tools import eq_

import mapnik

from .utilities import execution_path, run_all


def setup():
    # All of the paths used are relative, if we run the tests
    # from another directory we need to chdir()
    os.chdir(execution_path('.'))


def test_color_pickle():
    c = mapnik.Color('blue')

    eq_(pickle.loads(pickle.dumps(c)), c)

    c = mapnik.Color(0, 64, 128)

    eq_(pickle.loads(pickle.dumps(c)), c)

    c = mapnik.Color(0, 64, 128, 192)

    eq_(pickle.loads(pickle.dumps(c)), c)


def test_envelope_pickle():
    e = mapnik.Box2d(100, 100, 200, 200)

    eq_(pickle.loads(pickle.dumps(e)), e)


def test_parameters_pickle():
    params = mapnik.Parameters()
    params.append(mapnik.Parameter('oh', str('yeah')))

    params2 = pickle.loads(pickle.dumps(params, pickle.HIGHEST_PROTOCOL))

    eq_(params[0][0], params2[0][0])
    eq_(params[0][1], params2[0][1])

if __name__ == "__main__":
    setup()
    exit(run_all(eval(x) for x in dir() if x.startswith("test_")))

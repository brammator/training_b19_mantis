# -*- coding: utf-8 -*-
import getopt
import os.path
import sys

import jsonpickle

from fixture.common import random_string
from model.project import Project

try:
    opts, args = getopt.getopt(sys.argv[1:], "f:n:")
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

filename = "data/projects.json"
n = 5

for o, a in opts:
    if o == "-f":
        filename = a
    elif o == "-n":
        n = int(a)

testdata = [Project()] + [Project.random(i+1) for i in range(n)]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", filename)
with open(data_file, "w", encoding="utf-8") as fp:
    jsonpickle.set_encoder_options("json", indent=2)
    fp.write(jsonpickle.encode(testdata))

pass

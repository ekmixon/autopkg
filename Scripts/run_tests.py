#!/usr/local/autopkg/python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import unittest
from unittest import TestSuite, TextTestRunner

AUTOPKG_TOP: str = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Code")
)
sys.path.insert(0, AUTOPKG_TOP)

TESTS_DIR: str = os.path.join(AUTOPKG_TOP, "tests")
TEST_SUITE: TestSuite = unittest.defaultTestLoader.discover(TESTS_DIR)
RUNNER: TextTestRunner = TextTestRunner()

if RUNNER.run(TEST_SUITE).wasSuccessful():
    sys.exit(0)
sys.exit(1)

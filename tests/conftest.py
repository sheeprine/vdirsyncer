# -*- coding: utf-8 -*-
'''
General-purpose fixtures for vdirsyncer's testsuite.
'''
import pytest

import vdirsyncer.log


@pytest.fixture(autouse=True)
def setup_logging():
    vdirsyncer.log.set_level(vdirsyncer.log.logging.DEBUG)
    vdirsyncer.log.add_handler(vdirsyncer.log.stdout_handler)

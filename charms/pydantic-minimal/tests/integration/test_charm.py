# Copyright 2026 Charmer
# See LICENSE file for licensing details.
#
# The integration tests use the Jubilant library and the pytest-jubilant plugin.
# See https://documentation.ubuntu.com/ops/latest/howto/write-integration-tests-for-a-charm/
#
# pytest-jubilant provides a module-scoped `juju` fixture that creates a temporary Juju model.
# The `charm` fixture is defined in conftest.py.

import logging
import pathlib

import jubilant
import pytest

logger = logging.getLogger(__name__)


@pytest.mark.juju_setup
def test_deploy(charm: pathlib.Path, juju: jubilant.Juju):
    """Deploy the charm under test."""
    juju.deploy(charm, app="pydantic-minimal")
    juju.wait(jubilant.all_active)


def test_workload_version_is_set(charm: pathlib.Path, juju: jubilant.Juju):
    """Check that the pydantic-backed workload version is set at runtime."""
    version = juju.status().apps["pydantic-minimal"].version
    assert version == "2.3.4"

# Copyright 2026 Charmer
# See LICENSE file for licensing details.
#
# To learn more about testing, see https://documentation.ubuntu.com/ops/latest/explanation/testing/

from ops import testing

from charm import PydanticMinimalCharm


def test_start():
    """Test that the charm has the correct state after handling the start event."""
    # Arrange:
    ctx = testing.Context(PydanticMinimalCharm)
    # Act:
    state_out = ctx.run(ctx.on.start(), testing.State())
    # Assert:
    assert state_out.workload_version == "2.3.4"
    assert state_out.unit_status == testing.ActiveStatus()

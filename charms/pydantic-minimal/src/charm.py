#!/usr/bin/env python3
# Copyright 2026 Charmer
# See LICENSE file for licensing details.

"""Charm the application."""

import ops
from pydantic import BaseModel


class WorkloadMetadata(BaseModel):
    """Metadata validated during start handling."""

    version: str


class PydanticMinimalCharm(ops.CharmBase):
    """Charm the application."""

    def __init__(self, framework: ops.Framework):
        super().__init__(framework)
        framework.observe(self.on.start, self._on_start)

    def _on_start(self, event: ops.StartEvent):
        """Handle start event."""
        self.unit.status = ops.MaintenanceStatus("starting workload")
        metadata = WorkloadMetadata(version="2.3.4")
        self.unit.set_workload_version(metadata.version)
        self.unit.status = ops.ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    ops.main(PydanticMinimalCharm)

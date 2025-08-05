
import sys
import subprocess
import pytest

class TestCli:
    def test_gh_cli1(self):
        # Test running the entrypoint
        ret = subprocess.call(["/work/bin/entrypoint", "--help"])

        assert ret == 0

    def test_gh_cli2(self):
        # Test running the entrypoint
        ret = subprocess.call(["/usr/bin/gh", "--help"])

        assert ret == 0

    def test_gh_cli3(self):
        # Test running the entrypoint
        ret = subprocess.call(["/usr/bin/gh", "--version"])

        assert ret == 0


import pytest
from approvaltests.reporters import GenericDiffReporter, GenericDiffReporterConfig


class IntelliJDiffReporter(GenericDiffReporter):
    def __init__(self):
        config = GenericDiffReporterConfig(
            name="IntelliJ IDEA",
            path="/Applications/IntelliJ IDEA.app/Contents/MacOS/idea",
            extra_args=["diff"]
        )
        super().__init__(config)


@pytest.fixture(scope="session", autouse=True)
def intellij_diff_reporter():
    return IntelliJDiffReporter()

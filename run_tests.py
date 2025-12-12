import pytest


pytest.main("tests/", "--html=reports/report.html", "--self-contained-html", "-v")



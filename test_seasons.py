from datetime import date
from seasons import age_in_words


def test_age_in_words():
    # Test for zero minutes
    assert age_in_words(0) == "0 minutes"

    # Test for one minute
    assert age_in_words(1) == "1 minute"

    # Test for multiple minutes
    assert age_in_words(62) == "1 minute and 2 seconds"
    assert age_in_words(3661) == "1 hour, 1 minute and 1 second"
    assert age_in_words(525600) == "1 year"

    # Test for all units
    assert age_in_words(18934560) == "36 years, 6 months, 12 days, 2 hours and 40 minutes"

from seasons import main
def test_main(monkeypatch):
    # Test for valid date
    monkeypatch.setattr("builtins.input", lambda _: "1990-01-01")
    assert main() is None

    # Test for invalid date format
    monkeypatch.setattr("builtins.input", lambda _: "1990/01/01")
    assert main() == 1

    # Test for future date
    monkeypatch.setattr("builtins.input", lambda _: str(date.today()))
    assert main() == 1

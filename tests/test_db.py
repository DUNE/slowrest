import oracledb

import pytest

from slowrest.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(oracledb.InterfaceError) as e:
        db.execute("SELECT 1")

    assert "DPY-1006: cursor is not open" in str(e.value)


def test_test_print_command(runner, monkeypatch):
    class Recorder:
        called = False

    def fake_test_print():
        Recorder.called = True

    monkeypatch.setattr("slowrest.db.test_print", fake_test_print)
    result = runner.invoke(args=["test-command"])
    assert "Conducted test command" in result.output
    assert Recorder.called

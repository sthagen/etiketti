import pytest

import etiketti.cli as cli


def test_app_basic_pos(caplog):
    assert cli.app(['test/fixtures/basic/this.pdf']) == 0
    for record in caplog.records:
        assert record.levelname not in ('WARNING', 'ERROR', 'CRITICAL')
    assert 'enforce' not in caplog.text


def test_app_basic_arg(caplog):
    assert cli.app(['-i', 'test/fixtures/basic/this.pdf']) == 0
    for record in caplog.records:
        assert record.levelname not in ('WARNING', 'ERROR', 'CRITICAL')
    assert 'enforce' not in caplog.text


def test_app_help(caplog, capsys):
    assert cli.app([]) == 0
    for record in caplog.records:
        assert record.levelname not in ('WARNING', 'ERROR', 'CRITICAL')
    assert 'usage' in capsys.readouterr()[0]


def test_app_non_existing_folder(caplog, capsys):
    with pytest.raises(SystemExit):
        cli.app(['does-not-exist/this.pdf'])
    for record in caplog.records:
        assert record.levelname not in ('WARNING', 'ERROR', 'CRITICAL')
    out, err = capsys.readouterr()
    assert not out
    assert 'usage' in err
    assert 'etiketti: error: requested pdf at (does-not-exist/this.pdf) does not exist' in err


def test_app_in_pdf_as_folder(caplog, capsys):
    with pytest.raises(SystemExit):
        cli.app(['test/fixtures/basic'])
    for record in caplog.records:
        assert record.levelname not in ('WARNING', 'ERROR', 'CRITICAL')
    out, err = capsys.readouterr()
    assert not out
    assert 'usage' in err
    assert 'etiketti: error: requested pdf at (test/fixtures/basic) is not a file' in err


def test_app_non_existing_cfg_path(caplog, capsys):
    with pytest.raises(SystemExit):
        cli.app(['test/fixtures/basic/this.pdf', '-c', 'does-not-exist'])
    for record in caplog.records:
        assert record.levelname not in ('WARNING', 'ERROR', 'CRITICAL')
    out, err = capsys.readouterr()
    assert not out
    assert 'usage' in err
    assert 'etiketti: error: configuration path (does-not-exist) does not exist' in err


def test_app_cfg_as_folder(caplog, capsys):
    with pytest.raises(SystemExit):
        cli.app(['test/fixtures/basic/this.pdf', '-c', 'test/fixtures/basic'])
    for record in caplog.records:
        assert record.levelname not in ('WARNING', 'ERROR', 'CRITICAL')
    out, err = capsys.readouterr()
    assert not out
    assert 'usage' in err
    assert 'etiketti: error: configuration path (test/fixtures/basic) is not a file' in err

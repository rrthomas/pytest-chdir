from pathlib import Path
from pytest_chdir import define_chdir_fixture

define_chdir_fixture("chroot", Path("/"), __name__)


def test_chtmpdir(chtmpdir):
    assert Path.cwd() == chtmpdir


def test_chdatadir(chdatadir):
    assert Path.cwd() == chdatadir
    assert Path.cwd().stem == Path(__file__).stem


def test_chshared_datadir(chshared_datadir):
    assert Path.cwd() == chshared_datadir
    assert str(Path.cwd().stem) == "data"


def test_chroot(chroot):
    assert Path.cwd() == Path("/")
    assert Path.cwd() == chroot

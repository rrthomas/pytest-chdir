# pytest-chdir
A pytest fixture for changing current working directory.

[![Actions Status](https://github.com/rrthomas/pytest-chdir/workflows/Python%20package/badge.svg)](https://github.com/rrthomas/pytest-chdir/actions)
[![PyPI](https://img.shields.io/pypi/v/pytest-chdir.svg)](https://pypi.python.org/pypi/pytest-chdir)
[![PythonVersions](https://img.shields.io/pypi/pyversions/pytest-chdir.svg)](https://pypi.python.org/pypi/pytest-chdir)

# Usage

## Change directory to tmpdir
Using `chtmpdir` provides not only creating temporary directory but also  moving there automatically.

``` python
def test_move_to_tmpdir(chtmpdir):
    assert Path.cwd() == chtmpdir
    assert str(chtmpdir).startswith("/tmp")
```

## Define new fixtures to change current working directory
By using `define_chdir_fixture`, you can create a fixture to move to specified directory.

``` python
define_chdir_fixture("chetc", Path("/etc"), __name__)

def test_chetc(chetc):
    assert Path.cwd() == Path("/etc")
```

## Integrate with pytest-datadir
If you have installed [pytest-datadir](https://github.com/gabrielcnr/pytest-datadir), you can use `chdatadir` and `chshared_datadir`.

``` python
def test_chdatadir(chdatadir):
    assert str(Path.cwd().stem) == "test_dir"

def test_chshared_datadir(chshared_datadir):
    assert str(Path.cwd().stem) == "data"
```

# See also
* [pytest-datadir](https://github.com/gabrielcnr/pytest-datadir)

# License
This software is released under the MIT License, see [LICENSE](LICENSE).

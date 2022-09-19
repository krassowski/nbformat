# Use "hatchling version xx.yy.zz" to handle version changes
import re

try:
    from importlib.metadata import version
except ImportError:
    # Not available until Python 3.8
    version = lambda _: "0.0.0"  # noqa

__version__ = version("nbformat")

# matches tbump regex in pyproject.toml
_version_regex = re.compile(
    r"""
  (?P<major>\d+)
  \.
  (?P<minor>\d+)
  \.
  (?P<patch>\d+)
  (?P<pre>((a|b|rc)\d+))?
  (\.
    (?P<dev>dev\d*)
  )?
  """,
    re.VERBOSE,
)

_version_fields = _version_regex.match(__version__).groupdict()
version_info = tuple(
    field
    for field in (
        int(_version_fields["major"]),
        int(_version_fields["minor"]),
        int(_version_fields["patch"]),
        _version_fields["pre"],
        _version_fields["dev"],
    )
    if field is not None
)

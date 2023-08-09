# python-pydantic-argparse

## Usage

```bash
poetry install
poetry run pydantic-argparse
```

## Example

```bash
$ poetry run pydantic-argparse
foo=42 bar=None

$ poetry run pydantic-argparse --foo 29
foo=29 bar=None

$ poetry run pydantic-argparse --foo 29 --bar asdf
foo=29 bar='asdf'
```

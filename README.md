# Hotels Service

This is the repository for the hotels service.

# Development

## Python version management

Install pyenv with Homebrew [pyenv](https://github.com/pyenv/pyenv#homebrew-in-macos):

```bash
### installing
brew update
brew install pyenv

### setup path https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv
```

## Python

Install Python 3.11.5 using [pyenv](https://github.com/pyenv/pyenv):

```bash
pyenv install 3.11.5
```

## Poetry

We are using [Poetry](https://python-poetry.org/) as a tool for Python packaging and dependency management. <br/><br/>
Windows installation:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

macOS installation:

```bash
brew install poetry
```

## Django

We use [Django](https://docs.djangoproject.com/en/5.0/) as a web framework.

Activate the Poetry virtual environment:

```bash
$ poetry shell
```

Download necessary packages:

```bash
$ poetry install
```

You can check that Django is working correctly by running the server:

```bash
$ python manage.py runserver
```

The server is running at [localhost](http://127.0.0.1:8000/).
The endpoint to get hotels is http://127.0.0.1:8000/api/hotels

## Code Style

We use several code formatters to follow the PEP-8 guidelines. See dedicated docs for [code style](./docs/code-style.md) and for instructions on setting up autocorrection and project formatting.

### Setup pre-commit

The formatters and linters are run using the [pre-commit](https://pre-commit.com/) framework. `pre-commit` is automatically installed as a development dependency with Poetry.
Each `git commit` will then automatically run code formatting before you
even commit the code.

Try to run pre-commit hook:

```bash
pre-commit run --all-files
```

## Tests

We use [pytest](https://docs.pytest.org/en/7.1.x/) framework for unit testing.

To run all tests:

```bash
$ poetry run pytest
```

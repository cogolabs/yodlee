# yodlee [![Build Status](https://travis-ci.org/cogolabs/yodlee.svg?branch=master)](https://travis-ci.org/cogolabs/yodlee) [![Coverage Status](https://coveralls.io/repos/github/cogolabs/yodlee/badge.svg?branch=master)](https://coveralls.io/github/cogolabs/yodlee?branch=master) [![PyPI version](https://img.shields.io/pypi/v/yodlee.svg)](https://pypi.python.org/pypi/yodlee) [![License](https://img.shields.io/pypi/l/yodlee.svg)](https://pypi.python.org/pypi/yodlee) [![Wheel](https://img.shields.io/pypi/wheel/yodlee.svg)](https://pypi.python.org/pypi/yodlee) [![Python Versions](https://img.shields.io/pypi/pyversions/yodlee.svg)](https://pypi.python.org/pypi/yodlee)

[Envestnet Yodlee API Client](https://developer.yodlee.com/apidocs/index.php)

## Installation

```bash
pip install yodlee
```

## Development

```bash
brew install pyenv
brew install pyenv-virtualenv
pip install tox

# add lines below to .bashrc
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PYTHONPATH=".:$PYTHONPATH"
export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/bin:${PATH}

# setup pyenv
pyenv install 2.7.13
pyenv install 3.3.6
pyenv install 3.4.6
pyenv install 3.5.3
pyenv install 3.6.1
pyenv global 2.7.13 3.6.1 3.5.3 3.4.6 3.3.6

# run tests
tox

# develop
pyenv virtualenv yodlee
pip install -r requirements.txt

# test after developing
pyenv deactivate
tox

# develop again
pyenv activate yodlee
```

## Contributing

We are happy to receive your contribution if you first please complete our [Contributor License Agreement](https://github.com/cogolabs/about/blob/master/CLA.pdf).

## License

This package is available as open source under the terms of the [Apache 2.0 License](LICENSE.txt).

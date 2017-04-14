# yodlee ![Build Status](https://travis.cogolo.net/opensource/yodlee.svg?token=t2d4sthPxRMfxMqxUJAy) [![PyPI version](https://badge.fury.io/py/yodlee.svg)](https://badge.fury.io/py/yodlee)
[Evestnet Yodlee API Client](https://developer.yodlee.com/apidocs/index.php)

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
pyenv virutalenv yodlee
pip install -r requirements.txt

# test after developing
pyenv deactivate
tox

# develop again
pyenv activate yodlee
```

## Contributing

We are happy to receive your contribution if you will first please complete our [Contributor License Agreement](https://github.com/cogolabs/about/CLA.pdf).

## License

The package is available as open source under the terms of the [Apache 2 License](LICENSE.txt).

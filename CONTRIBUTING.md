# Contributing to Raspberry Pi Playbook

👏🎉 First off all, Thanks for your interest in contributing to our project! 🎉👏

The following is a set of guidelines for contributing to Raspberry Pi Playbook. These are
mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct

We take our open source community seriously and hold ourselves and other contributors to high standards of communication. By participating and contributing to this project, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

### Requirements

We use `pipenv` to manage and install dependencies. [pipenv](https://pipenv.pypa.io/en/latest/) provides a custom installer that will install `pipenv` isolated from the rest of your system.

```
curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python
```

To install the local development requirements inside a virtual environment run:

```
$ pipenv sync --dev
$ pipenv run inv install-hooks
```

> For more information about `pipenv` check the [docs](https://pipenv.pypa.io/en/latest/basics/).

We use [invoke](http://www.pyinvoke.org/) to wrap up some useful tasks like formatting, linting, testing and more.

Execute `inv[oke] --list` to see the list of available commands.

## Contributing

### Issues

We use GitHub issues to track public bugs/enhancements. Report a new one by [opening a new issue](https://github.com/fedejaure/cookiecutter-modern-pypackage/issues).

In this repository, we provide a couple of templates for you to fill in for:

* Bugs
* Feature Requests/Enhancements

Please read each section in the templates and provide as much information as you can. Please do not put any sensitive information,
such as personally identifiable information, connection strings or cloud credentials. The more information you can provide, the better we can help you.

### Pull Requests

Please follow these steps to have your contribution considered by the maintainers:

1. Fork the repo and create your branch from `develop` locally with a succinct but descriptive name.
2. Add tests for the new changes
3. Edit documentation if you have changed something significant
4. Make sure to follow the [styleguides](#styleguides)
5. Open a PR in our repository and follow the PR template so that we can efficiently review the changes
6. After you submit your pull request, verify that all status checks are passing

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design
work, tests, or other changes before your pull request can be ultimately accepted.

## Styleguides

### Ansible Code Style

All Ansible code is linted with [ansible-lint](https://github.com/ansible-community/ansible-lint) and [yamllint](https://github.com/adrienverge/yamllint). You can
execute `inv[oke] lint`.

## Additional Notes

If you have any question feel free to contact us at fedejaure@gmail.com.

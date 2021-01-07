# cookiecutter-svdvoort

Bleeding edge [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template to create new python packages.

---

## Purpose

This project is used to scaffold a `python` project structure.


## Features

- Always [`up-to-date`](https://github.com/wemake-services/wemake-python-package/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot) dependencies with the help of [`@dependabot`](https://dependabot.com/)
- Supports latest `python3.7+`
- [`poetry`](https://github.com/python-poetry/poetry) for managing dependencies
- [`mypy`](https://mypy.readthedocs.io) for optional static typing
- [`pytest`](https://github.com/pytest-dev/pytest) for testing
- `flake8` and numerous flake8 extensions for linting
- `Github Actions` as the default CI
- [`sphinx`](http://www.sphinx-doc.org/en/master/) and [`readthedocs.org`](https://readthedocs.org/) for documentation
- [`black`](https://black.readthedocs.io/en/stable/) for automatic code formatting
- [`pre-commit`](https://pre-commit.com/) to check for automatic formatting of your code and checking for errors before committing your changes
- Automatic integration with Visual Studio Code to start working on your project 


## Installation

Firstly, you will need to install dependencies:

```bash
pip install cookiecutter jinja2-git lice
```

Make sure Python Poetry is installed, [check the installation instructions here](https://python-poetry.org/docs/#installation).

For integration with Visual Studio Code [install Visual Studio Code](https://code.visualstudio.com/download) and add the following extension packs:

- [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

You can set up an (empty) git repository to automatically get started. 
Create new repository and copy the git link when asked during the set-up.

Then, create a project itself:

```bash
cookiecutter gh:Svdvoort/cookiecutter-svdvoort
```

Now you can open the the project folder in Visual Studio Code and you are good to go! 


## License

MIT. See [LICENSE](https://github.com/wemake-services/wemake-python-package/blob/master/LICENSE) for more details.

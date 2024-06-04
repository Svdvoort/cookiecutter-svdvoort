# cookiecutter-svdvoort

[Copier](https://copier.readthedocs.io) template for Python

---

## Installation

Install [pyenv](https://github.com/pyenv/pyenv), and use it to install an appropiate python version.

Install [python poetry](https://python-poetry.org/docs/#installation).
To support the virtual environments within vscode easily, we need to make poetry create virtualenvs within the project:

```bash
poetry config virtualenvs.in-project true
poetry config virtualenvs.path "{project-dir}/.venv"
```

Within your global python installation install the following packages:

```bash
pip install copier jinja2 jinja2-time
```

For integration with Visual Studio Code [install Visual Studio Code](https://code.visualstudio.com/download) and add the following extension packs:

- [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)

You can set up an (empty) git repository to automatically get started.
Create new repository and copy the git link when asked during the set-up.

Then, create a project itself:

```bash
copier copy https://github.com/Svdvoort/cookiecutter-svdvoort.git /path/to/repo
```

Note: here we use the http-link instead of the git-link to create the project.
This makes it easier for the github actions pipeline to find the project, no need to verify through SSH.
However, you can use the git-link if you do not want to use the automatic update github action.

Now you can open the the project folder in Visual Studio Code and you are good to go!

## Purpose

This project is used to scaffold a `python` project structure.

## License

MIT. See [LICENSE](https://github.com/wemake-services/wemake-python-package/blob/master/LICENSE) for more details.

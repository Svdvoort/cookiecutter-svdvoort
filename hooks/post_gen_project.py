# -*- coding: utf-8 -*-

"""
This module is called after project is created.

From pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import os
import sys
import textwrap

from git import Repo
import git.exc

# Get the root project directory:
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = "{{ project_name }}"

# We need these values to generate correct license:
LICENSE = "{{ license }}"
ORGANIZATION = "{{ organization }}"
GIT_URL = "{{ git_url }}"


def generate_license():
    """Generates license file for the project."""
    license_result = os.system(  # noqa: S605
        "lice {0} -o {1} -p {2} > {3}/LICENSE".format(
            LICENSE.lower(),
            ORGANIZATION,
            PROJECT_NAME,
            PROJECT_DIRECTORY,
        ),
    )
    if license_result:  # it means that return code is not 0, print exception
        print(license_result)  # noqa: WPS421
        sys.exit(1)


def print_futher_instuctions():
    """Shows user what to do next after project creation."""
    message = """
    Your project {0} is created.
    Now you can start working on it:

        cd {0}
    """
    print(textwrap.dedent(message.format(PROJECT_NAME)))  # noqa: WPS421


def setup_environment():
    print("Installing packages")
    os.system("poetry install --with dev,docs")

    print("Setting up git environment")

    repo = Repo.init()
    repo.git.add(all=True)
    repo.git.checkout("-b", "main")
    repo.index.commit("Initial commit")
    repo.create_remote("origin", GIT_URL)

    print("Setting up pre-commit")
    os.system("poetry run pre-commit install")

    repo.index.commit("Installed pre-commit")

    try:
        repo.git.push("origin", "-u", "main")
    except git.exc.GitCommandError:
        # If we are using cruft, we don't need to push.
        # Ugly solution, perhaps we need to think about this?
        # TODO
        pass


generate_license()
setup_environment()
print_futher_instuctions()

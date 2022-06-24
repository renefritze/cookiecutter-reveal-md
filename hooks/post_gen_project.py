#!/usr/bin/env python

import os
import sys
import subprocess


def _precommit():
    from pre_commit import main

    main.main(["install"])
    main.main(["run", "-a"])

def _git_init():
    try:
        subprocess.check_output(["git", "--version"])
    except (PermissionError, FileNotFoundError, subprocess.CalledProcessError) as e:
        return False
    subprocess.check_output(["git", "init"])
    subprocess.check_output(["git", "add", "."])
    subprocess.check_output(["git", "commit", "-m", "initial commit"])


def _install():
    subprocess.check_output(["make", "install"])
    subprocess.check_output(["make",]) 


if __name__ == "__main__":
    if "{{ cookiecutter.create_git_repository|lower }}" != "yes":
        sys.exit(0)

    _git_init()
    _precommit()
    _install()

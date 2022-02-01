"""
Tasks for maintaining the project.

Execute 'invoke --list' for guidance on using Invoke
"""
import platform
from pathlib import Path
from typing import Optional, Dict

from invoke import task
from invoke.context import Context
from invoke.runners import Result

ROOT_DIR = Path(__file__).parent
TASKS_DIR = ROOT_DIR / 'tasks'
HANDLERS_DIR = ROOT_DIR / 'handlers'
MOLECULE_DIR = ROOT_DIR / 'molecule'
ANSIBLE_TARGETS = [
    ROOT_DIR,
    TASKS_DIR,
    HANDLERS_DIR,
    MOLECULE_DIR
]
ANSIBLE_TARGETS_STR = " ".join([str(t) for t in ANSIBLE_TARGETS])
ANSIBLE_ROLES_PATH = f"{ROOT_DIR / '.roles'}:{ROOT_DIR / 'roles'}"


def _run(c, command, env=None):
    # type: (Context, str, Optional[Dict]) -> Result
    return c.run(command, pty=platform.system() != "Windows", env=env)


@task()
def install_hooks(c):
    # type: (Context) -> None
    """Install pre-commit hooks."""
    _run(c, "pipenv run pre-commit install")


@task()
def hooks(c):
    # type: (Context) -> None
    """Run pre-commit hooks."""
    _run(c, "pipenv run pre-commit run --all-files")


@task(
    help={
        "force": "Force overwriting an existing role or collection. (default: False)",
    }
)
def galaxy_install(c, force=False):
    # type: (Context, bool) -> None
    """Install ansible-galaxy requirements."""
    install_options = ['--force'] if force else []
    _run(c, f"pipenv run ansible-galaxy install -r requirements.yml {' '.join(install_options)}")


@task()
def yamllint(c):
    # type: (Context) -> None
    """Run yamllint, a linter for YAML files."""
    _run(c, f"pipenv run yamllint -c {ROOT_DIR / '.yamllint'} {ROOT_DIR}")


@task()
def ansible_lint(c):
    # type: (Context) -> None
    """Run ansible linter."""
    lint_options = [
        '--force-color',
        '-p',
        '-v',
        '--project-dir',
        str(ROOT_DIR)
    ]
    _run(c, f"pipenv run ansible-lint {' '.join(lint_options)} {ANSIBLE_TARGETS_STR}")


@task(pre=[yamllint, ansible_lint])
def lint(c):
    # type: (Context) -> None
    """Run all linting."""


@task()
def tests(c):
    # type: (Context) -> None
    """Run ansible molecule test."""
    _run(c, f"pipenv run molecule test", env={"ANSIBLE_ROLES_PATH": ANSIBLE_ROLES_PATH})


@task(
    help={
        "target": "Ansible playbook to run. (default: main)",
        "tag": "Only run plays and tasks tagged with these values",
        "skip_tag": "Only run plays and tasks whose tags do not match these values",
        "list_tags": "List all available tags",
    },
    iterable=['tag', 'skip_tag']
)
def playbook(c, tag, skip_tag, list_tags=False, target='main'):
    # type: (Context, List[str], List[str], bool, str) -> None
    """Runs Ansible playbooks, executing the defined tasks on the targeted hosts."""
    playbook_options = ['-i', 'inventory']
    if tag:
        playbook_options += ["--tags", f'"{ ",".join(tag) }"']
    if skip_tag:
        playbook_options += ["--skip-tags", f'"{ ",".join(skip_tag) }"']
    if list_tags:
        playbook_options.append("--list-tags")
    _run(c, f"pipenv run ansible-playbook {target}.yml {' '.join(playbook_options)}")


@task(
    help={
        "part": "Part of the version to be bumped.",
        "dry_run": "Don't write any files, just pretend. (default: False)",
    }
)
def version(c, part, dry_run=False):
    # type: (Context, str, bool) -> None
    """Bump version."""
    bump_options = ["--dry-run"] if dry_run else []
    _run(c, f"pipenv run bump2version {' '.join(bump_options)} {part}")

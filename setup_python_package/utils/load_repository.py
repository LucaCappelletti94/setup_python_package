import os
from git import Repo

repository = None


def load_repository():
    """Return current repository object."""
    global repository
    if repository is None:
        repository = Repo(os.getcwd())
    return repository


def load_repository_url() -> str:
    """Return repository URL."""
    return load_repository().remote().url.split(".git")[0]


def load_repository_name() -> str:
    """Return repository name."""
    return os.path.basename(load_repository().working_dir)


def load_repository_author_name() -> str:
    """Return repository author name."""
    return load_repository().head.reference.commit.author.name


def load_repository_author_email() -> str:
    """Return repository author email."""
    return load_repository().head.reference.commit.author.email
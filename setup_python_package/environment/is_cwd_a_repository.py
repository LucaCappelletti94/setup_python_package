from git import InvalidGitRepositoryError
from ..utils.load_repository import load_repository

def is_cwd_a_repository() -> bool:
    try:
        load_repository()
        return True
    except InvalidGitRepositoryError:
        return False
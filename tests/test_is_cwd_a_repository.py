from setup_python_package.environment import is_cwd_a_repository

def test_is_cwd_a_repository():
    assert is_cwd_a_repository()
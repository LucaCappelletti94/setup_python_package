from .load_repository import load_repository_name, load_repository_organization


def get_default_sonar_project_key()->str:
    """Return default package name based on repo name."""
    return "{organization}_{repository}".format(
        organization=load_repository_organization(),
        repository=load_repository_name()
    )
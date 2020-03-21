from .load_repository import load_repository_organization


def get_default_sonar_organization_key()->str:
    """Return default package name based on repo name."""
    return "{organization}-github".format(
        organization=load_repository_organization()
    ).lower()
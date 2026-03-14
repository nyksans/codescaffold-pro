import os
import hashlib
from git import Repo


CACHE_DIR = "cache"


def clone_repository(repo_url: str) -> str:
    """
    Clone a GitHub repository into the cache directory.

    If the repository was previously cloned,
    the cached version will be reused.

    Returns:
        str: Local path of the cloned repository
    """

    if not repo_url:
        raise ValueError("Repository URL cannot be empty")

    # ensure cache directory exists
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    # create deterministic folder name
    repo_hash = hashlib.md5(repo_url.encode()).hexdigest()
    repo_path = os.path.join(CACHE_DIR, repo_hash)

    # reuse existing clone
    if os.path.exists(repo_path):
        return repo_path

    try:
        Repo.clone_from(repo_url, repo_path, depth=1)
    except Exception as e:
        raise Exception(f"Git clone failed: {str(e)}")

    return repo_path
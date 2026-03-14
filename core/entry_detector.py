import os


ENTRY_CANDIDATES = [
    "main.py",
    "app.py",
    "run.py",
    "server.py",
    "index.py",
    "index.js",
    "app.js",
    "server.js",
    "main.js",
    "index.html"
]


def detect_entry_points(files):
    """
    Detect probable entry points in a repository.
    """

    detected = []

    for file in files:

        name = os.path.basename(file).lower()

        if name in ENTRY_CANDIDATES:
            detected.append(file)

    return detected
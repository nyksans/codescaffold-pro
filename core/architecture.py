import os


def detect_architecture(files):
    """
    Classify repository files into architecture layers.
    """

    layers = {
        "frontend": [],
        "logic": [],
        "algorithms": [],
        "backend": [],
        "assets": [],
        "other": []
    }

    for file in files:

        name = os.path.basename(file).lower()

        # Frontend
        if name.endswith(".html") or name.endswith(".css"):
            layers["frontend"].append(file)

        # JavaScript logic
        elif name.endswith(".js"):

            if "algo" in name or "algorithm" in name:
                layers["algorithms"].append(file)
            else:
                layers["logic"].append(file)

        # Backend
        elif name.endswith(".py"):
            layers["backend"].append(file)

        # Assets
        elif name.endswith(".png") or name.endswith(".jpg") or name.endswith(".svg"):
            layers["assets"].append(file)

        else:
            layers["other"].append(file)

    return layers
import os
import ast
import re


def parse_repository(repo_path: str):
    """
    Scan repository and extract file dependencies
    and code structure information.
    """

    dependencies = {}
    structure = {}

    all_files = []

    # first pass: collect all files
    for root, dirs, files in os.walk(repo_path):

        if ".git" in root:
            continue

        for file in files:

            full_path = os.path.join(root, file)

            all_files.append(file)

    # second pass: parse files
    for root, dirs, files in os.walk(repo_path):

        if ".git" in root:
            continue

        for file in files:

            full_path = os.path.join(root, file)

            imports = []
            classes = []
            functions = []

            try:
                with open(full_path, "r", encoding="utf8") as f:
                    content = f.read()
            except:
                continue

            # --------------------------
            # Python parsing
            # --------------------------

            if file.endswith(".py"):

                try:

                    tree = ast.parse(content)

                    for node in ast.walk(tree):

                        if isinstance(node, ast.Import):

                            for name in node.names:
                                imports.append(clean_import(name.name))

                        elif isinstance(node, ast.ImportFrom):

                            if node.module:
                                imports.append(clean_import(node.module))

                        elif isinstance(node, ast.ClassDef):
                            classes.append(node.name)

                        elif isinstance(node, ast.FunctionDef):
                            functions.append(node.name)

                except:
                    pass

            # --------------------------
            # JS parsing
            # --------------------------

            if file.endswith(".js"):

                js_import = re.findall(
                    r'import .* from ["\'](.*)["\']', content
                )

                js_require = re.findall(
                    r'require\(["\'](.*)["\']\)', content
                )

                for imp in js_import + js_require:

                    imports.append(clean_import(imp))

                classes += re.findall(r'class\s+(\w+)', content)

                functions += re.findall(r'function\s+(\w+)', content)

            # --------------------------
            # HTML parsing
            # --------------------------

            if file.endswith(".html"):

                scripts = re.findall(
                    r'<script.*src=["\'](.*)["\']',
                    content
                )

                for s in scripts:
                    imports.append(clean_import(s))

            # filter dependencies to local files only
            filtered_imports = []

            for imp in imports:

                if imp + ".py" in all_files:
                    filtered_imports.append(imp + ".py")

                elif imp + ".js" in all_files:
                    filtered_imports.append(imp + ".js")

                elif imp in all_files:
                    filtered_imports.append(imp)

            dependencies[file] = list(set(filtered_imports))

            structure[file] = {
                "classes": classes,
                "functions": functions
            }

    return dependencies, structure, all_files


def clean_import(name: str):
    """
    Normalize import paths
    """

    name = name.replace("./", "")
    name = name.replace("../", "")

    name = name.split("?")[0]

    name = os.path.basename(name)

    return name
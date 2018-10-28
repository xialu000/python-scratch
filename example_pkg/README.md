## Example Python Package
Tutorials used:

- https://packaging.python.org/tutorials/packaging-projects/

# Project Structure:
```
/example_pkg
    /example_pkg
        __init__.py
    setup.py
    LICENSE (optional for now)
    README.md
```

Licenses can be found from https://choosealicense.com

# Uploading

- Make sure setuptools & wheel packages are up-to-date.
- Generate dist directory:
```
    $ python setup.py sdist bdist_wheel

    ...

    $ ls dist/
    example_pkg-0.0.1-py3-none-any.whl
    example_pkg-0.0.1.tar.gz
```
- `tar.gz` file is source archive, `whl` file is a built distribution; good practice dictates uploading source archive (`tar.gz`)  & provide built archives (`.whl`) for supported/compatible projects
- `twine` is used to upload packages (insert target python package index url below):
```
    $ twine upload --repository-url {} dist/*
```


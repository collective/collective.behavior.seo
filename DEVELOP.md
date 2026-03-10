## Develop the package

We use tox

Run lint:

```
tox -e lint
```

Check dependencies:

```
tox -e dependencies
```

Check circular dependencies:

```
tox -e circular
```

run all tests

```
tox -e coverage
```

configure the package with plone/meta

```
uvx --from plone.meta config-package --no-commit . --branch=current
```

### Install and Start a Testinstance

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

```
pip install -r requirements.txt
```

```
uvx cookiecutter -f --no-input --config-file instance.yaml gh:plone/cookiecutter-zope-instance
```

```
runwsgi -v instance/etc/zope.ini
```

Open your browser and goto: http://localhost:8080
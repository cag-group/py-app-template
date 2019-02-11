## Initial setup

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip3 install -r requirements.txt
```

Original install:
```
pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
pip3 install matplotlib
pip3 install keras
```

## Add package

Lookup the package version you want to install on the package home page, or run

```
pip3 install <packagename>
```

and note the version of the installed package. Add it to `requirements.txt`

Do not use `pip3 freeze` because it will also list dependent packages and thus hiding which are our direct dependencies.

## Upgrade package

Conservative upgrade:
```
pip3 install <packagename> --upgrade
```

Upgrading with "eager" gives the same package version as we would have ended up with if we installed the new version from start.

```
pip3 install <packagename> --upgrade --upgrade-strategy eager
```

## Reinstalling everything

```
rm -rf venv
```

then follow procedure "Initial setup".

## Run in docker

```
docker build -t python-service .
docker rm -f python-service
docker run --name python-service -p 8080:8080 python-service
```

## Run/debug in Intellij

- In "Platform settings", add a new "Python SDK" of type "Virtualenv environment", select "Existing environment" and point Python SDK home path to: `/<app-folder>/venv/bin/python`
- Right-click on `main.py` and select `Debug` or `Run`

## Run tests

- In Intellij, right click and select Run on a test file
- In Intellij, right click and select Run on the a folder "test"
- Run all tests in project: python test_suite.py

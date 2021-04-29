# ML Aide tutorial
## Link
https://docs.mlaide.com/

## Setup

To run this tutorial we use [pyenv](https://github.com/pyenv/pyenv) and 
[virtualenv](https://virtualenv.pypa.io/en/latest/) to create a virtual 
environment. All dependencies will be installed in the virtual environment.

1. Create virtual environment
```
virtualenv venv
```

2. Activate virtual environment
```
source venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

### MacOS
Currently, there is a bug in the python ecosystem to run with the latest MacOS 
version. Therefore, you have to run the following command in your shell before 
installing dependencies:
```
export SYSTEM_VERSION_COMPAT=1
```

## Start
```
cd boston-house-prcing
python app.py
```

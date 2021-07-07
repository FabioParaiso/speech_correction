## speech_correction

*[ TODO Add project description]*

## How to Run

First, make sure that you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed and install the project.

```shell
mkvirtualenv speech_correction
pip install -e 'git+https://github.com/FabioParaiso/speech_correction.git.git#egg=speech'
```

> For a private repository accessible only through an SSH authentication, substitute `git+https://github.com` with `git+ssh://git@github.com`.

*[ TODO Add instructions to run package scritps ]*

## How to Contribute

First, make sure that you have [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed and install the project in development mode.

```shell
mkvirtualenv speech_correction
git clone https://github.com/FabioParaiso/speech_correction.git.git
cd speech_correction
pip install -r requirements.txt
pip install -e .
pip freeze | grep -v speech > requirements.txt
```

> For a private repository accessible only through an SSH authentication, substitute `https://github.com/` with `git@github.com:`.

Then, create or select a GitHub branch and have fun... 
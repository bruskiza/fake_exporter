# fake_exporter

Workings for generating fake exporters.

## Nginx

Currently, start Nginx from the current directory:

```bash
nginx -c nginx.conf -p . -e error.log
```

## Job Generator

Run the following:

```bash
pipenv --python 3.8
pipenv shell
pipenv sync
python generator.py --help
```


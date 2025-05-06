# Test configuration

### add config.ini to ./tests (adjust IP and Port accordingly):

```ini
[test_server]
IP = 127.0.0.1
PORT = 65432
```


### run tests (from repo root dir):

```bash
coverage run -m unittest discover -v ./tests/unit
```

### get test results:

```bash
coverage report -m
```

# Jadlog Tracking Monitor

This Python script monitors the package tracking information based
on informed CTE code and timeout set in seconds


## Usage/Examples

First install the dependencies


```bash
pip install -r requirements.txt
```

And execute passing two arguments

```bash
python3 jadlog-tracking.py xxxxxxxxxxx 1800
```

#### Arguments:
- CTE code: xxxxxxxxxxx in example
- Seconds to update: 1800 in example, 30 minutes

### How to get CTE code

First track your package in carrier website, press F12,
Network tab and click 'Mostrar detalhes'. A request to https://www.jadlog.com.br/siteInstitucional/tracking_dev.jad?cte=
will be made and its there! Your CTE code you need in this script.

## Be careful

Set a reasonable timeout, before you get blocked or get wrong responses
# UVRS2023

A dashboard for [UVRS2023](https://uppervalleyrunningclub.org/2023-upper-valley-running-series)
scoring.

## Previous years

* [https://github.com/michaelmusty/UVRS2022](https://github.com/michaelmusty/UVRS2022)

## Environment

```{shell}
pip install isort loguru black mypy numpy pandas bs4 requests selenium lxml webdriver-manager dash plotly PyPDF2 fuzzywuzzy gunicorn spacy fuzzy gensim html5lib
```

```{shell}
pip freeze > requirements.txt
```

We also need to download the language model

```{shell}
python -m spacy download en_core_web_sm
```

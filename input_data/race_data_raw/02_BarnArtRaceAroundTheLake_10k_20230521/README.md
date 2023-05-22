# -> race_data_raw -> race_data

## -> race_data_raw

To extract the raw race data these references were helpful:

* [medium article on web scraping](https://medium.com/analytics-vidhya/scraping-tables-from-a-javascript-webpage-using-selenium-beautifulsoup-and-pandas-cbd305ca75fe)

* [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager)

For some reason typing in the url manually works, but using `driver.get(url)` throws an error,
so detailing the steps in `get_race_data_raw.py` here:

First install webdriver

```{python}
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
```

Now, a window should pop up and you need to enter the url of the results page.
I thought the following would work, but it is different somehow...

```{python}
url_5k = "https://runsignup.com/Race/Results/15854#resultSetId-382432;perpage:5000"
url_10k = "https://runsignup.com/Race/Results/15854#resultSetId-382433;perpage:5000"

# url = url_5k
url = url_10k

driver.get(url)
```

Now that you have your driver
(after enter one of the above urls),
get your soup

```{python}
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="lxml")
tables = soup.find_all("table")
```

From your soup you can get a table

```{python}
import pandas as pd  # type: ignore
dfs = pd.read_html(str(tables))
assert len(dfs) == 1
df = dfs[0]
```

And then write the table to `race_data_raw/`

```{python}
# df.to_csv("input_data/race_data_raw/02_BarnArtRaceAroundTheLake_10k_20230521/5k_raw.csv")
df.to_csv("input_data/race_data_raw/02_BarnArtRaceAroundTheLake_10k_20230521/10k_raw.csv")
```

## race_data_raw -> race_data

Once you have `5k_raw.csv` and `10k_raw.csv` in `input_data/race_data_raw/02_BarnArtRaceAroundTheLake_10k_20230521/` directory
you can populate `race_data` via `02_race_data_raw_to_race_data.py`

```{python}
python input_data/race_data_raw/02_BarnArtRaceAroundTheLake_10k_20230521/02_race_data_raw_to_race_data.py
```

## edits

Note that all edits are made to `input_data/race_data/*.csv` instead of editing the `*_raw.csv` files.

* There are two "John Murphy"s in the results, so had to determine which one is "John Murphy IV" and edit the last name in the race results to match "John Murphy IV" in the UVRS roster.

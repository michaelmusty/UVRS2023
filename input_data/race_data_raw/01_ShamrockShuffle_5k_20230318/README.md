# getting and transforming race results

## -> race_data_raw

Download `.csv` from
[http://www.iresultslive.com/?op=summary&eid=5564](http://www.iresultslive.com/?op=summary&eid=5564)
and write to file named `5k_raw.csv`

## race_data_raw -> race_data

Once you have `5k_raw.csv` in the `input_data/01_ShamrockShuffle_5k_20230318/`,
you can populate `race_data` via `race_data_raw_to_race_data.py`

```{python}
python input_data/race_data_raw/01_ShamrockShuffle_5k_20230318/race_data_raw_to_race_data.py
```

## tweaks to `5k.csv`

removed `Unknown runner` record from `5k.csv`

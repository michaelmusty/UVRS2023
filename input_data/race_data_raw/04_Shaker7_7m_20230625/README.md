# -> race_data_raw -> race_data

## -> race_data_raw

[http://www.iresultslive.com/?op=downloadcsv&eid=5670&racename=7Miler](http://www.iresultslive.com/?op=downloadcsv&eid=5670&racename=7Miler)

## race_data_raw -> race_data

Once you have `4m_raw.csv` in `input_data/race_data_raw/04_Shaker7_7m_20230625/` directory
you can populate `race_data` via `04_race_data_raw_to_race_data.py`

```{shell}
python input_data/race_data_raw/04_Shaker7_7m_20230625/04_race_data_raw_to_race_data.py
```

## tweaks to `4m.csv`

Note that all edits are made to `input_data/race_data/*.csv` instead of editing the `*_raw.csv` files.

# -> race_data_raw -> race_data

## -> race_data_raw

[http://www.iresultslive.com/?op=downloadcsv&eid=5661&racename=4Miler](http://www.iresultslive.com/?op=downloadcsv&eid=5661&racename=4Miler)

## race_data_raw -> race_data

Once you have `4m_raw.csv` in `input_data/race_data_raw/03_SkipsRun_4m_20230618/` directory
you can populate `race_data` via `03_race_data_raw_to_race_data.py`

```{shell}
python input_data/race_data_raw/03_SkipsRun_4m_20230618/03_race_data_raw_to_race_data.py
```

## tweaks to `4m.csv`

Note that all edits are made to `input_data/race_data/*.csv` instead of editing the `*_raw.csv` files.

[https://github.com/michaelmusty/UVRS2023/issues/6](https://github.com/michaelmusty/UVRS2023/issues/6)

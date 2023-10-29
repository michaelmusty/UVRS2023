# -> race_data_raw -> race_data

## -> race_data_raw

Download csvs from [http://www.iresultslive.com/?eid=5835](http://www.iresultslive.com/?eid=5835)

## race_data_raw -> race_data

Once you have `12k_raw.csv` and `5k_raw.csv` in `input_data/race_data_raw/08_TigerRun_12k_20231029/` directory
you can populate `race_data` via `08_race_data_raw_to_race_data.py`

```{shell}
python input_data/race_data_raw/08_TigerRun_12k_20231029/08_race_data_raw_to_race_data.py
```

## tweaks to `12k.csv` and `5k.csv`

Note that all edits are made to `input_data/race_data/*.csv` instead of editing the `*_raw.csv` files.

[https://github.com/michaelmusty/UVRS2023/issues/7](https://github.com/michaelmusty/UVRS2023/issues/7)

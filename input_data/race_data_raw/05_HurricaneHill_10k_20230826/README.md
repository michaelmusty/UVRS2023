# -> race_data_raw -> race_data

## -> race_data_raw

[http://wnhtrs.com/index.php?n=hurricane_hill_5k10k_5](http://wnhtrs.com/index.php?n=hurricane_hill_5k10k_5)

## race_data_raw -> race_data

Once you have `10k_raw.csv` and `5k_raw.csv` in `input_data/race_data_raw/05_HurricaneHill_10k_20230826/` directory
you can populate `race_data` via `05_race_data_raw_to_race_data.py`

```{shell}
python input_data/race_data_raw/05_HurricaneHill_10k_20230826/05_race_data_raw_to_race_data.py
```

## tweaks to `10k.csv` and `5k.csv`

Note that all edits are made to `input_data/race_data/*.csv` instead of editing the `*_raw.csv` files.

[https://github.com/michaelmusty/UVRS2023/issues/7](https://github.com/michaelmusty/UVRS2023/issues/7)

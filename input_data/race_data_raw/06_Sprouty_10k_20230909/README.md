# -> race_data_raw -> race_data

## -> race_data_raw

[http://802timing.com/results/23results/runresults/9.9.23Sproutyoverall.htm](http://802timing.com/results/23results/runresults/9.9.23Sproutyoverall.htm)

## race_data_raw -> race_data

Prompt to get `sprouty_results.csv`: [https://chat.openai.com/share/cea13f40-34fc-4e58-9c49-3933d31fa170](https://chat.openai.com/share/cea13f40-34fc-4e58-9c49-3933d31fa170)

Then modify that to get `10k_raw.csv` and `5k_raw.csv`.

Once you have `10k_raw.csv` and `5k_raw.csv` in `input_data/race_data_raw/06_Sprouty_10k_20230909/` directory
you can populate `race_data` via `06_race_data_raw_to_race_data.py`

```{shell}
python input_data/race_data_raw/06_Sprouty_10k_20230909/06_race_data_raw_to_race_data.py
```

## tweaks to `10k.csv` and `5k.csv`

Note that all edits are made to `input_data/race_data/*.csv` instead of editing the `*_raw.csv` files.

[https://github.com/michaelmusty/UVRS2023/issues/7](https://github.com/michaelmusty/UVRS2023/issues/7)

# -> race_data_raw -> race_data

## -> race_data_raw

[http://pinnacletiming.us/index.php?n=downriver_rail_run_10k_overall_2023](http://802timing.com/results/23results/runresults/9.9.23Sproutyoverall.htm) copy/paste and multicursor to get `downriver_results.txt`

## race_data_raw -> race_data

Prompt to get `10k_raw.csv` from `.txt` file: [https://chat.openai.com/share/aff0d8ba-8add-48aa-9699-df447f07ad2a](https://chat.openai.com/share/aff0d8ba-8add-48aa-9699-df447f07ad2a)

Once you have `10k_raw.csv` in `input_data/race_data_raw/07_Downriver_10k_20231007/` directory
you can populate `race_data` via `07_race_data_raw_to_race_data.py`

```{shell}
python input_data/race_data_raw/07_Downriver_10k_20231007/07_race_data_raw_to_race_data.py
```

## tweaks to `10k.csv`

Note that all edits are made to `input_data/race_data/*.csv` instead of editing the `*_raw.csv` files.

[https://github.com/michaelmusty/UVRS2023/issues/7](https://github.com/michaelmusty/UVRS2023/issues/7)

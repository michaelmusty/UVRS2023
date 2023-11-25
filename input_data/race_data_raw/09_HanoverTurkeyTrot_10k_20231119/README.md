# -> race_data_raw -> race_data

## -> race_data_raw

Download results:

* [5k results](http://nebula.wsimg.com/cd2ada5e5a04707fa415757d6af4e722?AccessKeyId=D31F99142D21B69079D0&disposition=0&alloworigin=1)
* [10k results](http://nebula.wsimg.com/8fa4e4e78cdc5287814ecf8a15d30a1f?AccessKeyId=D31F99142D21B69079D0&disposition=0&alloworigin=1)

These are PDFs, so copy/paste into vscode and modify via copilot and/or multicursor to get `10k_raw.csv` and `5k_raw.csv`.

## race_data_raw -> race_data

Once you have `10k_raw.csv` and `5k_raw.csv` in `input_data/race_data_raw/09_HanoverTurkeyTrot_10k_20231119/` directory
you can populate `race_data` via `09_race_data_raw_to_race_data.py`

```{shell}
python input_data/race_data_raw/09_HanoverTurkeyTrot_10k_20231119/09_race_data_raw_to_race_data.py
```

## tweaks to `10k.csv` and `5k.csv`

Note that all edits are made to `input_data/race_data/*.csv` instead of editing the `*_raw.csv` files.

[https://github.com/michaelmusty/UVRS2023/issues/7](https://github.com/michaelmusty/UVRS2023/issues/7)

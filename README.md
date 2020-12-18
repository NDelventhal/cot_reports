<!-- TOC -->
## Table of Content
- [cot-reports](#cot-reports) 
- [Background](#background)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)
<!-- /TOC -->

## cot-reports
**cot-reports** is a Python library for fetching the Commitments of Trader reports of the of the Commodity Futures Trading Commission (CFTC). The following Commitments of Trader reports are supported: Legacy Futures-only, Legacy Futures-and-Options, Supplemental Futures-and-Options, Disaggregated Futures-only, Disaggregated Futures-and-Options, Traders in Financial Futures (TFF) Futures-only and Traders in Financial Futures (TFF) Futures-and-Options.

Please note: The functionality maybe interrupted in case any changes in the publication occur or in case the website is not available.  

## Background


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cot-reports

```python
pip install cot-reports (not available yet!)
```
Or install it through the author's Github repository 

```python
pip install git+https://github.com/NDelventhal/cot-reports
```

## Requirements 

The following libraries are required: 
- pandas
- numpy
- requests 
- beautifulsoup4

These libraries can be installed via the package manager [pip](https://pip.pypa.io/en/stable/).

```python
pip install numpy pandas requests beautifulsoup4
```

## Usage

```python

import cot-reports as cot

# Example cot_hist():
df = cot_hist(cot_report_type= "traders_in_financial_futures_futopt")
# cot_hist() downloads the historical bulk file for the specified report typ, in this example of the   Returns the data as dataframe.

# Example: cot_year()
df = cot_year(year = 2020, cot_report_type = "traders_in_financial_futures_fut")
# cot_year() downloads the  single year file of the specified report type and year. Returns the data as dataframe.

# Example: cot_all()
df = cot_all(cot_report_type="legacy_fut")
# cot_all() downloads the historical bulk file and all remaining single year files of the specified report type.  Returns the data as dataframe.


```

## License

This project is licensed under the [MIT License](https://github.com/NDelventhal/cot-reports/blob/main/LICENSE).

## Contact

- The author: Niall Delventhal - ni.delventhal@gmail.com


<!-- TOC -->
## Table of Content
- [cot_reports](#cot-reports) 
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Introduction to the COT reports](#introduction-to-the-cot-reports)
    - [Data release](#data-release)
    - [COT report types](#cot_report-types)
    - [Format of the reports](#format-of-the-reports)
    - [Classification methodology Legacy reports](#classification-methodology-Legacy-reports)
    - [Data aggregation](#data-aggregation)
    - [Use cases of the COT reports](#use-cases-of-the-COT-reports)
- [Sources](#sources)
- [Roadmap](#roadmap)
- [License](#license)
<!-- /TOC -->

## cot_reports
**cot_reports** is a Python library for fetching the Commitments of Trader reports of the Commodity Futures Trading Commission (CFTC). The following Commitments of Trader reports are supported: Legacy Futures-only, Legacy Futures-and-Options Combined, Supplemental Futures-and-Options Combined, Disaggregated Futures-only, Disaggregated Futures-and-Options Combined, Traders in Financial Futures (TFF) Futures-only and Traders in Financial Futures (TFF) Futures-and-Options Combined.

Please note: The functionality of the libraries' functions may interrupt in case any changes in the publication occur or in case the website is not available.  

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cot_reports 

```python
pip install cot_reports  
```
Or install the library through the author's Github repository 

```python
pip install git+https://github.com/NDelventhal/cot_reports
```

## Requirements 

The following libraries are required: 
- pandas
- requests 
- beautifulsoup4

These libraries can be installed via the package manager [pip](https://pip.pypa.io/en/stable/).

```python
pip install pandas requests beautifulsoup4
```

## Usage

Available report types with the corresponding 'cot_report_type' name used in the library:

| report        | 'cot_report_type'|
| ------------- |-------------| 
| Legacy Report Futures-only | 'legacy_fut'| 
| Legacy Report Futures-and-Options Combined | 'legacy_futopt'| 
| Supplemental Report Futures-and-Options combined  (short format) | 'supplemental_futopt'| 
| Disaggregated Report Futures-only | 'disaggregated_fut'| 
| Disaggregated Report Futures-and-Options Combined | 'disaggregated_futopt'|
| Traders in Financial Futures (TFF) | 'traders_in_financial_futures_fut'| 
| Traders in Financial Futures (TFF) Futures-and-Options Combined | 'traders_in_financial_futures_futopt'| 

Usage examples: 

- ***cot_hist()*** downloads the compressed bulk files for the specified report (cot_report_type) starting  from 1986 (depending on the report type) up to 2016 and returns the data in a dataframe.

- ***cot_year()*** downloads historical single year data for the specified report (cot_report_type) and returns the data in a dataframe (cot_report_type). If the current year is specified, the latest published data is fetched.

- ***cot_all()*** downloads the complete available data, including the latest, of the specified report and returns the data in a dataframe (cot_report_type).

- ***cot_all_reports()*** downloads all available historical information of the available COT reports and returns the data as seven dataframes.


```python
import cot_reports as cot

# Example: cot_hist()
df = cot.cot_hist(cot_report_type= 'traders_in_financial_futures_futopt')
# cot_hist() downloads the historical bulk file for the specified report type, in this example the Traders in Financial Futures Futures-and-Options Combined report. Returns the data as dataframe.

# Example: cot_year()
df = cot.cot_year(year = 2020, cot_report_type = 'traders_in_financial_futures_fut')
# cot_year() downloads the single year file of the specified report type and year. Returns the data as dataframe.

# Example for collecting data of a few years, here from 2017 to 2020, of a specified report:
df = pd.DataFrame()
begin_year = 2017
end_year = 2020
for i in range(begin_year, end_year + 1):
    single_year = pd.DataFrame(cot.cot_year(i, cot_report_type='legacy_futopt')) 
    df = df.append(single_year, ignore_index=True)

# Example: cot_all()
df = cot.cot_all(cot_report_type='legacy_fut')
# cot_all() downloads the historical bulk file and all remaining single year files of the specified report type.  Returns the data as dataframe.
```

## Introduction to the COT reports

To promote its goals of integrity, resilience and vibrancy of the U.S. derivatives markets through regulation, the U.S. Commodity Futures Trading Commission (CFTC) relies on collected data to conduct its functions. The CFTC's functions:

  - market oversight
  - monitoring for liquidity and systemic risk
  - oversight of market participants
  - regulatory compliance
  - enforcement of the Commodity Exchange Act (CEA)
    
In order to conduct these functions, data is seen as a critical asset to the CFTC, which states to have been one of the first federal agencies who implemented a data management organization in 2011. The CFTC is not solely collecting but also publishing a variety of reports on the derivative markets under its jurisdiction. These reports include the Commitment of Traders (COT) reports.

Through the publication of the COT reports the CFTC claims 'to help the public to understand market dynamics.'

The COT reports provide a breakdown of each Tuesday’s open interest for futures and options on futures markets in which 20 or more traders hold positions equal to or above the reporting levels established by the CFTC.

The data is reported to the CFTC by firms, such as:

  - futures commission merchants (FCMs)
  - clearing members
  - foreign brokers
  - exchanges

The actual trader classification is based on the predominant business purpose, which is self-reported by traders on the CFTC Form 401. The classification of a trader can vary for different commodities/markets, if the reported business purposes differ. However, the classifications are subject to review and corrections by the CFTC.

### Data release

The data, which is generally released each Friday at 3:30 pm Eastern time, comes with a lag of three days, as the reported data is typically from previous Tuesday (close). According to the commission the firms report to the CFTC on Wednesday morning. Next, the provided information is then subject to corrections and verifications by the CFTC prior to the release on Friday.

### COT report types

The types of the COT reports:

1. Legacy 

    - physical contracts & non-physical contracts
    - reportable position classifications:
        - non-commercial
        - commercial traders
    - available as Futures-only and Futures-and-Options Combined reports
    - available from 1986 and 1995
    - available in long and short format

2. Supplemental

    - selected agricultural commodity contracts
    - Supplemental reports break down the reportable open interest positions into three trader classifications
    - reportable position classifications:
        - non-commercial
        - commercial
        - index traders
    - available as Futures-and-Options Combined report
    - available from 2006
    - available in short format
    - Why was this report established? With the publication of the Supplemental COT report the CFTC has reacted on the rise of index traders. The commission started to publish the Supplemental report starting in 2006 with a further trader categorization of index traders for selected agricultural products to prevent a blending of traditional commercial positions and also of traditional non-commercial position with index funds positions. With the newly introduced classification of index traders misinterpretation related to export activity buying or selling end-user are avoided, by differentiating between traditional and non-traditional hedgers as well as between traditional non-commercial and index funds open interest. In general from the non-commercial category managed funds, pension funds and other institutional investors that are generally seeking exposure to commodity prices as an asset class in an unleveraged and passively-managed manner through standardized commodity indices are drawn into the index trader categorization. From the commercial category entities, whose positions predominantly reflect hedging of OTC transactions through commodity indices, are drawn into the index trader categorization. The Supplemental reports solved a disadvantage with respect to the usefulness of the information and serves the original intent in publishing the COT data better by enhancing the transparency.   
    
    
3. Disaggregated

    - data on physical contracts, such as contracts on agricultural products, petroleum products, natural gas products etc.
    - reportable position classifications:
        - Producer/Merchant/Processor/User
        - Swap Dealers
        - Managed Money
        - Other Reportable
    - available as Futures-only and Futures-and-Options Combined reports
    - available from 2006
    - available in long and short format
    
4. Traders in Financial Futures

    - data based on non-physical contracts
    - reportable position classifications:
        - Dealer/Intermediary
        - Asset Manager/Institutional
        - Leveraged Funds
        - Other Reportable
    - available as Futures-only and Futures-and-Options Combined reports
    - available from 2006
    - available in long format

### Format of the reports
The COT reports are either available in the short format, the long format or both - as specified above. Within the long format, aside from the additional listing of the concentrations of positions held by the largest four and largest eight traders, the data is grouped by crop year, where appropriate. Except, where not available (cot report type: Supplemental), the library accesses the long format. 

### Data aggregation
Aggregations occur in the reports not only in the classification of the trader, but also by merging future positions with differing expiration dates. Due to this handling continuous sentiment data on a product, referred to as market by the CFTC and within the COT reports, can be derived. As the data is highly aggregated, any results derived from the data should be interpreted with caution. 

### Classification Methodology Legacy reports 

Not only does the Legacy Futures-only COT report offer the greatest available historical data dating back to 1986, the Legacy reports also contain the most markets in comparison to the other COT report types. Unlike the others, the Legacy reports contain data on physical delivery contracts and non-physical delivery (financial) contracts. While the Supplemental and the Disaggregated reports are limited to physical delivery contracts, the Traders in Financial Futures reports are limited to non-physical financial contracts.

Classification Methodology: Legacy reports 

The positions of the market participants in the Legacy reports are broken down into:

- Commercials
    - market participants who use futures contracts for hedging as defined in CFTC Regulation 1.3, 17 CFR 1.3(z) and which hold positions equal to or above the reporting levels established by the CFTC
    - CFTC Form 40 declaration: the trader is engaged in business activities, which can be hedged by the use of futures (or options)
    - Example: A gold mining company, such as Goldcorp or Barrick Gold, would be classified as commercials in gold futures, as well as other merchants, processors or users buying and selling Gold
    - using descriptions of the other reports I derive the commercials to contain primarily producer/merchant/processor/user and swap dealers

- Non-commercials
    - market participant whose positions equal or are above the reporting levels of by the CFTC and are not considered as commercials
    - As a consequence this group is derived to have speculative interest and is commonly considered as speculators
    - using descriptions of the other reports I derive the non-commercials to contain primarily managed money, asset manager/institutional and leveraged funds

- Non-reportable
    - these market participants hold positions below the reporting levels of the CFTC
    - while the to the CFTC reporting firms are not informing the commission on this group, the aggregated non-reportable positions are nevertheless known to the CFTC through its information on the open interest data (and the reported commercials and non-commercials details)
        
### Use cases of the COT reports

There are numerous, partially overlapping, use cases for the COT data of the CFTC.
Here are the ones I can think of: 

1. Regulatory/Academic:
    - formulate recommendations to the CFTC, such as
        - enlarging transparency
        - establishing new monitoring facilities through Machine Learning
        - adding specific changes to the report to improve detecting misbehaviours of markets participants
    - analyse effects of past regulatory changes and regulatory demands
    - analyse price manipulations (this may only be identifiable through the CFTC’s confidential trader-level data, which is not accessible, but less aggregated data than publicly available has been provided to a number of researchers in the past)
    - add research/recommendations on limiting speculative bets on commodities
    - evaluate if other trading commissions (other countries) should establish a COT like database to combat misbehauviours and as a screening tool for market risks
    - analyse the usage of leverage and possible worst case scenarios targeting preventions of financial harm to commercials/investors

2. Central banks:
    - assess liquidity and systemic risk
    - assess bets on/against a currency, evaluate impact of decisions or costs of defending a thresshold in a currency pair; example: the Swiss National Bank (SNB) defended the 1.2 level in the EUR/CHF pair for years up until early 2015 and artificially stabilized the currency through activities, particularly in the treasuries and currency markets (including other CHF cross pairs). Further, the SNB's decision to not continue the support of the price limit caused a significant shock to the EUR/CHF price due to massive long exposure/herding of speculators and a severe liquidity shortage below the mark of 1.2.

3. Market participants:
    - Producers/Merchants: 
        - can monitor the behaviour of their competitors to time actions (hedge positions) or other strategic decisions; example: a farmer might decide on what to grow next season based on the commercial position
    - Speculators: 
        - evaluate if information is priced in (high vs. low position changes after events with potentially high impact)
        - analyse the behaviour of competitors
        - detect the 'mood of the markets' (risk aversion or risk appetite of market participants)
        - derive trading approaches

4. Market observers:
     - for buy-side analysts research
     - for coverage of financial journalists
     - monitoring of changes in positions or their values in a comparable metric, once derived, such as the U.S. dollar
     
5. (Behavioural) Finance:
    - add value to the research of market dynamics and trends/herding
    - analyse reactions/changes in positions prior and following market events, such as interest rate decisions or other macroeconomic factors/shocks
    - comparison/understanding of not only changes in price, but also activities in the markets 
    - effects of political events or geopolitical events
    - detecting mispricing through extremes in the position
    
6. Data vendors:
    - hosting data in a cleaned form (as the data contains somes cleanable parts) for enhanced frictionless access
    
7. Acceptance of new technologies through commercial activities
    - analysis of the acceptance of new technologies, through a screening if evidence for increased commercial interest activities can be found; example: commercial activities in Bitcoin futures at the Chicago Mercantile Exchange (CME) 


## Sources 

- COT reports data source: 
    - [Commitments of Traders - Historical Compressed](https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm)
- Sources of the above information on the CFTC and the COT reports: 
    - [CFTC About: Mission](https://cftc.gov/About/Mission/index.htm)
    - [CFTC Market Reports: Commitments of Traders](https://cftc.gov/MarketReports/CommitmentsofTraders/index.htm) 
    - [CFTC Commission Actions in Response to the 'Comprehensive Review of the Commitments of Traders Reporting Program' (June 21, 2006)](https://www.cftc.gov/sites/default/files/idc/groups/public/@commitmentsoftraders/documents/file/noticeonsupplementalcotrept.pdf)
    - [CFTC FORM 40 STATEMENT OF REPORTING TRADER](https://www.cftc.gov/sites/default/files/idc/groups/public/@forms/documents/file/cftcform40.pdf) 


## Roadmap

- creation of the predecessor of this library within the seminar course 'Statistical Programming and Open Science Methods (PhD-level)' of the Humboldt University of Berlin (Q1 2020)
- adding library to The Python Package Index (PyPI) 


## License

This project is licensed under the [MIT License](https://github.com/NDelventhal/cot_reports/blob/main/LICENSE).

## Contact

- The author: Niall Delventhal - ni.delventhal@gmail.com
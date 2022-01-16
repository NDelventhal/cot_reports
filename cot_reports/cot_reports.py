import pandas as pd
import requests, zipfile, io
from datetime import date
from beautifulsoup4 import BeautifulSoup

# cot_hist - downloads compressed bulk files

def cot_hist(cot_report_type = "legacy_fut"):
    '''Downloads the compressed COT report historical data of the selected report type
    starting from, depending on the selected report type, 1986, 1995 or 2006 until 2016
    from the cftc.gov webpage as zip file, unzips the downloaded folder and returns
    the cot data as DataFrame.  
    
    COT report types:  
    "legacy_fut" as report type argument selects the Legacy futures only report,
    "legacy_futopt" the Legacy futures and options report,
    "supplemental_futopt" the Sumpplemental futures and options reports,
    "disaggregated_fut" the Disaggregated futures only report, 
    "disaggregated_futopt" the COT Disaggregated futures and options report, 
    "traders_in_financial_futures_fut" the Traders in Financial Futures futures only report, and 
    "traders_in_financial_futures_fut" the Traders in Financial Futures futures and options report. 
    
    Args:
        cot_report_type (str): selection of the COT report type. Defaults to "legacy_fut" (Legacy futures only report). 
    
    Returns:
        A DataFrame with differing variables (depending on the selected report type). 
        
    Raises:
        ValueError: Raises an exception and returns the argument options.'''    
    try: 
        if cot_report_type== "legacy_fut": 
           url_end = "deacot1986_2016"
           txt = "FUT86_16.txt"
           print("Selected: COT Legacy report. Futures only.")

        elif cot_report_type == "legacy_futopt": 
           url_end = "deahistfo_1995_2016"
           txt = "Com95_16.txt"
           print("Selected: COT Legacy report. Futures and Options.")

        elif cot_report_type == "supplemental_futopt": 
           url_end = "dea_cit_txt_2006_2016"
           txt = "CIT06_16.txt"
           print("Selected: COT Sumpplemental report. Futures and Options.")
     
        elif cot_report_type == "disaggregated_fut": 
           url_end = "fut_disagg_txt_hist_2006_2016"
           txt = "F_Disagg06_16.txt"
           print("Selected: COT Disaggregated report. Futures only.")

        elif cot_report_type == "disaggregated_futopt": 
           url_end = "com_disagg_txt_hist_2006_2016"
           txt = "C_Disagg06_16.txt"
           print("Selected: COT Disaggregated report. Futures and Options.")

        elif cot_report_type == "traders_in_financial_futures_fut": 
           url_end = "fin_fut_txt_2006_2016"
           txt = "F_TFF_2006_2016.txt" 
           print("Selected: COT Traders in Financial Futures report. Futures only.")

        elif cot_report_type == "traders_in_financial_futures_futopt": 
           url_end = "fin_com_txt_2006_2016"
           txt = "C_TFF_2006_2016.txt" 
           print("Selected: COT Traders in Financial Futures report. Futures and Options.")
    except ValueError:    
           print("""Input needs to be either:
                "legacy_fut", "legacy_futopt", supplemental_futopt",
                "disaggregated_fut", "disaggregated_futopt", 
                "traders_in_financial_futures_fut" or
                "traders_in_financial_futures_futopt" """)
 
    cot_url = "https://cftc.gov/files/dea/history/" + str(url_end) + ".zip"
    req = requests.get(cot_url) 
    z = zipfile.ZipFile(io.BytesIO(req.content))
    z.extractall()
    print("Stored the extracted file", txt, "in the working directory.")
    df = pd.read_csv(txt, low_memory=False)
    return df

## Example:
## df = cot_hist(cot_report_type= "traders_in_financial_futures_futopt")

# cot_year - downloads single years

def cot_year(year = 2020, cot_report_type = "legacy_fut"):    
    '''Downloads the selected COT report historical data for a single year
    from the cftc.gov webpage as zip file, unzips the downloaded folder and returns
    the cot data as DataFrame.
    For the current year selection, please note: updates by the CFTC occur typically weekly.
    Once the documents update by CFTC occured, the updated data can be accessed through 
    this function. The cot_report_type must match one of the following.

    COT report types:  
    "legacy_fut" as report type argument selects the Legacy futures only report,
    "legacy_futopt" the Legacy futures and options report,
    "supplemental_futopt" the Sumpplemental futures and options reports,
    "disaggregated_fut" the Disaggregated futures only report, 
    "disaggregated_futopt" the COT Disaggregated futures and options report, 
    "traders_in_financial_futures_fut" the Traders in Financial Futures futures only report, and 
    "traders_in_financial_futures_fut" the Traders in Financial Futures futures and options report. 
    
    Args:
        cot_report_type (str): selection of the COT report type. Defaults to "legacy_fut" (Legacy futures only report).
        cot_year(int) = year specification as YYYY
    
    Returns:
        A DataFrame with differing variables (depending on the selected report type). 
        
    Raises:
        ValueError: Raises an exception and returns the argument options.'''    
    print("Selected:", cot_report_type)
    try: 
        if cot_report_type== "legacy_fut": 
           rep = "deacot"
           txt ="annual.txt"
       
        elif cot_report_type == "legacy_futopt": 
           rep = "deahistfo"
           txt ="annualof.txt"
      
        elif cot_report_type == "supplemental_futopt": 
           rep = "dea_cit_txt_"
           txt ="annualci.txt"
 
        elif cot_report_type == "disaggregated_fut": 
           rep = "fut_disagg_txt_"
           txt ="f_year.txt"

        elif cot_report_type == "disaggregated_futopt": 
           rep = "com_disagg_txt_"
           txt ="c_year.txt"

        elif cot_report_type == "traders_in_financial_futures_fut": 
           rep = "fut_fin_txt_"
           txt ="FinFutYY.txt"

        elif cot_report_type == "traders_in_financial_futures_futopt": 
           rep = "com_fin_txt_"
           txt ="FinComYY.txt"

    except ValueError:    
        print("""Input needs to be either:
                "legacy_fut", "legacy_futopt", supplemental_futopt",
                "disaggregated_fut", "disaggregated_futopt", 
                "traders_in_financial_futures_fut" or
                "traders_in_financial_futures_futopt" """)
    
    cot_url = "https://cftc.gov/files/dea/history/" + rep + str(year) + ".zip"
    r = requests.get(cot_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    df = pd.read_csv(txt, low_memory=False)  
    print("Downloaded single year data from:", year)
    return df

## Example:
## df = cot_year(year = 2019, cot_report_type = "traders_in_financial_futures_fut")


# cot_all - downloads complete available data of a chosen COT report type

def cot_all(cot_report_type="legacy_fut"): 
    '''Downloads all historical data for the chosen COT report type (compressed historical bulk
    file and all remaining single year files) from the cftc.gov webpage as zip files, 
    unzips the downloaded folders and returns the cot data files merged as a DataFrame.
    The cot_report_type must match one of the following.
    
    COT report types: 
    "legacy_fut" (default) downloads the Legacy Futures only report,
    "legacy_futopt" the Legacy Futures and Options report,
    "supplemental_futopt" the Sumpplemental Futures and Options report,
    "disaggregated_fut" the Disaggregated Futures only report, 
    "disaggregated_futopt" the COT Disaggregated Futures and Options report, 
    "traders_in_financial_futures_fut" the Traders in Financial Futures Futures only report, 
    "traders_in_financial_futures_fut" the Traders in Financial Futures Futures and Options report. 
  
    Args:
        cot_report_type (str): selection of the COT report type. Defaults to "legacy_fut" (Legacy futures only report).
    
    Returns:
        A DataFrame with differing variables (depending on the selected report type). 
        
    Raises:
        ValueError: Raises an exception and returns the argument options.'''  

    df = cot_hist(cot_report_type)
    for i in range(2017, date.today().year+1):
        years = pd.DataFrame(cot_year(i, cot_report_type)) 
        df = df.append(years, ignore_index=True) 
    return df

## Example:
## df = cot_all(cot_report_type="legacy_futopt")

# cot_all_reports - downloads complete available data for all COT report types

def cot_all_reports():   
  '''Downloads all available historical information of all COT reports and returns a dataframe for 
  each of the report types - seven in total. 
  The function iterates through cot_reports.cot_all() for each cot report type. 
  The following DataFrames are returned, listed in the order they are outputted:  
  - "legacy_fut" the Legacy Futures only report,
  - "legacy_futopt" the Legacy Futures and Options report,
  - "supplemental_futopt" the Sumpplemental Futures and Options report,
  - "disaggregated_fut" the Disaggregated Futures only report, 
  - "disaggregated_futopt" the COT Disaggregated Futures and Options report, 
  - "traders_in_financial_futures_fut" the Traders in Financial Futures Futures only report and  
  - "traders_in_financial_futures_fut" the Traders in Financial Futures Futures and Options report. 
  
  Args:
    cot_report_type (str): selection of the COT report type. Defaults to "legacy_fut" (Legacy futures only report).
    
  Returns:
    Seven DataFrames differing in their variables and size. See function description above for further details.'''

  l = ["legacy_fut", "legacy_futopt", "supplemental_futopt", "disaggregated_fut", "disaggregated_futopt", "traders_in_financial_futures_fut", "traders_in_financial_futures_futopt"]

  for report in l: 
    print(report)
    temp = '{}'.format(report)
    vars()[temp] = cot_all(cot_report_type=report)

  return  vars()['{}'.format("legacy_fut")],vars()['{}'.format("legacy_futopt")],vars()['{}'.format("supplemental_futopt")],\
  vars()['{}'.format("disaggregated_fut")],vars()['{}'.format("disaggregated_futopt")],vars()['{}'.format("traders_in_financial_futures_fut")],\
  vars()['{}'.format("traders_in_financial_futures_futopt")]

## Example:
## df_l, df_lo, df_s, df_d, df_do, df_t, df_to = cot_all_reports()

# cot_description

def cot_description():
  '''Scrapes the for the COT legacy report relevant parts of the explanatory notes offered by the CFTC from cftc.gov
  Returns:
    A DataFrames differing in their variables and size.
  '''
  url = 'https://www.cftc.gov/MarketReports/CommitmentsofTraders/ExplanatoryNotes/index.htm'
  res = requests.get(url)
  html_page = res.content
  soup = BeautifulSoup(html_page, 'html.parser')
  text = soup.find_all(text=True)
  from itertools import groupby
  split_at = "Open Interest"
  text = [list(g) for k, g in groupby(text, lambda x: x != split_at) if k][1]
  split_at = "Supplemental Report"
  text = [list(g) for k, g in groupby(text, lambda x: x != split_at) if k][0]
  print("scraped texts from cftc.gov:")
  print(text)
  x = {'var_info': ["open interest (oi)",
                    "reportable positions",
                    "commercial (c) and non-commercial (nc)",
                    "nonreportable positions (nr)",
                    "changes in commitments from previous reports",
                    "spreading",
                    "percent of open interest (oi)",
                    "number of traders (traders)",
                    "old and other futures",
                    "concentration ratios"],        
     'exp_not': [' '.join(text[0:2]),
                 ' '.join(text[3:4]),
                 ' '.join(text[5:10]),
                 ' '.join(text[11:12]),
                 ' '.join(text[13:14]),
                 ' '.join(text[15:16]),
                 ' '.join(text[17:18]), 
                 ' '.join(text[19:20]),
                 ' '.join(text[21:23]), 
                 ' '.join(text[24:25])]}
  df = pd.DataFrame(x, columns = ['var_info', 'exp_not'])
  return df

## Example:
## expl_not = cot_description()
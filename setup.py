import setuptools

setuptools.setup(
    name="cot_reports",
    packages = ["cot_reports"], 
    version="0.1.1",
    license='MIT',  
    url="https://github.com/NDelventhal/cot_grades",
    author="Niall Delventhal",
    author_email="ni.delventhal@gmail.com",
    description="is a Python library, which fetches the Commitments of Trader reports of the Commodity Futures Trading Commission (CFTC). The following COT reports are supported: Legacy Futures-only, Legacy Futures-and-Options, Supplemental Futures-and-Options, Disaggregated Futures-only, Disaggregated Futures-and-Options, Traders in Financial Futures (TFF) Futures-only and Traders in Financial Futures (TFF) Futures-and-Options.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    download_url = 'https://github.com/NDelventhal/cot_reports/archive/v_011.tar.gz',
    install_requires=['pandas','requests','beautifulsoup4'],
    classifiers=['Intended Audience :: Science/Research', 
    'License :: OSI Approved :: MIT License', 
    'Development Status :: 3 - Alpha', 
    'Programming Language :: Python',
    'Programming Language :: Python :: 3'],
)

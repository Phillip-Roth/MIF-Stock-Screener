
import yfinance as yf
import csv
import pandas as pd
from pandas_datareader import data as pdr

#yf.pdr_override()
#data = pdr.get_data_yahoo("AZO LOW NKE SBUX DIS YUM YUMC COP FANG E XOM HP KMI NEE PSX BRK-B FIS MMC MET PYPL PNC SPG ABB CSX GD GE MGA RSG DEO LLY JNJ KR TMO WMT GOOGL GOOG AMZN AAPL AMAT CSCO VZ", 
# start="2015-01-01", end="2021-08-18")

data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        ##tickers = "AZO LOW NKE SBUX DIS YUM YUMC COP FANG E XOM HP KMI NEE PSX BRK-B FIS MMC MET PYPL PNC SPG ABB CSX GD GE MGA RSG DEO LLY JNJ KR TMO WMT GOOGL GOOG AMZN AAPL AMAT CSCO VZ RELI CDOR XL AIR",
        tickers = "MMM ABT ABBV ABMD ACN ATVI ADBE AMD AAP AES AFL A APD AKAM ALK ALB ARE ALGN ALLE LNT ALL GOOGL GOOG MO AMZN AMCR AEE AAL AEP AXP AIG AMT AWK AMP ABC AME AMGN APH ADI ANSS ANTM AON AOS APA AAPL AMAT APTV ADM ANET AJG AIZ T ATO ADSK ADP AZO AVB AVY BKR BLL BAC BBWI BAX BDX BRK-B BBY BIO TECH BIIB BLK BK BA BKNG BWA BXP BSX BMY AVGO BR BRO BF-B CHRW CDNS CZR CPB COF CAH KMX CCL CARR CTLT CAT CBOE CBRE CDW CE CNC CNP CDAY CERN CF CRL SCHW CHTR CVX CMG CB CHD CI CINF CTAS CSCO C CFG CTXS CLX CME CMS KO CTSH CL CMCSA CMA CAG COP ED STZ COO CPRT GLW CTVA COST CTRA CCI CSX CMI CVS DHI DHR DRI DVA DE DAL XRAY DVN DXCM FANG DLR DFS DISCA DISCK DISH DG DLTR D DPZ DOV DOW DTE DUK DRE DD DXC EMN ETN EBAY ECL EIX EW EA EMR ENPH ETR EOG EPAM EFX EQIX EQR ESS EL ETSY EVRG ES RE EXC EXPE EXPD EXR XOM FFIV FAST FRT FDX FIS FITB FE FRC FISV FLT FMC F FTNT FTV FBHS FOXA FOX BEN FCX GPS GRMN IT GNRC GD GE GIS GM GPC GILD GL GPN GS GWW HAL HBI HIG HAS HCA PEAK HSIC HSY HES HPE HLT HOLX HD HON HRL HST HWM HPQ HUM HBAN HII IEX IDXX INFO ITW ILMN INCY IR INTC ICE IBM IP IPG IFF INTU ISRG IVZ IPGP IQV IRM JKHY J JBHT SJM JNJ JCI JPM JNPR K KEY KEYS KMB KIM KMI KLAC KHC KR LHX LH LRCX LW LVS LEG LDOS LEN LLY LNC LIN LYV LKQ LMT L LOW LUMN LYB MTB MRO MPC MKTX MAR MMC MLM MAS MA MTCH MKC MCD MCK MDT MRK FB MET MTD MGM MCHP MU MSFT MAA MRNA MHK TAP MDLZ MPWR MNST MCO MS MOS MSI MSCI NDAQ NTAP NFLX NWL NEM NWSA NWS NEE NLSN NKE NI NSC NTRS NOC NLOK NCLH NRG NUE NVDA NVR NXPI ORLY OXY ODFL OMC OKE ORCL OGN OTIS PCAR PKG PH PAYX PAYC PYPL PENN PNR PBCT PEP PKI PFE PM PSX PNW PXD PNC POOL PPG PPL PFG PG PGR PLD PRU PTC PEG PSA PHM PVH QRVO PWR QCOM DGX RL RJF RTX O REG REGN RF RSG RMD RHI ROK ROL ROP ROST RCL SPGI CRM SBAC SLB STX SEE SRE NOW SHW SPG SWKS SNA SO LUV SWK SBUX STT STE SYK SIVB SYF SNPS SYY TMUS TROW TTWO TPR TGT TEL TDY TFX TER TSLA TXN TXT TMO TJX TSCO TT TDG TRV TRMB TFC TWTR TYL TSN UDR ULTA USB UAA UA UNP UAL UNH UPS URI UHS VLO VTR VRSN VRSK VZ VRTX VFC VIAC VTRS V VNO VMC WRB WAB WMT WBA DIS WM WAT WEC WFC WELL WST WDC WU WRK WY WHR WMB WLTW WYNN XEL XLNX XYL YUM ZBRA ZBH ZION ZTS ABB E HP MGA YUMC ^GSPC",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "5y",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1mo",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = False,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )


#print(data)

#data.to_csv('OneDrive\Desktop\MIF_DATA.csv')
data.to_csv('OneDrive\Desktop\\MIF Stock Screener\MIF_DATA.csv')



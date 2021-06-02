import json
import requests

headers = {
    'x-rapidapi-key': "47144c0053msh094f9e1cdbcae95p183ea8jsn1769f0f55eb2",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

class Market:

    def get_quotes(company):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
        querystring = {"region":"US","symbols":company}
        response = requests.request("GET", url, headers=headers, params=querystring)
        initial = json.loads(response.text)
        return initial 

    def get_stock_close(company):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-spark"
        querystring = {"symbols":company,"interval":"1m","range":"1d"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        initial = json.loads(response.text)
        return initial

    def get_newsarticles(company):
        url = ('https://newsapi.org/v2/everything?'
       'q={}&'
       'qInTitle=bad+awful+terrible+losing+lose'
       'from=2021-05-01&'
       'to=2021-05-29&'
       'sortBy=popularity&'
       'apiKey=af561c8d1d82406cabd4b9f84c43ff32').format(company+'+bad+down+losing+lost+stock')
        response = requests.get(url)
        initial = json.loads(response.text)
        return initial

class Datasort:

    def sort_stock_query(company):
        connect = Market.get_quotes(company)
        averageDailyVolume10Day = connect["quoteResponse"]["result"][0]['averageDailyVolume10Day']
        fiftyTwoWeekLowChangePercent = connect["quoteResponse"]["result"][0]['fiftyTwoWeekLowChangePercent']
        fiftyTwoWeekHighChangePercent = connect["quoteResponse"]["result"][0]['fiftyTwoWeekHighChangePercent']
        trailingPE = connect["quoteResponse"]["result"][0]['trailingPE']
        priceToSales = connect["quoteResponse"]["result"][0]['priceToSales']
        epsTrailingTwelveMonths = connect["quoteResponse"]["result"][0]['epsTrailingTwelveMonths']
        epsForward = connect["quoteResponse"]["result"][0]['epsForward']
        epsCurrentYear = connect["quoteResponse"]["result"][0]['epsCurrentYear']
        epsNextQuarter = connect["quoteResponse"]["result"][0]['epsNextQuarter']
        sharesOutstanding = connect["quoteResponse"]["result"][0]['sharesOutstanding']
        bookValue = connect["quoteResponse"]["result"][0]['bookValue']
        bid = connect["quoteResponse"]["result"][0]['bid']
        ask = connect["quoteResponse"]["result"][0]['ask']
        bidSize = connect["quoteResponse"]["result"][0]['bidSize']
        askSize = connect["quoteResponse"]["result"][0]['askSize']
        counter = 0
        if averageDailyVolume10Day >= 400000:
            counter += 1
        if fiftyTwoWeekLowChangePercent < fiftyTwoWeekHighChangePercent:
            counter += 1
        if trailingPE < bid:
            counter += 1
        if priceToSales < 10:
            counter += 1
        if epsTrailingTwelveMonths > 2:
            counter += 1
        if epsForward < epsTrailingTwelveMonths:
            counter += 1
        if epsCurrentYear < epsTrailingTwelveMonths:
            counter += 1
        if epsNextQuarter > epsCurrentYear:
            counter += 1
        if sharesOutstanding < 1234543:
            counter += 1
        if bid < ask:
            counter += 1
        if askSize > bidSize:
            counter += 1
        return counter

    def sort_financial_query(company):
        connect = Market.get_quotes(company)
        revenue = connect["quoteResponse"]["result"][0]['revenue']
        marketCap = connect["quoteResponse"]["result"][0]['marketCap']
        totalCash = connect["quoteResponse"]["result"][0]['totalCash']
        floatShares = connect["quoteResponse"]["result"][0]['floatShares']
        ebitda = connect["quoteResponse"]["result"][0]['ebitda']
        actualearning1 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["earningsChart"]["quarterly"][0]['actual']
        estimatedearning1 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["earningsChart"]["quarterly"][0]['estimate']
        actualearning2 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["earningsChart"]["quarterly"][1]['actual']
        estimatedearning2 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["earningsChart"]["quarterly"][1]['estimate']
        actualearning3 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["earningsChart"]["quarterly"][2]['actual']
        estimatedearning3 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["earningsChart"]["quarterly"][2]['estimate']
        actualearning4 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["earningsChart"]["quarterly"][3]['actual']
        estimatedearning4 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["earningsChart"]["quarterly"][3]['estimate']
        yearlyrevenue1 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["financialsChart"]["yearly"][0]['revenue']
        yearlyearnings1 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["financialsChart"]["yearly"][0]['earnings']
        yearlyrevenue2 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["financialsChart"]["yearly"][1]['revenue']
        yearlyearnings2 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["financialsChart"]["yearly"][1]['earnings']
        yearlyrevenue3 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["financialsChart"]["yearly"][2]['revenue']
        yearlyearnings3 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["financialsChart"]["yearly"][2]['earnings']
        yearlyrevenue4 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["financialsChart"]["yearly"][3]['revenue']
        yearlyearnings4 = connect["quoteResponse"]["result"][0]["quoteSummary"]["earnings"]["financialsChart"]["yearly"][3]['earnings']
        counter = 0
        if (marketCap*0.30) < revenue:
            counter += 1
        if totalCash > revenue:
            counter += 1
        if floatShares > ebitda:
            counter += 1
        if actualearning1 > estimatedearning1:
            counter += 1
        if actualearning2 > estimatedearning2:
            counter += 1
        if actualearning3 > estimatedearning4:
            counter += 1
        if actualearning4 > estimatedearning4:
            counter += 1
        averageyearlyrevenue = (yearlyrevenue1 + yearlyrevenue2 + yearlyrevenue3 + yearlyrevenue4)/4
        if yearlyrevenue1 > averageyearlyrevenue:
            counter += 1
        if yearlyrevenue2 > averageyearlyrevenue:
            counter += 1
        if yearlyrevenue3 > averageyearlyrevenue:
            counter += 1
        if yearlyrevenue4 > averageyearlyrevenue:
            counter += 1
        averageyearlyearnings = (yearlyearnings1 + yearlyearnings2 + yearlyearnings3 + yearlyearnings4)/4
        if yearlyearnings1 > averageyearlyearnings:
            counter += 1
        if yearlyearnings2 > averageyearlyearnings:
            counter += 1
        if yearlyearnings3 > averageyearlyearnings:
            counter += 1
        if yearlyearnings4 > averageyearlyearnings:
            counter += 1
        return counter

    def sort_closeprice_query(company):
        connect = Market.get_stock_close(company)
        counter = 0
        closeprice = []
        for i in range(99):
            close_price = connect[company]["close"][i]
            closeprice.append(close_price)
        avg = sum(closeprice)/99
        for i in range(len(closeprice)):
            if avg > closeprice[i]:
                counter += 1
        return counter

    def sort_articledata_query(company):
        connect = Market.get_newsarticles(company)
        news = connect["totalResults"]
        counter = 0
        if news < 50:
            counter += 40
        return counter

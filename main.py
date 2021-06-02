from base import Datasort

def main():
    company_name = input('What is the Name of the Company? ')
    stock_name = input('What is the Stock Symbol of the Company? ')
    counter1 = Datasort.sort_stock_query(stock_name)
    counter2 = Datasort.sort_financial_query(stock_name)
    counter3 = Datasort.sort_closeprice_query(stock_name)
    counter4 = Datasort.sort_articledata_query(company_name)
    total_counter = counter1 + counter2 + counter3 + counter4
    percentage_of_worthy_stock = round(((total_counter/166)*100),0)
    print('Below is a list of criteria determining whether ' + company_name + ' is a good stock to purchase:\n[0-40%] == BAD STOCK\n[41-60%] == INTERMEDIATE STOCK\n[61-80%] == GOOD STOCK\n[81-100%] == VERY GOOD STOCK')
    print(company_name+ "'s percentage: ",percentage_of_worthy_stock,'%')

main()
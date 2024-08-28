# Exercício 13.2: Análise de Vendas
#
# 1. Crie um programa que peça ao utilizador para introduzir os valores de vendas diárias de uma semana (7 dias) e armazene esses valores em uma lista.
# 2. Calcule e imprima o total de vendas da semana.
# 3. Calcule e imprima a média diária de vendas.
# 4. Encontre e imprima o dia com a maior e o dia com a menor venda.
# 5. Modifique o programa para permitir que o utilizador introduza os valores de vendas de N dias (onde N é determinado pelo utilizador) e armazene esses valores em uma lista. Calcule e imprima o total, a média, o maior e o menor valor de vendas.
# 6. Escreva os resultados anteriores num ficheiro .csv

def get_sales(number_of_days): 
    sales = {}
    for day in range(1, number_of_days + 1):
        while True:
            try:
                no_of_sales = int(input(f"Sales in Day {day}: "))
                sales[f"Day {day}"] = no_of_sales
                break
            except ValueError:
                print("You should insert a valid integer!")
    return sales

def get_total_and_average_of_sales(sales):
    total_of_sales = sum(sales.values())
    average_daily_sales = total_of_sales / len(sales.values())
    return (total_of_sales, average_daily_sales)

def get_day_with_more_sales(sales):
    day_with_more_sales = (None, 0)
    for day, no_of_sales in sales.items():
        if no_of_sales > day_with_more_sales[1]:
            day_with_more_sales = (day, no_of_sales)
    
    return day_with_more_sales

def get_day_with_less_sales(sales):
    day_with_less_sales = (None, 9999999)
    for day, no_of_sales in sales.items():
        if no_of_sales < day_with_less_sales[1]:
            day_with_less_sales = (day, no_of_sales)
    
    return day_with_less_sales

def save_sales(sales, total_of_sales, average_daily_sales, day_with_more_sales, day_with_less_sales):
    try:
        with open('./data/ex2.csv', 'w') as csvFile:
            csvFile.write("day,number_of_sales\n")
            for day, no_of_sales in sales.items():
                csvFile.write(f"{day},{no_of_sales}\n")
            
            csvFile.write("\ntotal_of_sales,average_daily_sales,day_with_more_sales,day_with_less_sales\n")
            csvFile.write(f"{total_of_sales},{average_daily_sales},{day_with_more_sales},{day_with_less_sales}\n")
            csvFile.close()
    except:
        print("Error opening the file!")

def main():
    try:
        number_of_days = int(input('Please insert the number of days: '))
        sales = get_sales(number_of_days)
        total_of_sales, average_daily_sales = get_total_and_average_of_sales(sales)
        day_with_more_sales = get_day_with_more_sales(sales)
        day_with_less_sales = get_day_with_less_sales(sales)
        print(f"Total of sales: {total_of_sales}")
        print(f"Average daily sales: {average_daily_sales}")
        print(f"Day with more sales: {day_with_more_sales[0]} ({day_with_more_sales[1]})")
        print(f"Day with less sales: {day_with_less_sales[0]} ({day_with_less_sales[1]})")
        save_sales(sales, total_of_sales, average_daily_sales, day_with_more_sales, day_with_less_sales)
    except:
        print("You should insert a valid number of days.")

if __name__ == '__main__':
    main()
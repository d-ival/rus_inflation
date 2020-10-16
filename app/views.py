from csv import DictReader
from django.shortcuts import render

def if_then_else(condition, true_statement, false_statement):
    if condition:
        return true_statement
    else:
        return false_statement

def read_inflation_data(csvf):
    fieldnames = ['year', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', 'total']
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    csv_reader = DictReader(csvf, delimiter=';', fieldnames = fieldnames)
    next(csv_reader) # пропуск заголовков
    return [
        {
            'year': year_data['year'],
            'months': [year_data[month] for month in months],
            'total': float(year_data['total'])
        } for year_data in csv_reader
    ]


def inflation_view(request):
    template_name = 'inflation.html'

    datafile = 'inflation_russia.csv'

    with open(datafile, encoding='utf8', newline='') as csvf:
        context = {
            'inflation_history': read_inflation_data(csvf)
        }

    return render(request, template_name, context)
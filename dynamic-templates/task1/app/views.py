from django.shortcuts import render
from django.conf import settings

import csv, os

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open(os.path.join(settings.BASE_DIR, 'inflation_russia.csv'), 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)

        years = list()
        for year in csvreader:
            arr = list()
            for index, value in enumerate(year):
                if index == 0:
                    arr.append(int(value))
                elif value !='':
                    arr.append(float(value))
                else:
                    arr.append(1000000)
            years.append(arr)

    # print(years)

    context = {'years': years}

    return render(request, template_name,
                  context)
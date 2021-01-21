import json
def read(year, end_year=None):
    with open("./jsons/grand_totals.json", "r") as reports:
        lst_of_dics = json.loads(reports.read())
    if end_year:
      #  for num in range(year,end_year+1): [num for num in range(year,end_year)]
      pass

    else:
        for dic in lst_of_dics:
            if dic['Year'] == year:
                return dic
        
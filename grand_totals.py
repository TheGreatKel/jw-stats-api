import json
def read(year, end_year=None):
#      if end_year:# there happens to be an end year
#           #then we have to combine jsons. Sounds fun!
#         with open(f".jsons/country_reports_{year}.json", "r") as reports:
#             return json.loads(reports.read())[country]
#     else:

    with open("./jsons/grand_totals.json", "r") as reports:
        lst_of_dics = json.loads(reports.read())
        for dic in lst_of_dics:
            if dic['Year'] == year:
                return dic
        
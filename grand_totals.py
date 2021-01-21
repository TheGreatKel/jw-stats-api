import json
def read(year, other_year=None):
    with open("./jsons/grand_totals.json", "r") as reports:
        lst_of_dics = json.loads(reports.read())
    if other_year:
      look_up = {}
      res = []
      if other_year>year:
		for num in range(year,other_year+1):
			look_up[num] = None
      else:
      	for num in range(other_year,year+1):
      		look_up[num] = None
      for dic in lst_of_dics:
      	if dic["Year"] in look_up:
      		res.append(dic)
    else:
        for dic in lst_of_dics:
            if dic['Year'] == year:
                return dic
        
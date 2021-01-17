import json

def read(year, country=None):
	if country:# there happens to be a country
		with open(f"./jsons/country_reports_{year}.json", "r") as reports:
			lst_of_dics = json.loads(reports.read())
		for dic in lst_of_dics:
			if dic['Country or Territory'] == country:
				return dic
	else:
		with open(f"./jsons/country_reports_{year}.json", "r") as reports:
			return json.loads(reports.read())
    
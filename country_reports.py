import json

def read(year, country=None):
	with open(f"./jsons/country_reports_{year}.json", "r") as reports:
			lst_of_dics = json.loads(reports.read())
	if country:
		for dic in lst_of_dics:
			if dic['Country or Territory'] == country:
				return [dic]
	return lst_of_dics
    
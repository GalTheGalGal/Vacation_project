from src.utils.dal import DAL


countries = DAL.get_table("SELECT * FROM countries")

for country in countries:
    print(f"country name: {country["country_name"]}, country id: {
        country["country_id"]}")

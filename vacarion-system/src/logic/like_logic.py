<<<<<<< Updated upstream
import sys
sys.path.insert(1,r"C:\Users\kevin\OneDrive\שולחן העבודה\utils\main\vacarion-system\src\utils")
import dal
con = dal.DAL()

from ..utils import dal
con = dal.DAL()
countries = con.get_table("select * from countries")

for country in countries:
    print(f"country id: {country["country_id"]}, vacation_title: {
          country["vacation_title"]}")


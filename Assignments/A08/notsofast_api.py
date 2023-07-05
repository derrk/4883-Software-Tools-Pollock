
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv



description = """🚀
## 4883 Software Tools - Assignment 8
### FastAPI built api for fetching covid-19 data
"""


app = FastAPI(

    description=description,

)

db = []

# Open the CSV file
# populates the `db` list with all the csv data
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)


def getUniqueCountries():
    global db
    countries = {}

    for row in db:
        print(row)
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())

def getUniqueWhos():
    global db
    whos = {}

    for row in db:
        print(row)
        if not row[3] in whos:
            whos[row[3]] = 0
   
    return list(whos.keys())

def getTotalDeaths():
    total_deaths = 0
    for row in db:
        total_deaths += int(row[5])
    return total_deaths

def getTotalDeathsByCountry(country):
    total_deaths = 0
    for row in db:
        if row[2].lower() == country.lower():
            total_deaths += int(row[5])
    return total_deaths

def getTotalDeathsByRegion(region):
    total_deaths = 0
    for row in db:
        if row[3].lower() == region.lower():
            total_deaths += int(row[5])
    return total_deaths



def getTotalDeathsByRegionAndYear(region, year):
    total_deaths = 0
    for row in db:
        if row[3].lower() == region.lower() and int(row[0][:4]) == year:
            total_deaths += int(row[5])
    return total_deaths

def getTotalDeathsByCountryAndYear(country, year):
    total_deaths = 0
    for row in db:
        if row[2].lower() == country.lower() and int(row[0][:4]) == year:
            total_deaths += int(row[5])
    return total_deaths

def getTotalCases():
    total_cases = 0
    for row in db:
        total_cases += int(row[4])
    return total_cases

def getTotalCasesByCountry(country):
    total_cases = 0
    for row in db:
        if row[2].lower() == country.lower():
            total_cases += int(row[4])
    return total_cases

def getTotalCasesByRegion(region):
    total_cases = 0
    for row in db:
        if row[3].lower() == region.lower():
            total_cases += int(row[4])
    return total_cases

def getTotalCasesByCountryAndYear(country, year):
    total_cases = 0
    for row in db:
        if row[2].lower() == country.lower() and int(row[0][:4]) == year:
            total_cases += int(row[4])
    return total_cases

def getTotalCasesByRegionAndYear(region, year):
    total_cases = 0
    for row in db:
        if row[3].lower() == region.lower() and int(row[0][:4]) == year:
            total_cases += int(row[4])
    return total_cases

def getMaxDeathsCountry():
    max_deaths = 0
    max_country = ""
    country_deaths = {}
    for row in db:
        country = row[2]
        deaths = int(row[5])
        if country not in country_deaths:
            country_deaths[country] = deaths
        else:
            country_deaths[country] += deaths
        if country_deaths[country] > max_deaths:
            max_deaths = country_deaths[country]
            max_country = country
    return max_country, max_deaths

def getMaxDeathsCountryRange(min_date, max_date):
    max_deaths = 0
    max_country = ""
    country_deaths = {}
    for row in db:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        if min_date <= date <= max_date:
            country = row[2]
            deaths = int(row[5])
            if country not in country_deaths:
                country_deaths[country] = deaths
            else:
                country_deaths[country] += deaths
            if country_deaths[country] > max_deaths:
                max_deaths = country_deaths[country]
                max_country = country
    return max_country, max_deaths



@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/countries/")
async def countries():

    return {"countries":getUniqueCountries()}


@app.get("/whos/")
async def whos():

    return {"whos":getUniqueWhos()}

@app.get("/casesByRegion/")
async def casesByRegion(year:int = None):
    """
    Returns the number of cases by region

    """

    # create a dictionary as a container for our results
    # that will hold unique regions. Why, because there 
    # cannot be duplicate keys in a dictionary.
    cases = {}

    # return {'success':False,'message':'no database exists'}

    # loop through our db list
    for row in db:
        
        # If there is a year passed in and that year is not equal to this row
        # then skip the rest of code
        if year != None and year != int(row[0][:4]):
            continue
            
        # this line guarantees that the dictionary has the region as a key
        if not row[3] in cases:
            cases[row[3]] = 0
        
        # this line adds the case count to whatever is at that key location
        cases[row[3]] += int(row[4])    

    # return cases

    return {"data":cases,"success":True,"message":"Cases by Region","size":len(cases),"year":year}

@app.get("/deaths")
async def totalDeaths():
    deaths = getTotalDeaths()
    return {"total_deaths": deaths}

@app.get("/deaths_by_country/{country}")
async def deathsByCountry(country: str):
    deaths = getTotalDeathsByCountry(country)
    if deaths == 0:
        raise HTTPException(status_code=404, detail="Country not found")
    return {"country": country, "total_deaths": deaths}



@app.get("/deaths_by_country_year/{country}/{year}")
async def deathsByCountryAndYear(country: str, year: int):
    deaths = getTotalDeathsByCountryAndYear(country, year)
    if deaths == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"country": country, "year": year, "total_deaths": deaths}

@app.get("/deaths_by_region_year/{region}/{year}")
async def deathsByRegionAndYear(region: str, year: int):
    deaths = getTotalDeathsByRegionAndYear(region, year)
    if deaths == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"region": region, "year": year, "total_deaths": deaths}

@app.get("/deaths_by_region/{region}")
async def deathsByRegion(region: str):
    deaths = getTotalDeathsByRegion(region)
    if deaths == 0:
        raise HTTPException(status_code=404, detail="Region not found")
    return {"region": region, "total_deaths": deaths}

@app.get("/cases")
async def totalCases():
    cases = getTotalCases()
    return {"total_cases": cases}

@app.get("/cases_by_country/{country}")
async def casesByCountry(country: str):
    cases = getTotalCasesByCountry(country)
    if cases == 0:
        raise HTTPException(status_code=404, detail="Country not found")
    return {"country": country, "total_cases": cases}

@app.get("/cases_by_region/{region}")
async def casesByRegion(region: str):
    cases = getTotalCasesByRegion(region)
    if cases == 0:
        raise HTTPException(status_code=404, detail="Region not found")
    return {"region": region, "total_cases": cases}

@app.get("/cases_by_country_year/{country}/{year}")
async def casesByCountryAndYear(country: str, year: int):
    cases = getTotalCasesByCountryAndYear(country, year)
    if cases == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"country": country, "year": year, "total_cases": cases}

@app.get("/cases_by_region_year/{region}/{year}")
async def casesByRegionAndYear(region: str, year: int):
    cases = getTotalCasesByRegionAndYear(region, year)
    if cases == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"region": region, "year": year, "total_cases": cases}

@app.get("/max_deaths")
async def maxDeaths():
    country, deaths = getMaxDeathsCountry()
    if country == "":
        raise HTTPException(status_code=404, detail="No data found")
    return {"country": country, "total_deaths": deaths}

@app.get("/max_deaths_range")
async def maxDeathsRange(min_date: str = Query(...), max_date: str = Query(...)):
    min_date = datetime.strptime(min_date, '%Y-%m-%d')
    max_date = datetime.strptime(max_date, '%Y-%m-%d')
    country, deaths = getMaxDeathsCountryRange(min_date, max_date)
    if country == "":
        raise HTTPException(status_code=404, detail="No data found")
    return {"country": country, "total_deaths": deaths}

"""
Separator 


"""

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

@app.get("/get_values1/")
def get_values1(index1: int=None, index2: int=None):
    try:
        value1 = my_list[index1]
        value2 = my_list[index2]
        return [value1, value2]
    except IndexError:
        return {"error": "Invalid index provided."}


@app.get("/get_values2/{index1}/{index2}")
def get_values2(index1: int, index2: int):
    try:
        value1 = my_list[index1]
        value2 = my_list[index2]
        return [value1, value2]
    except IndexError:
        return {"error": "Invalid index provided."}
    


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=5000, log_level="debug", reload=True) #host="127.0.0.1"
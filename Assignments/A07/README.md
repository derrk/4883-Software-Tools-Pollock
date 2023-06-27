## Assignment 07
### Weather Webscraper and GUI
#### Description: 
This program uses beautiful soup to scrap data from wunderground.com weather website
The user will first run the 'get_weather.py' file, this will call the 'gui.py' and create a form
window where the user will enter the weather parameters they wish to retrieve. Once they have entered the
location, the gui will return a url that will be used to get that weather data for the given parameters. 
A function buildweather_gui will then run and generate a table populated with the requested weather data.

| # | File    | Description      |
|:-: | ------- | ----------------- |
| 01 | [airport codes](airport-codes.csv)| Airport codes needed for entering location code |
| 02 | [get_weather](get_weather.py) | Main file that will call the necessary files |
| 03 | [parsed data](https://github.com/derrk/4883-Software-Tools-Pollock/blob/main/parsed.json) | Data from weather site formatted in json |
| 04 | [gui](gui.py) | File containing the functions that build the gui |
| 05 | [weather gui](getweather_gui.png) | Window for user to enter parameters |
| 06 | [output](output_table.png) | Output example from given weather parameters |

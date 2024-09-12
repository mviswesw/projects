# #selinium - Only for browser
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager

# import chromedriver_autoinstaller 
# from selenium.webdriver.chrome.options import Options

# chromedriver_autoinstaller.install()
# options = Options()
# driver =  webdriver.Chrome(options=options)
# # # Initialize the WebDriver using webdriver_manager
# # driver = webdriver.Chrome(ChromeDriverManager().install())

# # Open Google
# driver.get("https://www.nseindia.com/")
# # <textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="Search" value="" jsaction="paste:puy29d;" aria-label="Search" aria-autocomplete="both" aria-expanded="true" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwiotu2zpKiIAxWLD1kFHZjfDrgQ39UDCBA" aria-activedescendant="" style=""></textarea>
# # Find the search box element

# nifty50 = driver.find_element("xpath", '//*[@id="tabList_NIFTY50"]/div/p[2]')
# print(nifty50.text)
# nifty_next50 = driver.find_element("xpath", '//*[@id="tabList_NIFTYNEXT50"]/div/p[2]')
# print(nifty_next50.text)
# nifty_midcapselect = driver.find_element("xpath", '//*[@id="tabList_NIFTYMIDCAPSELECT"]/div/p[2]')
# print(nifty_midcapselect.text)
# nifty_bank = driver.find_element("xpath", '//*[@id="tabList_NIFTYBANK"]/div/p[2]')
# print(nifty_bank.text)

# nifty_financialservices = driver.find_element("xpath", '//*[@id="tabList_NIFTYFINANCIALSERVICES"]/div/p[2]')
# print(nifty_financialservices.text)


import os, time
from influxdb_client_3 import InfluxDBClient3, Point

token = os.environ.get("INFLUXDB_TOKEN")
org = "lelele"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)
# # export INFLUXDB_TOKEN=U0V6bsgaedRJf5Wcs-7xo16_K2RSWwOJd76cWfOdivAtuYkZIS9JRoR3Sdfd4M_AnoqrG06i0KpVVW8H3HZtIg==
data = {

}
database="mybucket"

data = {
  "point1": {
    "stock": "nifty50",
    "value": "24,936.40",
  },
  "point2": {
    "stock": "nifty_next50",
    "value": "74,572.90",
  },
  "point3": {
    "stock": "nifty_midcapselect",
    "value": "13,007.45",
  },
  "point4": {
    "stock": "nifty_bank",
    "value": "51,117.80",
  },
  "point5": {
    "stock": "nifty_financialservices",
    "value": "23,722.15",
  }
}

for key in data:
  point = (
    Point("index")
    .tag("stock", data[key]["stock"])
    .field("value", data[key]["value"])
  )
  client.write(database=database, record=point)
  time.sleep(1) # separate points by 1 second

# print("Complete. Return to the InfluxDB UI.")

# query = """SELECT *
# FROM 'census'
# WHERE time >= now() - interval '24 hours'
# AND ('bees' IS NOT NULL OR 'ants' IS NOT NULL)"""

# # Execute the query
# table = client.query(query=query, database="mybucket", language='sql')

# # Convert to dataframe
# df = table.to_pandas().sort_values(by="time")
# print(df)

# Enter the search query and submit
# search_box.send_keys("Selenium Python")
# search_box.send_keys(Keys.RETURN)

# # Wait for results to load
# driver.implicitly_wait(10)  # seconds

# # Print the titles of the search results
# results = driver.find_elements("css selector", "h3")
# for result in results:
#     print(result.text)

# # Keep the browser open until user input
# input("Press Enter to close the browser...")

# # Close the WebDriver
# driver.quit()

"""
https://www.nseindia.com/
"""
# store 
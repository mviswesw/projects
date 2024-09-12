#selinium - Only for browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import chromedriver_autoinstaller 
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()
options = Options()
driver =  webdriver.Chrome(options=options)
# # Initialize the WebDriver using webdriver_manager
# driver = webdriver.Chrome(ChromeDriverManager().install())

# Open Google
driver.get("https://www.google.com")
# <textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="Search" value="" jsaction="paste:puy29d;" aria-label="Search" aria-autocomplete="both" aria-expanded="true" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwiotu2zpKiIAxWLD1kFHZjfDrgQ39UDCBA" aria-activedescendant="" style=""></textarea>
# Find the search box element
search_box = driver.find_element("name", "q")

# Enter the search query and submit
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
driver.implicitly_wait(10)  # seconds

# Print the titles of the search results
results = driver.find_elements("css selector", "h3")
for result in results:
    print(result.text)

# Keep the browser open until user input
input("Press Enter to close the browser...")

# Close the WebDriver
driver.quit()

"""
https://www.nseindia.com/
"""
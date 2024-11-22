# Externals.
from selenium_browser import SeleniumBrowser

# Locals.

# Hard-coded vals for ease-of-use.
url = "https://api.apyhub.com/convert/word-file/pdf-file"

def web_nav():
    print(f"WEBSURF INIT.")
    websurf = SeleniumBrowser()
    print(f"WEBSURF NAV.")
    # websurf.wait(10)
    websurf.navigate_to(url)

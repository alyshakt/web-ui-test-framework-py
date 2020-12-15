# web-ui-test-framework-py by Alysha Kester-Terry https://github.com/alyshakt

A Python based Web UI test automation framework using an object-oriented design. Just the bare bones.

Run `pip install -r requirements.txt` on the directory to install dependencies

This project uses Selenium https://www.selenium.dev/ and Chrome. -If you already have Chrome on your machine, you don't
need to do anything special to use it.

I built this project to be able to run using pytest https://docs.pytest.org
To run all tests, simply run `pytest tests -s` in the command line.

Find screenshots in test-reports/screenshots

I use the `record_xml_attribute` in my tests because I want useable xml reporting output to integrate with XRay
importing capabilities with Jira. It is not necessary to use it if you do not care for that output in your xml document.

To Run Headless with Chrome, open your test with the following code:

```
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(chrome_options=options)
```

You'll see a `SearchEngineType` class to define Enums for switching between types of search engines. This is simply an
example of how you could use Enums like this to standardize initial inputs and make things easier for testers to switch
between websites, environments or anything else you can think of. This Enum is used in `web_app_setup.py` to define the
URL for the Enum and pass it on to navigate to that URL.

Screenshots are automatically named by the created date and saved in PNG format, with the option to add a name to append
to the date.

This Base Page object strategy was gleaned with much gratitude from
http://elementalselenium.com/tips/9-use-a-base-page-object

# web-ui-test-framework-py by Alysha Kester-Terry https://github.com/alyshakt

A Python based test client for web UI testing. This could easily be expanded to do API or Database testing as well.

Use
===
Install IntelliJ https://www.jetbrains.com/idea/download/
Community edition

**MacOS**
---

-Install Brew if you don't already have it.
-Run `brew install node` to be sure you have node installed.

-Run `brew install chromedriver` and `brew install geckodriver`

-Run `pip3 install -r requirements.txt` on the directory to install dependencies. -This project uses
Selenium https://www.selenium.dev/ and Chrome or Firefox. -If you already have Chrome or Firefox on your machine, you
don't need to do anything special to use it.

**Windows**
---
Install chocolatey from here: https://chocolatey.org/install

-Run `choco install nodejs`

-Run `choco install chromedriver`

-Run `choco install selenium-gecko-driver`

-Run `choco install python --version=3.9.0`


**Everyone**
---
-Install The Python Community Edition Plugin for IntelliJ https://plugins.jetbrains.com/plugin/7322-python-community-edition

-Install the Requirements Plugin for Intellij https://plugins.jetbrains.com/plugin/10837-requirements

-You'll need to make sure you keep Chrome and Firefox updated to the latest desktop versions

-I built this project to be able to run using pytest runners https://docs.pytest.org
-You can run tests by
inputting `pytest --environment="{test, uat, dev}" --browser="{firefox, chrome, edge}" -s tests/{your directory path} --html=test-reports/runreport.html` into the command
line or, Using IntelliJ's pytest runner, you can run tests. Find the runner under /tests.

-Note that the test runner is configured to run using the Python interpreter of the project, so you will need to define
your python interpreter for your project, or change the runner to refer to another interpreter.

-You must define an *environment* variable when running like `--environment='test' or --environment='uat'`

-You must define a *browser* variable when running like `--browser='chrome' or --browser='firefox'`

-Optionally, you can define an *headless* variable when running like `--headless='true' or --headless='false'`

-To add logging output to the console, add `-o log_cli=true` to arguments

-To get a junit XML report, add `--junitxml=<path to save the output file to>.xml`; I like to save reports to
\test-reports

-To get an HTML report, add `--html=<path to save the file to>.html`; I like to save reports to \test-reports

-Find screenshots and HTML reports in test-reports/{environment}/screenshots.

Test Runner configurations are found in /runners

I use the `record_xml_attribute` in my tests because I want useable xml reporting output to integrate with XRay
importing capabilities with Jira. It is not necessary to use it if you do not care for that output in your xml document.

Screenshots are automatically named by the created date and saved in PNG format, with the option to add a name to append
to the date.
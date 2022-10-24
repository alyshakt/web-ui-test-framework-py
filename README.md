# web-ui-test-framework-py by Alysha Kester-Terry https://github.com/alyshakt

A Python based test client for web UI and backend cross-functional testing.

Use
===
-You'll need to make sure you keep Chrome and Firefox updated to the latest desktop versions

-Use Personal access token generated from GitHub to authenticate for VCS in IntelliJ

**MacOS**
---

-Install Brew if you don't already have it.
-Run `brew install node` to be sure you have node installed.

-Run `brew install chromedriver` and `brew install geckodriver`

-Run  `brew update`

-Install Python 3.9 or later

-Install latest Chrome and Firefox

-Run `pip3 install -r requirements.txt` on the directory to install dependencies. -This project uses
Selenium https://www.selenium.dev/ and Chrome or Firefox. -If you already have Chrome or Firefox on your machine, you
don't need to do anything special to use it.

**Linux**
---

- Make sure you have python lang installed in your machine

Then probably you will need the chromedriver installed, to do this:

- Check your current version for Google Chrome and based on that you can
  download `chromedriver` [here](https://chromedriver.chromium.org/downloads)
- Install `chromedriver` (if you need [help](https://skolo.online/documents/webscrapping/#step-2-install-chromedriver))
- Go to the project root and run `pip3 install -r requirements.txt`
- Go to the project root and run `pytest` or `pytest PATH_TO_FILE_TEST.py`

**Windows**
---
<h3>WARNING You will need to run IntelliJ and the Shell as an Administrator</h3>
Install chocolatey from here: https://chocolatey.org/install
<b>Be sure to run the installation and the following as an Administrator
</b>

-Run `choco install nodejs`

-Run `choco install chromedriver`

-Run `choco install selenium-gecko-driver`

-Run `choco install python`

-Run `pip --version` - if you get a version back, please run `python -m pip install -U pip`; If you DO NOT get a pip
version response, To manually install pip on Windows, you will need a copy of get-pip.py. For older Python versions, you
may need to use the appropriate version of the file from pypa.org. Download the file to a folder on your computer, or
use the curl command:
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
Next, run the following command to install pip:
python get-pip.py
If the file is not found, you may need to first navigate to the directory containing the get-pip.py file.

<h3> Adding PIP To Windows Environment Variables</h3>
One of the most common problems with running Python tools like pip is the “not on PATH” error. This means that Python cannot find the tool you’re trying to run in your current directory. In most cases, you’ll need to navigate to the directory in which the tool is installed before you can run the command to launch it.

If you’d rather run pip (or other tools) from any location, you’ll need to add the directory in which it’s installed as
a PATH environment variable by doing the following:

Open up the Control Panel and navigate to System and Security > System
Click on the Advanced system settings link on the left panel
Click Environment Variables.
Under System Variables, double-click the variable PATH.
Click New, and add the directory where pip is installed, e.g. `C:\Python310\Scripts`, and select OK.

**Everyone**
---

***Project setup***
---

1. In intelliJ welcome screen, select Project from VCS
2. Add your GitHub account and authorize with the access token mentioned above
3. Clone this project
4. Install The Python Community Edition Plugin for
   IntelliJ https://plugins.jetbrains.com/plugin/7322-python-community-edition
5. Install the Requirements Plugin for Intellij https://plugins.jetbrains.com/plugin/10837-requirements
6. Go to File > Project Structure > Project and assign the Python SDK to the SDK field
7. Click Apply and Save. Verify that the python SDK can be seen in the Platform Settings SDK section as well.

***Running Tests***
---
-I built this project to be able to run using pytest runners https://docs.pytest.org
-You can run tests by
inputting `pytest --environment="{test, stage, dev}" --browser="{firefox, chrome, edge}" -s tests/{your directory path} --html=test-reports/runreport.html`
into the command
line or, Using IntelliJ's pytest runner, you can run tests. Find the runner under /tests.

-Note that the test runner is configured to run using the Python interpreter of the project, so you will need to define
your python interpreter for your project, or change the runner to refer to another interpreter.

-You must define an *environment* variable when running like `--environment='dev' or --environment='stage'`

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

***Troubleshooting***
---
Selenium Failures like ```selenium.common.exceptions.SessionNotCreatedException: Message: session not created:
This version of ChromeDriver only supports Chrome version 103
Current browser version is 102.0.5005.115 with binary path C:\Users\AlyshaKester-Terry\AppData\Local\Google\Chrome\Application\chrome.exe```
Means you either need to update the chromedriver or your installed version of chrome
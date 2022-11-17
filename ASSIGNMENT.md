SDET CODE EXERCISE
======================

This should be a non-complex exercise. We don't want you to spend more than 4 hours on the project -- but it's up to you
how much time you take. We will need your example project, shared via GitHub, before your next interview.
You don't have to complete all 3 steps, but I would expect that this shouldn't take more than 4 hours total to complete the entire exercise.

GETTING STARTED
---------------
IMPORTANT: Start by following all the steps in the README https://github.com/alyshakt/web-ui-test-framework-py/blob/main/README.md 
Find the starter repo at <https://github.com/alyshakt/web-ui-test-framework-py> 
Clone the project through IntelliJ's VCS function. 
!!!Be sure to look through the README to set up the project appropriately.!!!

PROJECT REQUEST
---------------

STEP 1:
-----
I'd like to see a new App enum added to this repository to test Mindful Care. Mindful Care has two environments:
1. Stage = <https://app-40572.on-aptible.com/>
2. Prod = <https://mindful.care>

INFO:
*App enum:* `env_setup/App.py`
*App Setup:* `env_setup/AppSetup.py` to define the URL for different environment types
*Test location*: `tests/web_ui` (You could literally copy-paste the test that exists at `tests/web_ui/google_search_example/test_search.py` and make edits to the App type, page objects, etc.

STEP 2:
-----
I'd like to see new page objects for methods and locators for Mindful Care and the FAQ page.

INFO:
*Page Objects*: `web_page_objects` create new page objects for Mindful Care. Inherit the `BasePage` class `BasePage(object)` to take advantage of common items like clicking an element or entering text. The Locators page can inherit the `BaseLocators` class `BasePageLocators(BaseLocators)` to enable easy use of the BaseLocators library (found at `web_page_objects/LocatorsUtil.py`)

STEP 3:
-----
Implement the `App.mindful` enum and the new pageobjects in your test, and cover the following:

We want to find out if anything is not right in the FAQs page at `/frequently-asked-questions`

(These are hypothetical acceptance criteria, but should be asserted):

1. We want to make sure that there is a section called "What medications do you prescribe?"
2. In that section, we want to make sure that we say "We do not prescribe any controlled substances"
3. There should be a FAQ that describes that cancelation within 24 hours of the appointment or a no-show results in a
   $25 fee.

   
PROJECT DELIVERABLES
--------------------

A Pull Request at <https://github.com/alyshakt/web-ui-test-framework-py> that has the following:

1. New *App* for Mindful Care

2. Mindful Care page objects

3. Test(s) in the tests/ directory that validates the acceptance criteria

4. Test output in the test-reports directory

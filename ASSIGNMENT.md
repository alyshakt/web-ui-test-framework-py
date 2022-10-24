SDET CODE EXERCISE
======================

This should be a non-complex exercise. We don't want you to spend more than 4 hours on the project -- but it's up to you
how much time you take. We will need your example project, shared via GitHub, before your next interview.

GETTING STARTED
---------------

Find the starter repo at <https://github.com/alyshakt/web-ui-test-framework-py> and clone the project through IntelliJ's
VCS function. Be sure to look through the README to set up the project appropriately.

PROJECT REQUEST
---------------

I'd like to see a new App added to this repository to test Mindful Care. Mindful Care has two environments:

1. Stage = <https://app-40572.on-aptible.com/>

2. Prod = <https://mindful.care>

We haven't looked through all our FAQs for quite some time, so we want to be able to retrieve all the FAQ text in the
webpage and report it back in a readable format that our clinical team can look at to let us know what needs to be
corrected. This can be in any readable format -- from test output that can be copied/pasted to a CSV -- whatever
solution you would like to provide.

We also need to know if anything is not right, such as prices or medication names listed in the FAQs.

(These are hypothetical acceptance criteria, but should be asserted):

1. We only serve patients aged 18 and older for any service

2. We serve patients both virtually and in person at any of our locations

3. Existing patients need to call us at (516) 505-7201 or email support@mindful.care to schedule an appointment.

4. There should be a FAQ that describes that cancelation within 24 hours of the appointment or a no-show results in a
   $25 fee.

PROJECT DELIVERABLES
--------------------

A Pull Request at <https://github.com/alyshakt/web-ui-test-framework-py> that has the following:

1. New *App* for Mindful Care

2. Mindful Care page objects

3. Test(s) in the tests/ directory that validates the acceptance criteria

4. Test output in the test-reports directory

5. Some kind of human-readable output for all the FAQs sections and their text so that we can review all the answers
   shown on the website
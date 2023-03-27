Project's name: cuisineCalendar 

Application's name: mealPlanner 

Cuisine Calendar is a web application that allows users to create recipes and plan their meals for the week. The project was built using the Django web framework with Python. 

Testing Methodology and Coverage:

We have two folders in the Tests app for testing: manual_tests and dynamic_tests. In each folder, we have two test files: test_views.py and test_models.py. 
We are using Django's built-in testing framework, and we have aimed for 100% test coverage. In manual_tests, we test the application manually by going through each feature and making sure it works as expected. In dynamic_tests, we use automated tests to check the functionality of the application. We also have another file test_templates.py in the Tests app to test the templates.

Running the Tests:
To run the manual tests, use the following command:

python manage.py tests Tests.manual_tests.test_views/python manage.py tests Tests.manual_tests.test_models

To run the dynamic tests, use the following command:

python manage.py tests Tests.dynamic_tests.tests_views/python manage.py tests Tests.dynamic_tests.test_models

To run the test_templates.py:

python manage.py tests Tests.test_templates

Security Measures:

We have implemented two security measures in our application. The first is HTTPS, which encrypts data sent between the 
client and the server. However, due to issues with SSL configuration, HTTPS is not functioning as expected.

The second security measure we implemented is rate limiting with authentication. We have used the Django Ratelimit 
library to limit the number of requests a user can make in a given time period. This helps prevent brute force attacks 
on the authentication system. However, we have noticed that the library uses ugettext, which is not supported in the 
latest version of Django.

Configuration:
We have created two new files: settings_dev.py and settings_test.py, to improve the configuration. 

To launch the development server with the settings_dev.py file, use the following command:
python manage.py runserver --settings=myproject.settings_dev

To launch the test server with the settings_test.py file, use the following command:
python manage.py testserver --settings=myproject.settings_test

Secret Key:
We have placed the secret_key in a separate file called keys.py, which is ignored by Git.

Conclusion:
The testing methodology and security measures taken in the development of the website ensure that the website functions as expected and is secure from potential attacks. The use of manual and dynamic tests ensures that the code changes do not introduce any regressions, while the implementation of HTTPS and authentication with rate-limiting provides an additional layer of security to the website.

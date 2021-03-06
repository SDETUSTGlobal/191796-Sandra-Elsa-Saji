Feature: Data table
Verify that the new user registration is successful after passing correct inputs.
Scenario:
Given the user on the user registration page.
When user enter invalid data on the page
| Fields                 | Values              |
| First Name             | Sandra		           |
| Last Name              | Saji		             |
| Email Address          | someone@gmail.com   |
| Re-enter Email Address | someone@gmail.com   |
| Password               |PASSWORD             |
| Birthdate              | 08                  |
Then the user registration should be successful.
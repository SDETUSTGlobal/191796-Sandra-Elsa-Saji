Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM home Page
    Given launch chrome browser1
    When open orange hrm homepage1
    And enter username "admin" and password "admin123"
    And click on login button
    Then user must successfully login to Dashboard

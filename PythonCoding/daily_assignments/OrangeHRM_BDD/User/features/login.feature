Feature: Login Functionality

  Scenario: Valid Login

    Given user launches OrangeHRM application

    When user enters username "Admin" and password "admin123"

    And user clicks login button

    Then user should navigate to dashboard page
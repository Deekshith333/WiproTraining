Feature: Login Functionality

  Background:
    Given User launches OrangeHRM application
    And User is on login page

  Scenario: Successful login
    When User enters username "Admin"
    And User enters password "admin123"
    And User clicks login button
    Then User should navigate to dashboard

  Scenario: Invalid login
    When User enters username "Admin"
    And User enters password "wrong123"
    And User clicks login button
    Then User should see invalid credentials message
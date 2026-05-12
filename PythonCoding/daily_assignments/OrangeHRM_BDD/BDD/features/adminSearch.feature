
Feature: Admin User Search

  Scenario: Search users using multiple filters

    Given User launches OrangeHRM application

    And User logs in with valid credentials

    When User navigates to Admin module

    And User searches users with following details
      | Username | Admin   |
      | UserRole | Admin   |
      | Status   | Enabled |

    Then Matching users should be displayed
Feature: Admin Search

  Scenario: Search User

    Given admin is logged into OrangeHRM

    When I enter the following search criteria:
      | Username  | Admin   |
      | User Role | Admin   |
      | Status    | Enabled |

    Then matching records should be displayed
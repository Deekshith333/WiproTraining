Feature: Employee Creation

  Scenario Outline: Add Employee

    Given user is logged into OrangeHRM

    When I enter "<FirstName>" and "<LastName>"

    And user clicks save button

    Then employee should be created successfully

    Examples:
      | FirstName | LastName |
      | John      | Cena     |
      | Ram       | Kumar    |
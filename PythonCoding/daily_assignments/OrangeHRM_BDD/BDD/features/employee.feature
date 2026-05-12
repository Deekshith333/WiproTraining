Feature: Employee Management

  Scenario Outline: Add multiple employees

    Given User launches OrangeHRM application
    And User logs in with valid credentials

    When User navigates to PIM module
    And User clicks Add Employee

    And User enters first name "<FirstName>"
    And User enters last name "<LastName>"

    And User clicks Save button

    Then Employee should be added successfully

    Examples:
      | FirstName | LastName |
      | Rahul     | Sharma   |
      | Sneha     | Reddy    |
      | Arjun     | Kumar    |
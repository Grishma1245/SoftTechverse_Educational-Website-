Feature: Student Management Navigation
  As a logged-in admin
  I want to interact with the Student Details menu
  So that I can access student management features

  @smoke @student
  Scenario: Expand Student Details menu in sidebar
    Given I am logged in as a valid user
    When I click the Student Details menu
    Then the Student List option should be visible


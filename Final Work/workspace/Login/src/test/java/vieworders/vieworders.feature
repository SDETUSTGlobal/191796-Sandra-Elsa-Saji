Feature: View all orders
Given the user on the view all orders page.
Scenario: Check all button 
When user clicks Check all button 
Then user should see all orders checked
Scenario: Uncheck all button 
When user clicks Uncheck all button 
Then user should see all orders unchecked.
Scenario: Check box checking and unchecking
When user clicks desired orders check box
Then user should see desired orders checked/unchecked.
Scenario: Delete selected button 
When user clicks Delete selected button 
Then user should see all selected orders unchecked.
Scenario: Edit
When user clicks Edit
Then navigate to edit page.

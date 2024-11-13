Feature: Product management

  Scenario: Reading a product by ID
    Given the following products exist in the system
      | name         | category     | price | availability |
      | Laptop       | Electronics  | 999   | available    |
    When I request to read the product with ID 1
    Then I should see the product with name "Laptop" and category "Electronics"

  Scenario: Updating a product
    Given the following product exists in the system
      | name         | category     | price | availability |
      | Smartphone   | Electronics  | 699   | available    |
    When I update the product with ID 1 to have the name "Smartphone Pro" and price 799
    Then I should see the updated product with name "Smartphone Pro" and price 799

  Scenario: Deleting a product
    Given the following product exists in the system
      | name         | category     | price | availability |
      | Coffee Maker | Appliances   | 99    | available    |
    When I request to delete the product with ID 2
    Then the product should be deleted from the system

  Scenario: Listing all products
    Given the following products exist in the system
      | name         | category     | price | availability |
      | Laptop       | Electronics  | 999   | available    |
      | Desk Chair   | Furniture    | 149   | unavailable  |
    When I request to list all products
    Then I should see a list of all products

  Scenario: Searching products by name
    Given the following products exist in the system
      | name         | category     | price | availability |
      | Laptop       | Electronics  | 999   | available    |
      | Smartphone   | Electronics  | 699   | available    |
    When I search for a product by name "Laptop"
    Then I should see the product with name "Laptop"

  Scenario: Searching products by category
    Given the following products exist in the system
      | name         | category     | price | availability |
      | Coffee Maker | Appliances   | 99    | available    |
      | Desk Chair   | Furniture    | 149   | unavailable  |
    When I search for products in the "Furniture" category
    Then I should see the product "Desk Chair"

  Scenario: Searching products by availability
    Given the following products exist in the system
      | name         | category     | price | availability |
      | Laptop       | Electronics  | 999   | available    |
      | Desk Chair   | Furniture    | 149   | unavailable  |
    When I search for products that are available
    Then I should see the product "Laptop"

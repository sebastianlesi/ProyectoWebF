Feature: Register Comment
In order to keep track of the comment I make,
As a user
I want to register a comment in the corresponding publication together with its details.

 Background: There is a registered user and publication
   Given Exists a user "user" with password "password"
   And Exists publication registered by "user"
      | titulo                     |
      | Movilidad en España        |

  Scenario: Register just comment name
    Given I login as user "user" with password "password"
    When I register comment at publication "Movilidad en España"
      | Comentario      |
      | bueno           |
    Then I'm viewing the details page for comment at publication "Movilidad en España" with comment "bueno"
      | Comentario      |
      | bueno           |
    And There are 1 comments
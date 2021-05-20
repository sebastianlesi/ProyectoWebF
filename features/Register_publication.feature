Feature: Register Publication
In order to keep track of the publications I make,
As a user
I want to register a publication together with its text and multimedia.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Register just publication
        Given I login as user "user" with password "password"
        When I register publication
            | titulo        | Descripcion    | Vistas    |
            | The Tavern    | ingenieria     | 0         |
        Then I'm viewing the details page for publication by "user"
            | titulo        | Descripcion    | Vistas    |
            | The Tavern    | ingenieria     | 0         |
        And There are 1 publications
Feature: Validate JSON
    I want to get response and validate JSON

    Scenario: Validate JSON
        Given a request url https://jsonplaceholder.typicode.com/users
        When the request sends GET
        Then the response status is 200
            And the response json matches
                """
                {
                    "id": "number",
                    "name": "string",
                    "username": "string",
                    "email": "string",
                    "address": {
                        "street": "string",
                        "suite": "string",
                        "city": "string",
                        "zip-code": "string",
                        "geo": {
                            "lat": "number",
                            "lng": "number"
                        }
                    },
                    "phone": "string",
                    "website": "string",
                    "company": {
                    "name": {"type": "string"},
                    "catchPhrase": {"type": "string"},
                    "bs": {"type": "string"}
                    }
                }
                """
            And the response json at $.[0].id is equal to 1
            And the response json at $.[0].name is equal to "Leanne Graham"
            And the response json at $.[0].username is equal to "Bret"
            And the response json at $.[-1].id is equal to 10

            #Some negative tests
            And the response json at $.[1] does not contain 'negative'
            And the response json at $.[3].phone is not equal to '88844422'
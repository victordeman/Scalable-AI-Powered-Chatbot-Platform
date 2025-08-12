# API Documentation

## REST API
- **Endpoint**: `/api/chat`
  - Method: POST
  - Request: `{"message": "string"}`
  - Response: `{"response": "string"}`
  - Authentication: Bearer token

## GraphQL API
- **Endpoint**: `/graphql`
  - Query example:
    ```graphql
    query {
      chat(message: "Hello") {
        response
      }
    }
    ```

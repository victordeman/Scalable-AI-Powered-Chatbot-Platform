from fastapi import FastAPI
from src.api.rest import router as rest_router
from src.api.graphql import schema
from strawberry.fastapi import GraphQLRouter

app = FastAPI(title="Scalable AI-Powered Chatbot Platform")

# Include REST API routes
app.include_router(rest_router, prefix="/api")

# Include GraphQL API
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

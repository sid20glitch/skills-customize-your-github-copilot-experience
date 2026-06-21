# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create a fully functional API with endpoints, request validation, and documentation that students can interact with using HTTP requests.

## 📝 Tasks

### 🛠️ Create a Basic API with FastAPI

#### Description
Set up a FastAPI application with multiple endpoints that handle different HTTP methods (GET, POST, PUT, DELETE). Create routes for managing a collection of items with basic CRUD operations.

#### Requirements
Completed API should:

- Initialize a FastAPI application with a main entrypoint
- Create at least 4 endpoints (GET all items, GET single item, POST/create item, DELETE item)
- Use path parameters and query parameters appropriately
- Return JSON responses with proper HTTP status codes
- Include at least one POST endpoint that accepts a request body with validation

### 🛠️ Add Request Validation and Data Models

#### Description
Implement Pydantic models to validate incoming requests and define the structure of your API responses. Ensure all data is validated before processing.

#### Requirements
Completed API should:

- Define Pydantic models for request and response data
- Use these models in endpoint function signatures for automatic validation
- Return meaningful error messages for invalid requests
- Document expected data formats in model docstrings
- Handle validation errors gracefully with appropriate HTTP status codes

### 🛠️ Test and Document Your API

#### Description
Test your API endpoints using tools like curl or a Python requests script. Use FastAPI's built-in Swagger documentation to explore and verify your API works correctly.

#### Requirements
Completed API should:

- All endpoints respond with correct status codes and data formats
- Swagger UI documentation is accessible at /docs and displays all endpoints
- Include docstrings on each endpoint function explaining what it does
- Test at least one POST request that validates the request body
- Demonstrate that the API correctly rejects invalid requests

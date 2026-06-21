"""
Building REST APIs with FastAPI
================================

Create a REST API using FastAPI that manages a collection of items.
This starter code provides the basic structure to get you started.

Learn about:
- FastAPI application setup
- Route handlers and HTTP methods
- Path and query parameters
- Request body validation with Pydantic
- JSON responses and HTTP status codes
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(
    title="Item Management API",
    description="A REST API for managing items",
    version="1.0.0"
)

# ============================================================================
# Data Models - Define the structure of items in your API
# ============================================================================

class Item(BaseModel):
    """
    Represents an item in the system.
    
    Attributes:
        id: Unique identifier for the item
        name: Name of the item
        description: Detailed description of the item
        price: Price of the item in dollars
    """
    id: int
    name: str
    description: Optional[str] = None
    price: float


class ItemCreate(BaseModel):
    """
    Data model for creating a new item.
    Used for request body validation.
    """
    name: str
    description: Optional[str] = None
    price: float


# ============================================================================
# In-Memory Data Storage
# ============================================================================

# TODO: In production, this would be a database
# For this assignment, we'll use a simple dictionary to store items
items_db: dict = {
    1: Item(id=1, name="Laptop", description="High-performance laptop", price=999.99),
    2: Item(id=2, name="Mouse", description="Wireless mouse", price=29.99),
    3: Item(id=3, name="Keyboard", description="Mechanical keyboard", price=79.99),
}

next_item_id = 4


# ============================================================================
# API Endpoints - TODO: Complete these endpoints
# ============================================================================

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint - returns a welcome message.
    """
    return {"message": "Welcome to the Item Management API!"}


@app.get("/items/", response_model=List[Item], tags=["Items"])
def get_all_items():
    """
    Retrieve all items from the system.
    
    Returns:
        List of all Item objects
    """
    # TODO: Implement this endpoint
    # Should return a list of all items from items_db
    pass


@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: int):
    """
    Retrieve a single item by ID.
    
    Args:
        item_id: The ID of the item to retrieve
        
    Returns:
        The requested Item object
        
    Raises:
        HTTPException: If item not found (status 404)
    """
    # TODO: Implement this endpoint
    # Should retrieve an item by ID from items_db
    # Raise HTTPException with status_code=404 if not found
    pass


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(item: ItemCreate):
    """
    Create a new item in the system.
    
    Args:
        item: The item data to create (ItemCreate model validates the input)
        
    Returns:
        The created Item object with assigned ID
    """
    # TODO: Implement this endpoint
    # Should create a new item, assign it an ID, store it, and return it
    # Remember to increment next_item_id for the next item
    pass


@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
def update_item(item_id: int, item: ItemCreate):
    """
    Update an existing item.
    
    Args:
        item_id: The ID of the item to update
        item: The new item data
        
    Returns:
        The updated Item object
        
    Raises:
        HTTPException: If item not found (status 404)
    """
    # TODO: Implement this endpoint
    # Should update an existing item by ID
    # Raise HTTPException with status_code=404 if not found
    pass


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int):
    """
    Delete an item from the system.
    
    Args:
        item_id: The ID of the item to delete
        
    Raises:
        HTTPException: If item not found (status 404)
    """
    # TODO: Implement this endpoint
    # Should delete an item by ID
    # Raise HTTPException with status_code=404 if not found
    pass


# ============================================================================
# Running the Application
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    # Run the API locally
    # Access the API at http://localhost:8000
    # View automatic documentation at http://localhost:8000/docs
    uvicorn.run(app, host="0.0.0.0", port=8000)

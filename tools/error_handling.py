"""
Error handling utilities for MCP tool functions.

This module provides utilities to convert Pydantic ValidationError exceptions
into MCP-compatible error responses.
"""

from functools import wraps
from typing import Callable, Any, Dict
from pydantic import ValidationError


def handle_validation_errors(func: Callable) -> Callable:
    """
    Decorator that catches Pydantic ValidationError and converts it to MCP error response.
    
    This decorator wraps tool functions to automatically handle parameter validation
    errors. When a ValidationError is raised (typically during Pydantic model
    construction), it converts the error into a structured MCP error response.
    
    Args:
        func: The tool function to wrap
        
    Returns:
        Wrapped function that handles ValidationError
        
    Error Response Format:
        {
            "error": "Parameter validation failed",
            "validation_errors": [
                {
                    "parameter": str,  # Parameter name
                    "value": Any,      # Provided value
                    "constraint": str, # Constraint type (e.g., "greater_than")
                    "message": str     # Human-readable error message
                }
            ],
            "success": False
        }
    
    Requirements:
        - 7.2: Parameter validation fails with descriptive error messages
        - 9.6: Validation errors include parameter name, value, and constraint
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Dict[str, Any]:
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            # Convert Pydantic ValidationError to MCP error response
            errors = e.errors()
            
            validation_errors = []
            for err in errors:
                # Extract parameter name from location tuple
                param_name = str(err["loc"][0]) if err["loc"] else "unknown"
                
                validation_errors.append({
                    "parameter": param_name,
                    "value": err.get("input"),
                    "constraint": err["type"],
                    "message": err["msg"]
                })
            
            return {
                "error": "Parameter validation failed",
                "validation_errors": validation_errors,
                "success": False
            }
    
    return wrapper


def format_validation_error(e: ValidationError) -> Dict[str, Any]:
    """
    Convert a Pydantic ValidationError to an MCP error response.
    
    This is a utility function that can be used directly in try-except blocks
    if the decorator approach is not suitable.
    
    Args:
        e: The ValidationError exception
        
    Returns:
        MCP error response dictionary
        
    Requirements:
        - 7.2: Parameter validation fails with descriptive error messages
        - 9.6: Validation errors include parameter name, value, and constraint
    """
    errors = e.errors()
    
    validation_errors = []
    for err in errors:
        # Extract parameter name from location tuple
        param_name = str(err["loc"][0]) if err["loc"] else "unknown"
        
        validation_errors.append({
            "parameter": param_name,
            "value": err.get("input"),
            "constraint": err["type"],
            "message": err["msg"]
        })
    
    return {
        "error": "Parameter validation failed",
        "validation_errors": validation_errors,
        "success": False
    }

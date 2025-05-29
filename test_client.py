#!/usr/bin/env python3
"""
Test client for the Bark MCP server.
This script simulates an MCP client calling the notify tool.
"""
import os
import sys
import json
import subprocess
import tempfile
from dotenv import load_dotenv

def main():
    """Run a test of the Bark MCP server."""
    # Load environment variables
    load_dotenv()
    
    # Check if environment variables are set
    if not os.environ.get("BARK_SERVER_URL") or not os.environ.get("BARK_API_KEY"):
        print("Error: BARK_SERVER_URL and BARK_API_KEY environment variables must be set.")
        print("Create a .env file or set them in your environment.")
        sys.exit(1)
    
    # Create a temporary file for the request
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
        # Create a sample request to the notify tool
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "mcp/tools/call",
            "params": {
                "name": "notify",
                "arguments": {
                    "title": "Test Notification",
                    "content": "This is a test notification from the Bark MCP test client.",
                    "url": "https://example.com"
                }
            }
        }
        
        # Write the request to the temporary file
        json.dump(request, temp)
        temp_path = temp.name
    
    try:
        # Start the Bark MCP server as a subprocess
        server_process = subprocess.Popen(
            ["python", "-m", "bark_mcp.cli"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Send the request to the server
        with open(temp_path, 'r') as f:
            request_str = f.read()
            server_process.stdin.write(request_str + "\n")
            server_process.stdin.flush()
        
        # Read the response from the server
        response_line = server_process.stdout.readline()
        
        try:
            response = json.loads(response_line)
            print("Response from server:")
            print(json.dumps(response, indent=2))
            
            if "result" in response and response.get("id") == 1:
                print("\nNotification sent successfully!")
            else:
                print("\nError sending notification.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON response from server.")
            print(f"Raw response: {response_line}")
    
    finally:
        # Clean up
        if 'server_process' in locals():
            server_process.terminate()
        
        # Remove the temporary file
        if os.path.exists(temp_path):
            os.unlink(temp_path)

if __name__ == "__main__":
    main()

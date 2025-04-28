from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


"""
Standard Input/Output (stdio)
The stdio transport enables communication through standard input and output streams. 
This is particularly useful for local integrations and command-line tools.

Use stdio when:

Building command-line tools
Implementing local integrations
Needing simple process communication
Working with shell scripts
"""
if __name__ == "__main__":
    mcp.run(transport="stdio")


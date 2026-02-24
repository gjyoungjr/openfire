from fastmcp import FastMCP

# Create MCP Server (no host/port = stdio transport for Cursor)
mcp = FastMCP("openfire-mcp")


@mcp.tool()
def count_total_rs(txt: str) -> int:
    """Count the total number of Rs in a given string

    Input: 
        txt: str -> The string to count the Rs in
    Output:
        count:int -> The total number of Rs in the string
    """
    return txt.lower().count('r')


if __name__ == "__main__":
    mcp.run()

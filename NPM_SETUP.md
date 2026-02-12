# NPM Build and Execution Setup

This document explains the npm build system for the USS Blackwell MCP Server.

## Files Created

### 1. `package.json`
The npm package configuration file that defines:
- Package metadata (name, version, description)
- Binary entry point (`uss-blackwell-mcp-server` command)
- Build and test scripts
- Dependencies and requirements
- Files to include in npm distribution

### 2. `build.js`
Build script that creates a Node.js wrapper for the Python server:
- Creates `build/index.js` wrapper script
- Handles Python environment detection
- Provides clean npm/npx execution interface

### 3. `.npmignore`
Specifies files to exclude from npm package distribution:
- Test files and coverage reports
- Development files (.kiro/, build.js)
- IDE and OS-specific files

### 4. `build/index.js` (generated)
Node.js wrapper that:
- Detects available Python command (python3, python, or py)
- Launches server.py with proper environment
- Handles process signals and termination

## Usage

### For End Users

**Install globally:**
```bash
npm install -g uss-blackwell-mcp-server
uss-blackwell-mcp-server
```

**Run with npx (no installation):**
```bash
npx uss-blackwell-mcp-server
```

**Use in Claude Desktop config:**
```json
{
  "mcpServers": {
    "uss-blackwell": {
      "command": "npx",
      "args": ["uss-blackwell-mcp-server"]
    }
  }
}
```

### For Developers

**Build the package:**
```bash
npm install
npm run build
```

**Test locally:**
```bash
node build/index.js
```

**Run tests:**
```bash
npm test                    # Run all tests
npm run test:coverage       # Generate coverage report
npm run test:properties     # Run property-based tests with statistics
```

## Publishing to npm

1. **Build the package:**
   ```bash
   npm run build
   ```

2. **Test the package locally:**
   ```bash
   npm pack
   npm install -g uss-blackwell-mcp-server-1.0.0.tgz
   uss-blackwell-mcp-server
   ```

3. **Publish to npm:**
   ```bash
   npm login
   npm publish
   ```

## Requirements

### Runtime Requirements
- Python 3.10 or higher
- Python packages: mcp-use, hypothesis, pytest (installed via pip)

### Build Requirements
- Node.js 16.0 or higher
- npm (comes with Node.js)

## How It Works

1. User runs `npx uss-blackwell-mcp-server`
2. npm downloads and caches the package
3. npm executes `build/index.js`
4. The wrapper detects Python and runs `server.py`
5. The MCP server starts and communicates via stdio

## Benefits

- **Easy Installation**: Users can install with `npm install` or run with `npx`
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Standard Distribution**: Follows MCP server conventions
- **No Manual Setup**: Automatically handles Python detection
- **Version Management**: npm handles versioning and updates

## Troubleshooting

**"Python not found" error:**
- Install Python 3.10+ from https://python.org/downloads/
- Ensure Python is in your system PATH

**"Module not found" error:**
- Install Python dependencies: `pip install -r requirements.txt`

**Build fails:**
- Ensure Node.js 16+ is installed
- Run `npm install` to install build dependencies

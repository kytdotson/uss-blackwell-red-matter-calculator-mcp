#!/usr/bin/env node

/**
 * Build script for USS Blackwell MCP Server
 * 
 * This script creates a Node.js wrapper that launches the Python MCP server.
 * The wrapper handles Python environment detection and provides a clean
 * execution interface for npm/npx users.
 */

import { writeFileSync, mkdirSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Create build directory if it doesn't exist
const buildDir = join(__dirname, 'build');
if (!existsSync(buildDir)) {
  mkdirSync(buildDir, { recursive: true });
}

// Create the Node.js wrapper script
const wrapperScript = `#!/usr/bin/env node

/**
 * USS Blackwell MCP Server - Node.js Wrapper
 * 
 * This wrapper launches the Python MCP server with proper environment detection.
 */

import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Detect Python command (python3, python, or py)
function getPythonCommand() {
  const commands = ['python3', 'python', 'py'];
  
  for (const cmd of commands) {
    try {
      const result = spawn(cmd, ['--version'], { stdio: 'pipe' });
      return cmd;
    } catch (e) {
      continue;
    }
  }
  
  console.error('Error: Python 3.10 or higher is required but not found.');
  console.error('Please install Python from https://www.python.org/downloads/');
  process.exit(1);
}

// Get the path to server.py (one directory up from build/)
const serverPath = join(__dirname, '..', 'server.py');

// Launch the Python MCP server
const pythonCmd = getPythonCommand();
const serverProcess = spawn(pythonCmd, [serverPath], {
  stdio: 'inherit',
  env: {
    ...process.env,
    PYTHONUNBUFFERED: '1'
  }
});

// Handle process termination
serverProcess.on('exit', (code) => {
  process.exit(code || 0);
});

// Handle signals
process.on('SIGINT', () => {
  serverProcess.kill('SIGINT');
});

process.on('SIGTERM', () => {
  serverProcess.kill('SIGTERM');
});
`;

// Write the wrapper script
const indexPath = join(buildDir, 'index.js');
writeFileSync(indexPath, wrapperScript, { mode: 0o755 });

console.log('✓ Build completed successfully');
console.log(\`  Created: \${indexPath}\`);

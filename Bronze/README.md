# Personal AI Employee - Bronze Tier

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Workflow](#workflow)
- [Components](#components)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

## Overview

This project implements a Personal AI Employee at the Bronze Tier level as part of the Agent Factory hackathon. The AI Employee operates as a digital full-time equivalent (FTE), automating personal and business affairs using Claude Code as the executor and Obsidian as the management dashboard.

The system follows a local-first approach with privacy-focused architecture, where an AI agent proactively manages tasks using file-based triggers and responses. The solution combines the power of AI reasoning with a robust file system to create an autonomous employee capable of processing tasks 24/7.

## Architecture

The system follows a three-tier architecture:

### The Brain: Claude Code
Acts as the reasoning engine that processes tasks and makes decisions based on the company handbook and skill definitions.

### The Memory/GUI: Obsidian
Uses local Markdown files as the dashboard, keeping all data local and accessible. The vault structure organizes tasks and information.

### The Senses (Watchers): Python Scripts
Lightweight Python scripts monitor the file system to trigger the AI when new tasks arrive.

## Features

### Core Functionality
- **File System Monitoring**: Continuously watches the Inbox folder for new markdown files
- **Content Reading**: Reads and processes content from incoming files with retry logic
- **Response Generation**: Creates detailed response files in the Needs_Action folder
- **Automatic File Movement**: Moves processed files from Inbox to Done folder
- **Content Preservation**: Maintains original content in response files for reference

### Enhanced Capabilities
- **Retry Logic**: Implements multiple attempts to read files to handle race conditions
- **Error Handling**: Comprehensive error handling for file operations
- **Debugging Support**: Detailed logging for troubleshooting
- **Robust File Operations**: Safe file movement to prevent data loss

### Workflow Management
- **Inbox**: Receives new tasks and requests
- **Needs_Action**: Contains processed tasks requiring human attention
- **Done**: Stores completed tasks for reference

## Installation

### Prerequisites
- Python 3.13 or higher
- Node.js v24+ LTS
- Claude Code (Pro subscription or free Gemini API with Claude Code Router)
- Obsidian v1.10.6+

### Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/1hmed1/Hackathon0.git
   ```

2. Navigate to the Bronze folder:
   ```
   cd Hackathon0/Bronze
   ```

3. Install required Python packages:
   ```
   pip install watchdog
   ```

4. Ensure your vault structure is properly set up with:
   - `vault/Inbox/`
   - `vault/Needs_Action/`
   - `vault/Done/`

## Usage

### Starting the AI Employee
1. Open a terminal in the Bronze folder
2. Run the watcher script:
   ```
   python watcher.py
   ```
3. The system will start monitoring the vault/Inbox folder

### Adding New Tasks
1. Place new markdown (.md) files in the `vault/Inbox/` folder
2. The AI Employee will automatically detect and process them
3. Responses will appear in the `vault/Needs_Action/` folder
4. Original files will be moved to the `vault/Done/` folder

### Example Task Format
```markdown
# Task Title

Brief description of the task.

## Details
- Specific requirements
- Important information
- Action items needed
```

## File Structure

```
Bronze/
├── watcher.py                 # Main file system watcher
├── vault_structure.py         # Initial vault setup script
├── vault/                     # Obsidian vault directory
│   ├── Inbox/                 # New tasks arrive here
│   ├── Needs_Action/          # Processed tasks requiring action
│   ├── Done/                  # Completed tasks
│   ├── Dashboard.md           # Overall status dashboard
│   └── Company_Handbook.md    # Rules and guidelines
├── skills/                    # AI skill definitions
│   └── file-triage/           # File processing skills
│       └── SKILL.md           # Detailed processing instructions
└── README.md                  # This file
```

## Workflow

### 1. Task Arrival
- New markdown files are placed in the `vault/Inbox/` folder
- The file system watcher detects the new file immediately

### 2. Content Processing
- The watcher reads the content with retry logic to handle race conditions
- Original content is preserved and included in the response
- A summary is generated based on the content

### 3. Response Generation
- A response file is created in the `vault/Needs_Action/` folder
- The response includes the original content for reference
- Action items are suggested based on the task

### 4. File Organization
- The original file is moved from `Inbox/` to `Done/` folder
- This prevents duplicate processing of the same task
- The `Done/` folder serves as an archive of completed tasks

### 5. Human Review
- Review the response in `Needs_Action/` folder
- Take necessary actions based on the suggestions
- Move completed tasks to appropriate locations

## Components

### watcher.py
The core component that monitors the file system and processes tasks. Features include:
- File system event detection using watchdog
- Content reading with retry logic
- Response generation with proper formatting
- Automatic file movement between folders
- Comprehensive error handling

### Vault Structure
The organized file system that serves as the AI's memory:
- **Inbox**: Incoming tasks and requests
- **Needs_Action**: Processed items requiring attention
- **Done**: Completed tasks for reference
- **Dashboard.md**: High-level status information
- **Company_Handbook.md**: Rules and operational guidelines

### SKILL.md
Contains procedural knowledge for the AI employee:
- Step-by-step instructions for task processing
- Decision-making criteria for categorization
- Output formatting guidelines
- Quality assurance procedures

## Security

### Data Privacy
- All data remains local on your machine
- No external data transmission during normal operation
- File-based system ensures data control

### Credential Management
- No credentials stored in the vault
- External API connections handled separately
- Environment variables recommended for sensitive data

### Access Control
- Standard file system permissions apply
- No network exposure in basic configuration
- Local-only operation by design

## Troubleshooting

### Common Issues

#### Watcher Not Detecting Files
- Ensure the watcher script is running
- Verify file extensions are .md
- Check that files are being created in the correct Inbox folder

#### Empty Content in Responses
- This usually indicates a race condition
- The retry logic should handle this automatically
- If persistent, check file permissions

#### Files Not Moving to Done
- Verify the Done folder exists
- Check file permissions for move operations
- Ensure no other processes are locking the files

### Debugging Tips
- Enable verbose logging in the watcher for detailed output
- Check file permissions in all vault folders
- Verify the Python environment has required packages

## Future Enhancements

### Silver Tier Features
- Multiple watcher types (Gmail, WhatsApp, etc.)
- MCP server integration for external actions
- Human-in-the-loop approval workflows
- Automated scheduling capabilities

### Gold Tier Features
- Cross-domain integration
- Advanced error recovery
- Comprehensive audit logging
- Multi-step task completion loops

### Platinum Tier Features
- Cloud deployment options
- 24/7 operation capabilities
- Advanced synchronization protocols
- Production-grade monitoring

## Contributing

Contributions to improve the AI Employee are welcome. Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is part of the Agent Factory hackathon and follows the educational license guidelines provided for the hackathon.

## Acknowledgments

- Claude Code for the reasoning engine capabilities
- Obsidian for the knowledge management platform
- The Agent Factory community for inspiration and guidance

## Repository

For the latest updates and source code, visit: https://github.com/1hmed1/Hackathon0/tree/main/Bronze

---

*This AI Employee represents the Bronze Tier implementation of a digital FTE, demonstrating local-first, privacy-focused automation for personal and business tasks.*
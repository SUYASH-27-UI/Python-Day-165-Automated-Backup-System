# Python-Day-165-Automated-Backup-System
# Python Day 165 – Automated Backup & Restore Utility

## Project Description
A Python-based backup utility that creates compressed ZIP backups of folders and allows users to restore previously created backups.

## Features
- Create ZIP backups of folders.
- Automatically generate timestamped filenames.
- View available backups.
- Restore selected backups.
- Preserve folder and subfolder structure.
- Validate backup and destination paths.

## Technologies Used
- Python
- ZIP File Handling
- OS Module
- DateTime Module

## File Structure
- `backup_manager.py` – Main application.
- `backups/` – Automatically generated backup files.

## How to Run
1. Install Python.
2. Run `python backup_manager.py`.
3. Select an operation from the menu.
4. Enter the required folder paths.

## Learning Outcomes
Learned folder traversal, ZIP compression, file restoration, timestamp generation, and path validation.

## Safety Note
Test restoration with sample folders first. Restoring into a folder with existing files may overwrite files with matching names. Keep important original data safe.

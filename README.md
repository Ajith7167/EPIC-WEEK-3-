# Employee Management System

## Overview

A Python-based Employee Management System demonstrating CRUD
operations, configuration management, environment variables,
dependency management, and application logging.

## Features

- Create employees
- Search employees
- Update employee details
- Delete employees
- JSON-based data storage
- Environment-specific configuration
- Python logging and exception tracking

## Setup

Create a virtual environment:

    python -m venv venv

Activate on Windows PowerShell:

    .\venv\Scripts\Activate.ps1

Install dependencies:

    pip install -r requirements.txt

Configure application settings in `.env`.

Run the application from the project root:

    python -m employee_management.main

## Logging

Application logs are stored in:

    logs/application.log

## Configuration

Configuration is loaded from `.env` using python-dotenv.

Do not commit `.env` or sensitive information to GitHub.
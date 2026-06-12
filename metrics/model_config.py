"""
Azure OpenAI model configuration for deepeval.

This module provides a shared model identifier for all deepeval metrics,
configured to use the internal Azure OpenAI endpoint.

Credentials are loaded from environment variables (set via a .env file
or your CI/CD environment). No secrets are hard-coded in source code.

Required environment variables:
    AZURE_API_KEY          - Azure OpenAI API key
    AZURE_API_BASE         - Azure OpenAI endpoint URL
    AZURE_API_VERSION      - Azure OpenAI API version
    AZURE_DEPLOYMENT_NAME  - Azure OpenAI deployment (model) name
"""

import os
import sys

from dotenv import load_dotenv

# Load .env file if present (no-op when vars are set externally, e.g. CI)
load_dotenv()

_REQUIRED_VARS = [
    "AZURE_API_KEY",
    "AZURE_API_BASE",
    "AZURE_API_VERSION",
    "AZURE_DEPLOYMENT_NAME",
]

_missing = [v for v in _REQUIRED_VARS if not os.getenv(v)]
if _missing:
    print(
        f"ERROR: Missing required environment variables: {', '.join(_missing)}\n"
        "Please copy .env.example to .env and fill in your Azure OpenAI credentials.",
        file=sys.stderr,
    )
    sys.exit(1)

# deepeval uses litellm under the hood.
# The "azure/<deployment>" prefix tells litellm to route to Azure OpenAI,
# using AZURE_API_KEY, AZURE_API_BASE, and AZURE_API_VERSION from the env.
MODEL = f"azure/{os.environ['AZURE_DEPLOYMENT_NAME']}"

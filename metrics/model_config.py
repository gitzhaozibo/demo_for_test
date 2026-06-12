"""
Azure OpenAI model configuration for deepeval.

This module provides a custom DeepEvalBaseLLM implementation that talks
directly to a private Azure OpenAI endpoint via the openai SDK, bypassing
litellm's public-model routing.

Credentials are loaded from environment variables (set via a .env file
or your CI/CD environment). No secrets are hard-coded in source code.

Required environment variables:
    AZURE_API_KEY          - Azure OpenAI API key
    AZURE_API_BASE         - Azure OpenAI endpoint URL (private or public)
    AZURE_API_VERSION      - Azure OpenAI API version
    AZURE_DEPLOYMENT_NAME  - Azure OpenAI deployment (model) name
"""

import os
import sys
from typing import Tuple

from dotenv import load_dotenv
from openai import AsyncAzureOpenAI, AzureOpenAI

from deepeval.models.base_model import DeepEvalBaseLLM

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


class AzureOpenAILLM(DeepEvalBaseLLM):
    """Custom DeepEvalBaseLLM that calls a private Azure OpenAI endpoint directly.

    Unlike the litellm-based string approach, this class uses the openai SDK
    so it works with both public and private (VNet/private-endpoint) deployments.
    """

    def __init__(self) -> None:
        self._api_key = os.environ["AZURE_API_KEY"]
        self._endpoint = os.environ["AZURE_API_BASE"]
        self._api_version = os.environ["AZURE_API_VERSION"]
        self._deployment = os.environ["AZURE_DEPLOYMENT_NAME"]

    def get_model_name(self) -> str:
        return f"Azure OpenAI ({self._deployment})"

    def load_model(self) -> AzureOpenAI:
        return AzureOpenAI(
            api_key=self._api_key,
            azure_endpoint=self._endpoint,
            api_version=self._api_version,
        )

    def generate(self, prompt: str) -> Tuple[str, float]:
        client = self.load_model()
        response = client.chat.completions.create(
            model=self._deployment,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content, 0.0

    async def a_generate(self, prompt: str) -> Tuple[str, float]:
        async_client = AsyncAzureOpenAI(
            api_key=self._api_key,
            azure_endpoint=self._endpoint,
            api_version=self._api_version,
        )
        response = await async_client.chat.completions.create(
            model=self._deployment,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content, 0.0


# Shared model instance used by all metrics.
MODEL = AzureOpenAILLM()

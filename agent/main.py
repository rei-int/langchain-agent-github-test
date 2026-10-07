"""Entrypoint shim: point the stock OpenAI SDK at the governed egress proxy.

The platform injects TRASE_OPENAI_BASE_URL and TRASE_RUN_CREDENTIAL. The OpenAI
SDK reads OPENAI_BASE_URL and OPENAI_API_KEY. Aliasing the two here keeps the
agent itself stock — wrap, don't edit. If the platform injected the SDK-standard
names, this file would not need to exist and `entrypoint` could point straight
at the agent.

TRASE_RUN_CREDENTIAL is the grant handle (it starts with ``dsa_``). The proxy
ignores a bare run id in this slot, and the call is refused as
egress.callerUnidentified before any destination is named.
"""

import os


def run() -> str:
    os.environ["OPENAI_BASE_URL"] = os.environ["TRASE_OPENAI_BASE_URL"]
    os.environ["OPENAI_API_KEY"] = os.environ["TRASE_RUN_CREDENTIAL"]

    from agent.agent import main

    return main()

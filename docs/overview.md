# Connector Overview

`adk-conn` packages a small agent that uses Google ADK plus an
`ApplicationIntegrationToolset` instance to expose connector-backed operations to an
LLM agent.

## Primary Components

- `conn/agent.py` defines the tool binding and the root agent.
- `conn/pyproject.toml` captures the Python package metadata and dependencies.
- `conn/README.md` is the package-level entry point for local setup.

## Intended Direction

The repository should evolve from an example into a repeatable connector template with:

- environment-driven configuration instead of inline placeholders
- a clear runtime contract for supported entity operations
- smoke tests for connection validation and prompt behavior

## Immediate Documentation Needs

- document how project, location, and connection identifiers are supplied
- define how connector permissions are represented
- describe expected failure modes for unavailable entities or quota issues

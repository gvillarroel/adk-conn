# Runtime and Configuration

The current implementation hard-codes several values in `conn/agent.py`. That is good
enough for a prototype, but not for repeatable execution across environments.

## Required Runtime Inputs

- Google Cloud project id
- connector location
- connection name
- allowed entity operations
- selected model name

## Recommended Configuration Model

1. Read connector settings from environment variables.
2. Validate them at startup before the agent is created.
3. Emit a short startup summary that confirms the active connection.
4. Fail fast when a required field is missing.

## Operational Checks

- confirm the target connection exists in the expected location
- verify the agent has permission to call the configured entity operations
- validate one low-risk operation such as `LIST` before wider rollout

## Follow-Up

Add one scripted smoke test that boots the agent with a disposable configuration and
asserts the toolset can be created successfully.

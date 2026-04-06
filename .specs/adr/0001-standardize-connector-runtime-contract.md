---
adr: "0001"
title: "ADR 0001: Standardize the Connector Runtime Contract"
summary: "Define one consistent runtime contract for transport, auth, and tool registration across ADK connectors."
status: "Proposed"
date: "2026-04-05"
product: "adk-conn"
owner: "Platform Architecture"
area: "Connector Runtime"
tags:
  - architecture
  - connectors
  - runtime
---

# ADR 0001: Standardize the Connector Runtime Contract

## Status

Proposed

## Context

The repository is evolving toward a reusable connector layer, but transport behavior,
authentication flow, and tool exposure rules are not yet expressed as one stable contract.
That makes it harder to onboard a new connector, compare integrations, and automate tests.

## Decision

We should define a shared connector runtime contract that covers:

- lifecycle hooks
- auth injection
- request and response envelopes
- error normalization
- tool registration boundaries

## Consequences

Positive:

- new connectors become faster to add
- tests can validate one contract instead of connector-specific behavior
- observability becomes easier to standardize

Negative:

- the first pass will require refactoring uneven integration code
- stricter boundaries may expose assumptions in existing experiments

## Follow-Up

- draft the contract in code and docs
- add one golden-path example connector
- add contract tests for success and failure paths

# Make.com

Make.com is an automation tool where each automation workflow someone builds is called a scenario, and the components of that scenario(spreadsheet actions,email actions,routes, webhooks, ...) of the automation are called modules. The data that is being passed from one module to another is called a bundle.

### What makes Make.com stand out from Zapier and n8n is that:

- iteration of list is native or automatic.
- non-linear branching via router
- the canvas itself is the logic

# Zapier

zapier is the oldest automation tool in the eco-system. it's the richest in terms of library of pre-built apps to use for assembling automation.

### what makes zapier standout:

- it's rich library
- it's very simple to use
- it's strictly step by step

# n8n

n8n is the tool where it's open-source and can be self hosted. it's the most flexible from the 3.

### what makes n8n stand out:

- it's self hosted
- it's the most flexible for the professional with full data access.
- very cost efficient.

#### custom backend along with n8n

a custom backend can be used along n8n for 2 main ways:

1. _n8n_: acts like an **outer orchestrator** where heavy tasks are handled by the custom backend(i.e custom LLM,determinstic logic,...) while 3rd party SaaS connections are maintained and activated by n8n(email,spreadsheets,...)2. _backend as a core engine_:here everything is handled by the backend and n8n only handles non-critical operations like notifications.

## Architectural difference:

| Dimension | Excution model   |                                            | Excution model                                                | When to use |
| --------- | ---------------- | ------------------------------------------ | ------------------------------------------------------------- | ----------- |
| Zapier    | sequential       | task-based(very expensive for high volume) | quick and standard automation for non-dev to manage           |
| n8n       | Graph/node based | Fixed VPS cost(very cheap alternative)     | for privacy sensitive and high vol pipeline.                  |
| make.com  | Graph based      | operation-based(moderate price)            | for complex data transformation to avoid writing backend code |

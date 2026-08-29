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

## Architectural difference:

| Dimension | Excution model || Excution model |
|--------------|-----------------||-----------------|
| Zapier |sequential |task-based(very expensive for high volume) |
| n8n |Graph/node based|Fixed VPS cost(very cheap alternative) |
| make.com |Graph based |operation-based(moderate price) |

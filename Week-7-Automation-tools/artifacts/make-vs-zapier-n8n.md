# Make.com

Make.com is an automation tool where each automation workflow someone builds is called a scenario, and the components of that scenario(spreadsheet actions,email actions,routes, webhooks, ...) of the automation are called modules. The data that is being passed from one module to another is called a bundle.

What makes Make.com stand out from Zapier and n8n is that:

- iteration of list is native or automatic. That is, if a module returns data as a list of items, then Make.com does the next operations of the modules for each item in the list.
- non-linear branching via router, where there can be multiple paths of an automation that can run simultaneously without any pre-condition.
- the canvas itself is the logic, where everything regarding the automation is visible there.

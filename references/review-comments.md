# How to Write Code Review Comments

## Core Rules

1. **Comment on the code, never the developer.** Bad: "You did X wrong." Good: "This function could handle the null case."
2. **Explain the reasoning.** Do not just say "this is wrong" -- explain why and what principle applies.
3. **Balance direction with autonomy.** Point out problems and let the author decide how to fix them when possible. Provide direct guidance for critical issues.

## Comment Labels

Use severity labels to set clear expectations:

- **Blocker / Required**: Must be fixed before approval
- **High / Should fix**: Strongly recommended but author can justify skipping
- **Nit:**: Minor style or preference issue, not blocking
- **Optional:**: Suggestion the author can take or leave
- **FYI:**: Educational context, no action required

## Writing Effective Comments

- Be specific: cite the exact line range and explain the problem
- Be constructive: suggest a direction, not just a complaint
- Be concise: one clear point per comment
- Separate concerns: one comment per issue, not bundled

## When Code Needs Explanation

If the author explains code only in the review thread, request that the explanation be added to the code itself (as a comment or by simplifying the code). Future readers will not see review threads.

## Acknowledge Good Work

When you see clean code, a clever solution, or thorough testing, say so. Positive feedback reinforces the practices you want to see more of.

## Handling Pushback

- If the author disagrees, consider whether they have a valid point -- they are closer to the code
- Explain your reasoning thoroughly when you believe the change matters for code health
- Insist on cleanup now rather than accepting "I will fix it later" -- deferred cleanup rarely happens
- Stay professional and kind throughout

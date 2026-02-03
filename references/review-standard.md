# The Standard of Code Review

## Core Standard

Approve a CL once it definitely improves overall code health of the codebase -- even if imperfect. No code is "perfect" -- only "better." A CL that improves maintainability, readability, or understandability should not be delayed for days because it is not perfect.

## Principles (ordered by precedence)

1. **Technical facts and data** override personal preferences and opinions
2. **Style guide** is the authority on style matters -- not the reviewer's taste
3. **Software design** decisions rest on engineering principles, not opinion
4. When **multiple valid approaches** exist with supporting evidence, accept the author's choice
5. If no other rule applies, the reviewer may request consistency with the existing codebase, as long as it does not worsen overall code health

## Mentoring in Reviews

Share knowledge through review comments, but mark educational-only comments as non-mandatory. Prefix with "Nit:" or "Optional:" to signal these are not blocking.

## Conflict Resolution

1. Seek consensus based on documented guidelines
2. Consider synchronous discussion if written review stalls
3. Escalate to team leads or maintainers rather than letting reviews block progress

## Key Judgments

- **Approve** when the CL improves code health, even if you would have done it differently
- **Request changes** when the CL degrades code health or introduces issues
- **LGTM with comments** when confident the author will address remaining non-blocking feedback
- Never approve a CL that degrades overall code health, even under time pressure

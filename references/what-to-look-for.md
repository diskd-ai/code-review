# What to Look For in a Code Review

Review every line assigned to you. For each area below, focus only on issues **introduced by the change**, not pre-existing problems.

## 1. Design

- Does the change belong in this codebase, or in a library/service?
- Does it integrate well with the rest of the system?
- Is the overall architecture appropriate for the problem?
- Is the timing right, or does this depend on unmerged work?

## 2. Functionality

- Does the code do what the author intended?
- Is the intended behavior good for users (end-users and developers)?
- Check edge cases, concurrency, and potential bugs
- For UI changes: look at the actual rendered result, not just the code
- Think about parallel programming issues: deadlocks, race conditions

## 3. Complexity

- Can any part be simplified without losing correctness?
- Is any line, function, or class too hard for another developer to understand quickly?
- Flag over-engineering: code solving problems that do not yet exist
- "Too complex" = cannot be understood quickly by code readers

## 4. Tests

- Are unit, integration, or end-to-end tests present and appropriate?
- Will tests actually fail when the code breaks?
- Do tests avoid false positives (testing implementation rather than behavior)?
- Treat test code with the same quality bar as production code

## 5. Naming

- Are names long enough to communicate intent, short enough to be readable?
- Does naming follow project conventions?

## 6. Comments

- Comments should explain **why**, not **what** (code should be self-explanatory)
- Exceptions: regex, complex algorithms may need "what" comments
- If code needs a comment to explain what it does, consider simplifying the code first
- TODOs should reference a tracking issue

## 7. Style

- Follow the project style guide -- do not mix style fixes with functional changes
- Prefix non-blocking style suggestions with "Nit:"
- Never block a CL solely on style nits

## 8. Documentation

- If the CL changes build, test, interaction, or release processes, update related docs
- If the CL deprecates or removes code, update or remove corresponding docs

## 9. Every Line

- Read every line of human-written code assigned to you
- For data files, generated code, or large structures: scan for reasonableness
- If a line is hard to read and slows down the review, ask the author to clarify the code itself (not just explain in the review thread)

## 10. Context

- Look at the whole file, not just the changed lines -- the change may add complexity in context
- Consider the CL in the broader system context

## 11. Good Things

- Tell the author when they did something well
- Positive reinforcement of good practices is at least as valuable as pointing out mistakes

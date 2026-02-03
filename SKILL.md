---
name: code-review
description: "Review code with a structured, high-signal review process. Use when asked to review code, review a PR, review a codebase, give feedback on a changelist, audit code quality, or perform a code review. Supports both diff/PR reviews and full codebase reviews. Produces actionable findings with severity labels, exact file+line citations, and a final verdict. Covers design, functionality, complexity, tests, naming, comments, style, documentation, security, and performance."
---

# Code Review

Perform a structured code review. Produce actionable findings with exact file+line citations.

## Determine Review Mode

1. **Change review** (PR, diff, CL): review only code introduced by the change. Go to "Change Review Workflow."
2. **Codebase review** (full repo, specific files/modules): review the code as-is. Go to "Codebase Review Workflow."

---

## Change Review Workflow

### 1. Establish what to review

Obtain access to the post-change files for accurate line citations.

- Local checkout: use `git diff` (unstaged/staged) or a commit range
- If only a diff snippet is provided: ask for a branch/commit or full file contents

### 2. Scope the change

Constrain the review to code introduced by the change:

```bash
git diff --name-only          # changed files
git diff --stat               # change size per file
python scripts/diff_changed_ranges.py --json  # changed line ranges per file
```

### 3. Broad assessment

Read the CL/PR description and skim all changed files. Ask: "Does this change make sense as a whole?"

- If the change should not proceed at all, provide immediate feedback with reasoning
- If the overall design is wrong, flag it before reviewing details

### 4. Critical components

Identify the most significant files (largest logical changes) and review those first. This provides context for smaller modifications.

If fundamental design issues emerge, communicate immediately -- major restructuring may invalidate subsequent code.

### 5. Systematic review

Review remaining files in logical order. Read tests before implementation when it helps clarify intent. Apply the review checklist (step 6 below).

Rules:
- Do not comment on pre-existing issues unless the change makes them newly reachable
- Prefer blocker/high-severity items over nits
- Review every line of human-written code

### 6. Verdict

- **Approve** if the CL improves overall code health, even if imperfect
- **Request changes** if the CL degrades code health or has blocking issues
- Technical facts override personal preference; accept the author's valid approach when multiple exist

---

## Codebase Review Workflow

### 1. Establish scope

Determine what to review:

- **Entire repo**: scan project structure, identify key modules
- **Specific files/modules**: focus on the requested scope
- **Specific concern** (e.g., "review security," "review architecture"): focus the checklist on that area

### 2. Understand the architecture

- Read project structure, entry points, and dependency graph
- Identify layers (domain, infrastructure, API, etc.)
- Note the tech stack, patterns, and conventions in use

### 3. Systematic review

Walk through the code module by module. Apply the review checklist below, focusing on all areas or the specific concern requested.

### 4. Summary

Provide an overall assessment of code health with prioritized findings.

---

## Review Checklist

For each file/hunk under review, evaluate against these areas (see [references/what-to-look-for.md](references/what-to-look-for.md) for full details):

| Area | Key questions |
|------|--------------|
| **Design** | Right architecture? Belongs here? Proper separation of concerns? |
| **Functionality** | Does what's intended? Edge cases handled? |
| **Complexity** | Simplest correct solution? Over-engineered? |
| **Tests** | Present, correct, will fail when code breaks? |
| **Naming** | Descriptive, follows conventions? |
| **Comments** | Explain why, not what? |
| **Style** | Follows style guide? Consistent? |
| **Docs** | Updated if behavior changed? |
| **Security** | Input validation, auth, injection, secrets? |
| **Performance** | N+1, unbounded loops, resource leaks, races? |

## Verify Citations

Before writing each finding, verify exact line numbers:

```bash
python scripts/print_lines.py <file> <startLine> <endLine>
```

Use citation format: `path/to/file.ts#L10-L42`

## Write Comments

Follow comment best practices (see [references/review-comments.md](references/review-comments.md) for full guide):

- Comment on the **code**, never the developer
- Explain **why** the issue matters
- Use severity labels: **Blocker**, **High**, **Nit:**, **Optional:**, **FYI:**
- One issue per comment
- Acknowledge good work

## Produce the Review

Fill the template from `assets/review_template.md`. Each finding must include:

- Severity (Blocker / High / Medium / Low)
- Actionable fix direction
- Exact `file#Lx-Ly` citation

End with:
- **Verdict**: `approve`, `request changes`, or `comment only`
- 1-2 sentence justification
- **Confidence**: 0.0 to 1.0

## Reference Files

- **[references/review-standard.md](references/review-standard.md)** -- Core review standard: when to approve vs request changes, conflict resolution
- **[references/what-to-look-for.md](references/what-to-look-for.md)** -- Full checklist of review areas with details for each
- **[references/review-comments.md](references/review-comments.md)** -- How to write effective comments, severity labels, handling pushback

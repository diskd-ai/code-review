# Code Review Skill

> **Install:** `npx skills add diskd-ai/code-review` | [skills.sh](https://skills.sh)

Structured code review skill that produces high-signal, actionable findings with severity labels, exact file+line citations, and a final verdict. Supports both PR/diff reviews and full codebase reviews.

---

## Scope & Purpose

This skill provides a repeatable review workflow covering:

* Design and architecture assessment
* Functionality and correctness verification
* Complexity and over-engineering detection
* Test coverage and quality evaluation
* Naming, comments, style, and documentation checks
* Security vulnerability scanning
* Performance and reliability analysis

---

## When to Use This Skill

**Triggers:**
* Asked to review code, a PR, a diff, a CL, or a codebase
* Asked to audit code quality, perform a security review, or check architecture
* Mentions of "code review," "review this," or "give feedback on this code"

**Use cases:**
* Review a pull request or diff before merge
* Audit an entire codebase or specific module for quality
* Focus on a specific concern (security, performance, design)
* Produce a standardized review report with prioritized findings

---

## Review Workflow

### Change Review (PR / diff / CL)

1. Establish what to review (checkout, diff access)
2. Scope the change (`git diff --name-only`, `diff_changed_ranges.py`)
3. Broad assessment -- does the change make sense as a whole?
4. Critical components -- review largest logical changes first
5. Systematic review -- remaining files against the checklist
6. Verdict -- approve, request changes, or comment only

### Codebase Review (full repo / module / files)

1. Establish scope -- entire repo, specific module, or specific concern
2. Understand the architecture -- structure, layers, patterns
3. Systematic review -- module by module against the checklist
4. Summary -- overall code health with prioritized findings

---

## Review Checklist

| Area | Key Questions |
|------|--------------|
| **Design** | Right architecture? Proper separation of concerns? |
| **Functionality** | Does what's intended? Edge cases handled? |
| **Complexity** | Simplest correct solution? Over-engineered? |
| **Tests** | Present, correct, will fail when code breaks? |
| **Naming** | Descriptive, follows conventions? |
| **Comments** | Explain why, not what? |
| **Style** | Follows style guide? Consistent? |
| **Documentation** | Updated if behavior changed? |
| **Security** | Input validation, auth, injection, secrets? |
| **Performance** | N+1, unbounded loops, resource leaks, races? |

---

## Severity Labels

| Label | Meaning |
|-------|---------|
| **Blocker** | Must be fixed before approval |
| **High** | Strongly recommended to fix |
| **Medium** | Worth addressing |
| **Nit** | Minor style or preference, not blocking |
| **Optional** | Suggestion the author can take or leave |
| **FYI** | Educational context, no action required |

---

## Skill Structure

```
code-review/
  SKILL.md                           # Entry point (workflow + checklist)
  README.md                          # This file (overview)
  references/
    review-standard.md               # When to approve vs request changes
    what-to-look-for.md              # Full review checklist with details
    review-comments.md               # How to write effective comments
  scripts/
    diff_changed_ranges.py           # Parse git diff into changed line ranges
    print_lines.py                   # Print exact line ranges for citations
  assets/
    review_template.md               # Standardized review report template
```

---

## Report Format

Every review produces a standardized report (see `assets/review_template.md`):

* **Metadata** -- scope, date, review mode
* **Summary** -- 1-3 sentence overview
* **Findings** -- tables grouped by severity, each with area, `file#Lx-Ly` citation, description, and suggested fix
* **Positive Observations** -- acknowledge good code and patterns
* **Checklist Summary** -- pass / needs work / N/A per area
* **Verdict** -- approve / request changes / comment only, justification, confidence score

---

## Resources

* **Full skill reference**: [SKILL.md](SKILL.md)
* **Review standard**: [references/review-standard.md](references/review-standard.md)
* **What to look for**: [references/what-to-look-for.md](references/what-to-look-for.md)
* **Comment best practices**: [references/review-comments.md](references/review-comments.md)
* **Report template**: [assets/review_template.md](assets/review_template.md)

---

## License

MIT

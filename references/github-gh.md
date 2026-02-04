# GitHub PR Review with `gh`

Prefer a local checkout for accurate `path/to/file#Lx-Ly` citations.

## Authenticate

```bash
gh auth status
gh auth login
```

Non-interactive auth (PAT on stdin):

```bash
gh auth login --with-token < token.txt
```

Per `gh auth login --help`, the minimum PAT scopes are `repo`, `read:org`, and `gist`.

## Clone and check out the PR (preferred)

Clone once:

```bash
gh repo clone OWNER/REPO
cd REPO
```

Check out by PR number/URL/branch:

```bash
gh pr checkout 123
```

If not in a repo directory, target a repo explicitly:

```bash
gh pr checkout 123 -R OWNER/REPO
```

## Inspect PR metadata

```bash
gh pr view 123
gh pr view 123 --comments
```

If you need structured data (changed files, base branch, etc.):

```bash
gh pr view 123 --json baseRefName,headRefName,changedFiles,files
```

## Get changed files / diff

Quick file list:

```bash
gh pr diff 123 --name-only
```

Patch (useful when you cannot check out locally):

```bash
gh pr diff 123 --patch --color=never
```

## Map changes to local line citations

Read the base branch from the PR:

```bash
BASE_BRANCH="$(gh pr view 123 --json baseRefName -q .baseRefName)"
```

Then diff against it and compute changed line ranges:

```bash
git fetch origin "$BASE_BRANCH"
git diff --name-only "origin/$BASE_BRANCH...HEAD"
python scripts/diff_changed_ranges.py --range "origin/$BASE_BRANCH...HEAD" --json
```

## Post review feedback (summary review)

Approve / comment / request changes:

```bash
gh pr review 123 --approve -b "LGTM"
gh pr review 123 --comment -b "Non-blocking: consider simplifying X."
gh pr review 123 --request-changes -b "Blocker: missing validation for Y."
```

Multi-line review body from stdin:

```bash
cat <<'EOF' | gh pr review 123 --request-changes --body-file -
Blocker: ...

High: ...
EOF
```

Comment without submitting a review:

```bash
cat <<'EOF' | gh pr comment 123 --body-file -
FYI: ...
EOF
```

## References

- CLI help: `gh help pr`, `gh pr view --help`, `gh pr diff --help`, `gh pr review --help`
- Manual: https://cli.github.com/manual/

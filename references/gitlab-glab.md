# GitLab MR Review with `glab`

Prefer a local checkout for accurate `path/to/file#Lx-Ly` citations.

## Authenticate

```bash
glab auth status
glab auth login
```

Non-interactive auth (token on stdin):

```bash
glab auth login --stdin < token.txt
```

Per `glab auth login --help`, the minimum token scopes are `api` and `write_repository`.

## Clone and check out the MR (preferred)

Clone once:

```bash
glab repo clone GROUP/NAMESPACE/REPO
cd REPO
```

Check out by MR ID / branch / URL:

```bash
glab mr checkout 123
```

If not in a repo directory, target a repo explicitly:

```bash
glab mr checkout 123 -R GROUP/NAMESPACE/REPO
```

## Inspect MR metadata

```bash
glab mr view 123
glab mr view 123 --comments
```

Open in the browser when you need fields not shown in text output:

```bash
glab mr view 123 --web
```

## Get diff

Raw diff (pipe-friendly):

```bash
glab mr diff 123 --raw --color=never
```

## Map changes to local line citations

After checkout, identify the target branch (shown by `glab mr view 123`) and diff against it.

Example (replace `TARGET_BRANCH` as needed):

```bash
TARGET_BRANCH="main"
git fetch origin "$TARGET_BRANCH"
git diff --name-only "origin/$TARGET_BRANCH...HEAD"
python scripts/diff_changed_ranges.py --range "origin/$TARGET_BRANCH...HEAD" --json
```

## Post review feedback

Approve:

```bash
glab mr approve 123
```

Revoke approval:

```bash
glab mr revoke 123
```

Comment (use `-m` for non-interactive usage):

```bash
glab mr note 123 -m "Blocker: missing validation for Y."
```

## References

- CLI help: `glab help mr`, `glab mr view --help`, `glab mr diff --help`, `glab mr approve --help`, `glab mr note --help`
- GitLab docs: https://docs.gitlab.com/editor_extensions/gitlab_cli/

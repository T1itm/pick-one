# Contributing to Pick-One

Thank you for contributing to Pick-One (ladder, spinner, and dice games).
Every change follows the same flow: **Issue → Branch → Pull Request → Review → Merge**.

## 1. Start with an issue
- Before you start working, open an issue or assign yourself to an existing one.
- Issues start in the `Backlog` column of the GitHub Projects board. Move the card to `In progress` when you start.
- Keep each issue small enough for one person to finish in one or two days.

## 2. Branch rules
- `main` must always be in a working state. **Never push directly to `main`.**
- Create a new branch from `main` for every task.

| Type | Name format | Example |
|------|-------------|---------|
| New feature | `feat/<issue-number>-<description>` | `feat/4-dice-roll` |
| Bug fix | `fix/<issue-number>-<description>` | `fix/12-wheel-overlap` |
| Documentation | `docs/<issue-number>-<description>` | `docs/3-contributing` |
| Tests | `test/<issue-number>-<description>` | `test/8-ladder-logic` |

```bash
git switch main
git pull origin main
git switch -c feat/4-dice-roll
```

- Use lowercase English letters and hyphens (`-`) only.
- Delete your branch after the pull request is merged.

## 3. Commit messages
```
<type>: <what you did> (#<issue-number>)
```
Examples: `feat: add dice count selector (#4)`, `fix: prevent spinner labels from overlapping (#12)`

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `style`, `chore`

## 4. Pull request rules
- Fill in every section of the pull request template.
- Write `Closes #<issue-number>` in the description so the issue closes automatically when merged.
- One pull request should solve **one issue**. Split large changes into smaller pull requests.
- Before opening a pull request, update your branch with the latest `main` and test your change in the browser.

## 5. Review rules
- A pull request needs **at least one approval from a teammate other than the author** before it can be merged.
- Respond to review requests **within 24 hours**.
- Reviewers check that:
  - the change meets the issue's completion criteria,
  - it works when they run it themselves,
  - the code is readable and understandable.
- Comment on the code, not the person, and explain your reasoning.
  - Good example: "Labels overlap when there are more than 12 items. Could we limit the maximum?"
- If changes are requested, add new commits to the same branch and request a review again.
- After all conversations are resolved, **the pull request author merges it** using **Squash and merge**.

## 6. Using AI tools
AI tools are allowed under these rules:
- You must **understand and be able to explain** any code you submit.
- In the "AI usage" section of the pull request template, describe what you delegated, how you checked the output, and what you changed or rejected.
- An AI review never replaces a human review from a teammate.

## 7. Repository settings (for admins)
Settings → Branches → Add branch protection rule → `main`
- [x] Require a pull request before merging
- [x] Require approvals: **1**
- [x] Require conversation resolution before merging
- [x] Do not allow bypassing the above settings

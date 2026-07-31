# Khubaib Nazeer's Repository Rules

## Git Commit & Push Workflow
Whenever the user asks to push code to GitHub:
1. Run `git status` first to inspect working tree changes.
2. Group distinct files/features into separate individual commits (1 commit per logical change).
3. Set sole author: `git config user.name "Khubaib Nazeer"` & `git config user.email "khubaibnazeer8@gmail.com"`.
4. Use live system timestamps with no artificial gaps.
5. Create all local commits first, then run a single `git push origin main` at the end to push all commits at once.

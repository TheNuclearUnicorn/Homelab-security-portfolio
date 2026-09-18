# First Public Git Commit

The Stage 7 working tree is suitable for initialization as a new public repository. It should **not** inherit private infrastructure-repository history.

## Recommended First Commit

From the repository root:

```bash
git init -b main
git add .
git status
```

Review the staged tree, complete `PUBLICATION-CHECKLIST.md`, and run your preferred secret scanner.

Configure your own public Git identity; this package does not invent one:

```bash
git config user.name "<YOUR PUBLIC GIT NAME>"
git config user.email "<YOUR PUBLIC GIT EMAIL>"
```

Create the first commit:

```bash
git commit -m "docs: publish homelab security portfolio v1.0.0"
```

After creating the public repository:

```bash
git remote add origin <PUBLIC_REPOSITORY_URL>
git push -u origin main
```

Optional release tag after final GitHub review:

```bash
git tag -a v1.0.0 -m "Homelab Security Portfolio v1.0.0"
git push origin v1.0.0
```

Do not publish from a filtered copy of the private infrastructure repository. The public portfolio should keep independent Git history from its first commit.

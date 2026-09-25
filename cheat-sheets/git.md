# Git Cheat Sheet

Quick reference for Git commands used in this curriculum.

## Basic Commands

### Configuration
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Repository Setup
```bash
git init                    # Initialize new repository
git clone <url>             # Clone existing repository
```

## Daily Workflow

### Check Status
```bash
git status                  # Show working directory status
```

### Stage Changes
```bash
git add <file>              # Stage specific file
git add .                   # Stage all changes
git add -A                  # Stage all changes (including deletions)
```

### Commit
```bash
git commit -m "message"     # Commit staged changes
```

### Push/Pull
```bash
git push                    # Push commits to remote
git pull                    # Pull changes from remote
```

## Branching

### Branch Operations
```bash
git branch                  # List branches
git branch <name>           # Create new branch
git checkout <name>         # Switch to branch
git checkout -b <name>      # Create and switch to branch
git branch -d <name>        # Delete branch
```

### Merging
```bash
git merge <branch>         # Merge branch into current
```

## Useful Commands

### History
```bash
git log                     # Show commit history
git log --oneline           # Compact history
```

### Undo Changes
```bash
git checkout -- <file>      # Discard file changes
git reset HEAD <file>       # Unstage file
```

### Remote Operations
```bash
git remote -v               # Show remote repositories
git remote add <name> <url> # Add remote
```

## Common Patterns

### Feature Branch Workflow
```bash
git checkout -b feature-name
# Make changes
git add .
git commit -m "Add feature"
git push origin feature-name
```

### Fix Mistakes
```bash
git commit --amend         # Fix last commit
git reset --soft HEAD~1     # Undo last commit, keep changes
```

---

*This cheat sheet is a quick reference. For detailed understanding, refer to official Git documentation.*

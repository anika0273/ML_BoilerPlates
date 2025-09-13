```bash
git filter-branch --force --index-filter \
'git ls-files -s | grep -vE "\.ipynb$|\.gitignore$" | cut -f 2 | xargs git rm --cached -r --ignore-unmatch' \
--prune-empty --tag-name-filter cat -- --all
```

```bash
git reflog expire --expire=now --all
git gc --prune=now --aggressivegit push origin --force --all
```

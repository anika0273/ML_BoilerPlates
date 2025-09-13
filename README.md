# If you are having any issues pushing the code on github

```bash
git filter-branch --force --index-filter \
'git ls-files -s | grep -vE "\.ipynb$|\.gitignore$" | cut -f 2 | xargs git rm --cached -r --ignore-unmatch' \
--prune-empty --tag-name-filter cat -- --all
```

```bash
git reflog expire --expire=now --all
git gc --prune=now --aggressivegit push origin --force --all
```

# If you are running into any import error it is best to create a new venv, for each of code. Follow the steps below:

1. Create the venv and Activate

```text
python3 -m venv your_venv_name
source your_venv_name/bin/activate
```

2. Upgrade pip

```text
pip install --upgrade pip
```

3. Install All Required Packages

```text
pip install numpy pandas matplotlib seaborn scikit-learn joblib notebook ipykernel
```

4. Register the New Kernel with Jupyter

```text
python -m ipykernel install --user --name=your_venv_name --display-name="Python (your_venv_name)"
```

This will make "Python (your_venv_name)" available as a selectable kernel in Jupyter.

5. Launch Jupyter Notebook

```text
jupyter notebook
```

6. In Your Jupyter Notebook
   Go to the Kernel menu → Change Kernel → Python (kmeansvenv)

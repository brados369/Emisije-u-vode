name: Update Data and Push to GitHub
on:
  schedule:
    - cron: '0 0 * * 1' # Pokreće se jednom nedeljno (ponedeljak u ponoć)
  workflow_dispatch: # Ručno pokretanje
jobs:
  update_data:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Setup Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install pandas requests

    - name: Run update script
      run: python update_data.py

    - name: Commit and push changes
      run: |
        git config --global user.name "GitHub Actions"
        git config --global user.email "actions@github.com"
        git add emisije_vode.xlsx emisije_vode_*.xlsx emisije_vode_*.html emisije_vode_*.pdf
        git commit -m "Automatsko ažuriranje podataka i analize"
        git push

message=$1

# 复制 README.md
cp README.md docs/README.md

# 更新 master
git add .
git commit -m "$message"
git push -f git@github.com:mymmon/PCL-notebook.git master

# 更新 gh-pages
cd docs/
git init
git add -A
git commit -m "$message"
git push -f git@github.com:mymmon/PCL-notebook.git master:gh-pages
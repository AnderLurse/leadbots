#!/bin/bash
cd "/c/Users/Desktop-k806k2/Documents/leadbots" || exit
git add .
commit_msg="update: $(date '+%Y-%m-%d %H:%M:%S') - auto commit"
git commit -m "$commit_msg"
git push origin main

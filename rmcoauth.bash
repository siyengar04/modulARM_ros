git filter-branch --force --env-filter '

if [ "$GIT_AUTHOR_EMAIL" = "sameer.m.iyengar@gmail.com" ]; then
  
export GIT_AUTHOR_NAME="Sameer Iyengar"
                                  
export GIT_AUTHOR_EMAIL="sameer.m.iyengar@gmail.com"
                                              
fi
  
if [ "$GIT_COMMITTER_EMAIL" = "sameer.m.iyengar@gmail.com" ]; then
                                                                 
export GIT_COMMITTER_NAME="Sameer Iyengar"
                                     
export GIT_COMMITTER_EMAIL="sameer.m.iyengar@gmail.com"
                                                 
fi
  
' --msg-filter 'sed "/Co-authored-by/d"' --tag-name-filter cat -- --branches --tags

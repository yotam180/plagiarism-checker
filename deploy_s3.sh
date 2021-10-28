REACT_APP_REMOTE_URL="/process" npm run-script build
aws s3 sync build/ s3://plagiarism-checker-frontend --acl public-read
aws cloudfront create-invalidation --distribution-id E2BILBK6D9Y0EG --paths "/*"

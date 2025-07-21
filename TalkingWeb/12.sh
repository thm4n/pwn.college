cat << EOF | nc challenge.localhost 80
GET /submission%20gate%20task HTTP/1.1
Host: challenge.localhost:80

EOF

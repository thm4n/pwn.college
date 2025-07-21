cat << EOF | nc challenge.localhost 80
GET / HTTP/1.1
Host: challenge.localhost:80
Cookie: cookie=242683a97cadd3fdf1fa49cd74ceb515

EOF

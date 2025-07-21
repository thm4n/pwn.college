cat << EOF | nc challenge.localhost 80
POST /entry HTTP/1.1
Host: challenge.localhost:80
Content-Type: application/x-www-form-urlencoded
Content-Length: 19

secret_key=cqjrjtix

EOF

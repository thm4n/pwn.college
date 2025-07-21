location=$(cat << EOF | nc challenge.localhost 80 | grep "Location: /" | awk '{print $2}'
GET / HTTP/1.1
Host: challenge.localhost:80
Content-Type: application/x-www-form-urlencoded

EOF
)

cat << EOF | nc challenge.localhost 80
GET ${location} HTTP/1.1
Host: challenge.localhost:80
Content-Type: application/x-www-form-urlencoded

EOF

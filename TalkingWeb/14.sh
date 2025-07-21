cat << EOF | nc challenge.localhost 80
GET /fulfill?access=hohzbrqd&auth_token=xxeoghbs&secret_key=ewlmnixz HTTP/1.1
Host: challenge.localhost:80

EOF

# < /dev/urandom tr -dc 'A-Za-z0-9' | head -c 16 | xargs ./scripts/generate_hash.sh
echo "### Please change your password after your first login ###"
echo user: admin
echo password: $1
docker run --rm authelia/authelia:latest authelia crypto hash generate argon2 --password "$1"

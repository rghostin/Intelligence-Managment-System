# Installation

### Preparation
- [ ] **Optional** clean up everything related to docker: `docker system prune -a --volumes`
- [ ] Verify correct domain in `nginx/nginx.conf`
- [ ] Verify no volumes from older versions `docker volume ls`
- [ ] Verify TZ is correct in all Dockerfiles (nginx/web)
- [ ] Database credentials: Set new credentials in `db/db_conn.env`
- [ ] Configure .env taken from `prod.env`:
  * Generate new `SECRET_KEY`
  * Restrict Allowed Hosts
  * Set admin details
  
### Base Installation
- [ ] Run containers : `docker-compose up --build -d`
- [ ] Verify status: `docker ps -a`, `docker-compose logs -f`

### TLS letsencrypt
In the nginx container, `docker exec -it nginx sh`, run: `certbot --nginx -d sharpa.live -d www.sharpa.live --agree-tos -m sharp.imsystem@gmail.com`
A new configuration is written in `/etc/nginx/nginx`.
Test renewal with `certbot renew --dry-run`.
If OK, add the following cronjob: `0 6 * * * certbot renew --post-hook "nginx -s reload"`

### Post Installation
- [ ] Add superuser : `docker exec -it django-ims bash', then inside the container `python manage.py createsuperuser`


# Maintenance
### Updating the application
- Make the update in code
- `docker-compose up --build -d`, unchanged containers are left unchanged.

### Reloading nginx
- Reload nginx: `docker exec nginx "nginx -s reload"`
- If the container restarted, need to reconfigure the TLS. Just run again `certbot --nginx -d sharpa.live -d www.sharpa.live --agree-tos -m sharp.imsystem@gmail.com` and choose to reuse the existing certificates (persisted in the letsencrypt volume).


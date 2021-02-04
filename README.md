# Installation

### Preparation
- [ ] **Optional** clean up everything related to docker: `docker system prune -a --volumes`
- [ ] Verify correct domain in `nginx/nginx.conf`
- [ ] Verify no volumes from older versions `docker volume ls`
- [ ] Verify TZ is correct in all Dockerfiles (nginx/web)
- [ ] Set domain name in `postfix/postfix.env`
- [ ] Database credentials: Set new credentials in `db/db_conn.env`
- [ ] Configure .env taken from `prod.env`:
  * Generate new `SECRET_KEY`
  * Restrict Allowed Hosts
  * Set admin details `ADMIN_NAME`, `ADMIN_EMAIL`, `SERVER_EMAIL`
  * Set new GPG passphrase `DBBACKUP_GPG_PASSPHRASE`
  
### Base Installation
- [ ] Run containers : `docker-compose up --build -d`
- [ ] Verify status: `docker ps -a`, `docker-compose logs -f`

### TLS letsencrypt
In the nginx container, `docker exec -it nginx sh`, run: `certbot --nginx -d sharpa.live -d www.sharpa.live --agree-tos -m sharp.imsystem@gmail.com` (persisted in letsencrypt volume)
A new configuration is written in `/etc/nginx/nginx`.
Test renewal with `certbot renew --dry-run`.
If OK, add the following cronjob: `0 6 * * * certbot renew --post-hook "nginx -s reload"`


### Backup system
- [ ] In the web container, generate new GPG keys with `scripts/gen_pgp_key.py` (persisted in gpginfrastructure volume).
- [ ] Install and configure rclone
    * On client machine, `rclone config`, select drive, keep default options to do oauth via browser
    * Copy drive configuration file to web container /root/.config/rclone/rclone.conf. Test with `rclone about "drive:`
- [ ] Test by running `run_backup.sh -r`, `restore_backup.sh`
- [ ] On host machine, configure cron job for `run_backup.sh`
        ```
        MAILTO=sharp.imsystem@gmail.com
        * 4 * * * /usr/bin/docker exec django-ims /app/web/scripts/run_backup.sh 2>&1
        ```
- [ ] On host configure TZ: `sudo timedatectl set-timezone Europe/Brussels`


### Post Installation
- [ ] Add superuser : `docker exec -it django-ims bash', then inside the container `python manage.py createsuperuser`


# Maintenance
### Updating the application
- Make the update in code
- `docker-compose up --build -d`, unchanged containers are left unchanged.

### Reloading nginx
- Reload nginx: `docker exec nginx "nginx -s reload"`
- If the container restarted, need to reconfigure the TLS. Just run again `certbot --nginx -d sharpa.live -d www.sharpa.live --agree-tos -m sharp.imsystem@gmail.com` and choose to reuse the existing certificates (persisted in the letsencrypt volume).


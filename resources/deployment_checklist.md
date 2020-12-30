### Install app
- [ ] Set up virtual env and install requirements
- [ ] Set up media directory
- [ ] Set up static directory and collect statics  
- [ ] Configure .env
  * Generate new `SECRET_KEY`
  * Confirm `DEBUG=False`
  * Restrict Allowed Hosts
  * Set `STATIC_ROOT` and `STATIC_MEDIA`
    
### Configure web server and HTTPS
- [ ] Configure apache2 TODO
- [ ] Configure .env
   * Set `SECURE_SSL_REDIRECT=True`, `SECURE_HSTS_SECONDS=`, `SECURE_HSTS_INCLUDE_SUBDOMAINS=True`
    
### Configure mailing system
- [ ] Configure mail server TODO
- [ ] Configure SMTP connection in .env 
      * Confirm `ADMIN_EMAIL="sharp.imsystem@gmail.com` and `SERVER_EMAIL="noreply@sharpa.live"`

### Configure backup system
- [ ] Set up PGP keys **with new passphrase** for backup (_c.f gen_pgp_key.py_)
- [ ] Set `PROJ_ROOT_DIR` in restore_backup.sh and run_backup.sh
- [ ] Configure backup directory
- [ ] Install and configure rclone
    * On client machine, `rclone config`, select drive, keep default options to do oauth via browser
    * Copy drive configuration file to server
    * Test with `rclone about "drive:`
- [ ] Configure .env
    * Set `DBBACKUP_STORAGE_LOCATION`
    * Set `DBBACKUP_GPG_PASSPHRASE`
    * Confirm `ADMIN_EMAIL="sharp.imsystem@gmail.com"` (same as for PGP key)
- [ ] Configure cron job for `run_backup.sh`
- Test by running run_backup.sh

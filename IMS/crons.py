from django.core import management
from django_cron import CronJobBase, Schedule
from django.conf import settings

"""
Usage : crontab -e
*/5 * * * * source /home/ubuntu/project/venv/bin/activate && python3 /home/ubuntu/project/project/manage.py runcrons > /home/ubuntu/cronjob.log
"""


class BackupCron(CronJobBase):
    RUN_AT_TIMES = ['4:00', '22:16']
    MIN_NUM_FAILURES = 2

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'ims.backup'

    def do(self):
        print(self.RUN_AT_TIMES)
        management.call_command('dbbackup', '--clean', '--compress')
        management.call_command('mediabackup', '--clean', '--compress')

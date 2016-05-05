from django_cron import CronJobBase, Schedule


class CronCurrencyJob(CronJobBase):
    RUN_EVERY_MINS = 720

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'configuration.get_cbr_info'


class CronBordereauJob(CronJobBase):
    RUN_EVERY_MINS = 1400

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'configuration.get_bordereau'

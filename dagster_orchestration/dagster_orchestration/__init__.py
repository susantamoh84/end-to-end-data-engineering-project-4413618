from dagster import Definitions, load_assets_from_modules

from .assets import resources

from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

# Define a job that will materialize the assets
my_dagster_job = define_asset_job("my_dagster_job", selection=AssetSelection.all())

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
my_job_schedule = ScheduleDefinition(
    job=my_dagster_job,
    cron_schedule="0 * * * *",  # every hour
)

defs = Definitions(assets=load_assets_from_modules(
    [assets]), resources=resources, jobs=[my_dagster_job], schedules=[my_job_schedule])
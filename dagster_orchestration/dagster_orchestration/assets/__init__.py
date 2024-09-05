import os
from dagster_dbt import DbtCliResource, DbtProject, dbt_assets

from dagster_airbyte import AirbyteResource
from dagster_airbyte import load_assets_from_airbyte_instance

from dagster import AssetExecutionContext

from pathlib import Path

resources = {
    "dbt": DbtCliResource(
        project_dir=os.getenv("DBT_PROJECT_DIR"),
        profiles_dir=os.getenv("DBT_PROFILES_DIR"),
    ),
    "airbyte_instance": AirbyteResource(
        host="localhost",
        port="8000",
        # If using basic auth, include username and password:
        username="airbyte",
        password=os.getenv("AIRBYTE_PASSWORD")
    )
}

my_dbt_project = DbtProject(project_dir=Path(os.getenv("DBT_PROJECT_DIR")))


@dbt_assets(manifest=my_dbt_project.manifest_path)
def my_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    
airbyte_assets = load_assets_from_airbyte_instance(
    resources.get("airbyte_instance"), key_prefix=["RawDataset"])
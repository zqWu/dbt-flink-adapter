import os

import pytest

from tests.sqlgateway.mock.mock_client import MockFlinkSqlGatewayClient

# import json

# Import the fuctional fixtures as a plugin
# Note: fixtures with session scope need to be local

pytest_plugins = ["dbt.tests.fixtures.project"]


# The profile dictionary, used to write out profiles.yml
@pytest.fixture(scope="class")
def dbt_profile_target():
    profile = {
        'type': 'flink',
        'threads': 1,
        'host': os.getenv('FLINK_SQL_GATEWAY_HOST', '127.0.0.1'),
        'port': int(os.getenv('FLINK_SQL_GATEWAY_PORT', '8083')),
        'session_name': os.getenv('SESSION_NAME', 'test_session'),
        'database': os.getenv('DATABASE_NAME', 'default_catalog'),
        'schema': os.getenv('DATABASE_NAME', 'default_database'),
    }

    # we need setup MockFlinkSqlGatewayClient
    MockFlinkSqlGatewayClient.create_session(
        host=profile.get("host"),
        port=profile.get("port"),
        session_name=profile.get("session_name"),
    )

    return profile

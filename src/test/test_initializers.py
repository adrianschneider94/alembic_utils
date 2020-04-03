from alembic_utils import TEST_RESOURCE_ROOT, PGFunction
from alembic_utils.testbase import run_alembic_command


def test_pg_function_from_file() -> None:
    """Test that the alembic current command does not erorr"""
    # Runs with no error
    SQL_PATH = TEST_RESOURCE_ROOT / "to_upper.sql"
    func = PGFunction.from_path(SQL_PATH)
    assert func.schema == "public"


def test_pg_function_from_sql_file_valid() -> None:
    SQL = """
CREATE OR REPLACE FUNCTION public.to_upper(some_text text)
RETURNS TEXT AS
$$
    SELECT upper(some_text)
$$ language SQL;
    """

    func = PGFunction.from_sql(SQL)
    assert func.schema == "public"


def test_pg_function_from_sql_file_invalid() -> None:
    SQL = """
    NO VALID SQL TO BE FOUND HERE
    """
    func = PGFunction.from_sql(SQL)
    assert func is None
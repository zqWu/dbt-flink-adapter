import unittest

from flink.sqlgateway.result_parser import SqlGatewayResultParser, SqlGatewayResult

sample_input = {
    "results": {
        "columns": [
            {
                "name": "id",
                "logicalType": {
                    "type": "BIGINT",
                    "nullable": True
                },
                "comment": None
            },
            {
                "name": "content",
                "logicalType": {
                    "type": "VARCHAR",
                    "nullable": True,
                    "length": 2147483647
                },
                "comment": None
            }
        ],
        "data": [
            {
                "kind": "INSERT",
                "fields": [
                    1,
                    "aaa"
                ]
            }
        ]
    },
    "resultType": "PAYLOAD",
    "nextResultUri": "/v1/sessions/1c20ff6b-b060-49a6-b311-3210ba766b65/operations/84313330-bf20-4b87-bfc2-7b629908866d/result/1"
}


class SqlGatewayResultParserTest(unittest.TestCase):
    def test_parser(self):
        result: SqlGatewayResult = SqlGatewayResultParser.parse_result(sample_input)
        self.assertEqual(1, len(result.rows), "Number of rows should be 2")
        self.assertEqual(result.next_result_url, "/v1/sessions/1c20ff6b-b060-49a6-b311-3210ba766b65/operations/84313330-bf20-4b87-bfc2-7b629908866d/result/1")
        self.assertEqual(1, result.rows[0]["id"], "ID column of the first row should be = 1")
        self.assertEqual("aaa", result.rows[0]["content"], "ID column of the first row should be = 'aaa'")


if __name__ == '__main__':
    unittest.main()

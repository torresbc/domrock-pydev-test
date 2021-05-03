import pandas as pd

from src import main


class TestMain:
    @classmethod
    def setup_class(cls):
        cls.df_balance = pd.DataFrame(
            {
                "item": ["80.03.104-1", "80.03.104-2"],
                "data_inicio": [pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                pd.to_datetime("1/1/1900", format="%m/%d/%Y")],
                "qtd_inicio": [100, 100],
                "valor_inicio": [10000, 10000],
                "data_final": [pd.to_datetime("1/4/1900", format="%m/%d/%Y"),
                               pd.to_datetime("1/4/1900", format="%m/%d/%Y")],
                "qtd_final": [120, 110],
                "valor_final": [12000, 10000]
            }
        )

        cls.df_mov = pd.DataFrame(
            {
                "item": ["80.03.104-1", "80.03.104-1", "80.03.104-2",
                         "80.03.104-2", "80.03.104-2"],
                "tipo_movimento": ["Ent", "Ent", "Ent", "Sai", "Sai"],
                "data_lancamento": [pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/3/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/4/1900", format="%m/%d/%Y")],
                "quantidade": [10, 10, 10, 5, 5],
                "valor": [1000, 1000, 1000, 500, 500]
            }
        )

        cls.df_mov_grouped = pd.DataFrame(
            {
                "item": ["80.03.104-1", "80.03.104-2",
                         "80.03.104-2", "80.03.104-2"],
                "tipo_movimento": ["Ent", "Ent", "Sai", "Sai"],
                "data_lancamento": [pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/3/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/4/1900", format="%m/%d/%Y")],
                "quantidade": [20, 10, 5, 5],
                "valor": [2000, 1000, 500, 500]
            }
        )

        cls.df_mov_pivot = pd.DataFrame(
            {
                "item": ["80.03.104-1", "80.03.104-2",
                         "80.03.104-2", "80.03.104-2"],
                "data_lancamento": [pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/3/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/4/1900", format="%m/%d/%Y")],
                "quantidade_Ent": [20., 10, 0, 0],
                "quantidade_Sai": [0., 0, 5, 5],
                "valor_Ent": [2000., 1000, 0, 0],
                "valor_Sai": [0., 0, 500, 500],
            }
        )

        cls.df_merge = pd.DataFrame(
            {
                "item": ["80.03.104-1", "80.03.104-2",
                         "80.03.104-2", "80.03.104-2"],
                "data_lancamento": [pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/3/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/4/1900", format="%m/%d/%Y")],
                "quantidade_Ent": [20., 10, 0, 0],
                "quantidade_Sai": [0., 0, 5, 5],
                "valor_Ent": [2000., 1000, 0, 0],
                "valor_Sai": [0., 0, 500, 500],
                "item": ["80.03.104-1", "80.03.104-2", "80.03.104-2", "80.03.104-2"],
                "data_inicio": [pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                pd.to_datetime("1/1/1900", format="%m/%d/%Y")],
                "qtd_inicio": [100, 100, 100, 100],
                "valor_inicio": [10000, 10000, 10000, 10000],
                "data_final": [pd.to_datetime("1/4/1900", format="%m/%d/%Y"),
                               pd.to_datetime("1/4/1900", format="%m/%d/%Y"),
                               pd.to_datetime("1/4/1900", format="%m/%d/%Y"),
                               pd.to_datetime("1/4/1900", format="%m/%d/%Y")],
                "qtd_final": [120, 110, 110, 110],
                "valor_final": [12000, 10000, 10000, 10000]

            }
        )

        cls.df_filter = pd.DataFrame(
            {
                "item": ["80.03.104-1", "80.03.104-2",
                         "80.03.104-2", "80.03.104-2"],
                "data_lancamento": [pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/3/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/4/1900", format="%m/%d/%Y")],
                "quantidade_Ent": [20., 10, 0, 0],
                "valor_Ent": [2000., 1000, 0, 0],
                "quantidade_Sai": [0., 0, 5, 5],
                "valor_Sai": [0., 0, 500, 500],
                "qtd_inicio": [100, 100, 100, 100],
                "valor_inicio": [10000, 10000, 10000, 10000],
                "qtd_final": [120, 110, 110, 110],
                "valor_final": [12000, 10000, 10000, 10000]
            }
        )

        cls.df_normalize = pd.DataFrame(
            {
                "item": ["80.03.104-1", "80.03.104-2",
                         "80.03.104-2", "80.03.104-2"],
                "data_lancamento": [pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/1/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/3/1900", format="%m/%d/%Y"),
                                    pd.to_datetime("1/4/1900", format="%m/%d/%Y")],
                "quantidade_Ent": [20., 10, 0, 0],
                "valor_Ent": [2000., 1000, 0, 0],
                "quantidade_Sai": [0., 0, 5, 5],
                "valor_Sai": [0., 0, 500, 500],
                "qtd_inicio": [100, 100, 100, 100],
                "valor_inicio": [10000, 10000, 10000, 10000],
                "qtd_final": [120, 110, 110, 110],
                "valor_final": [12000, 10000, 10000, 10000]
            }
        )

    def test_read_excel_file(self):
        path = f"../tests/sample_saldo.xlsx"
        response = main.read_excel_file(path)
        pd.testing.assert_frame_equal(response, self.df_balance)

        path = f"../tests/sample_movto.xlsx"
        response = main.read_excel_file(path)
        pd.testing.assert_frame_equal(response, self.df_mov)

    def test_group_daily(self):
        group = {
            "columns": ["item", "tipo_movimento", "data_lancamento"],
            "sum": ["quantidade", "valor"]
        }

        response = main.group_daily(self.df_mov, **group)
        pd.testing.assert_frame_equal(response, self.df_mov_grouped)

    def test_pivot_tables(self):
        pivot = {
            "index": ["item", "data_lancamento"],
            "columns": "tipo_movimento",
            "values": ["quantidade", "valor"],
            "aggfunc": "sum"
        }

        response = main.pivot_tables(self.df_mov_grouped, **pivot)
        pd.testing.assert_frame_equal(response, self.df_mov_pivot)

    def test_merge_tables(self):
        response = main.merge_tables(self.df_mov_pivot, self.df_balance, "item", "item")
        pd.testing.assert_frame_equal(response, self.df_merge)

    def test_filter_columns(self):
        columns = ["item", "data_lancamento", "quantidade_Ent", "valor_Ent", "quantidade_Sai", "valor_Sai",
                    "qtd_inicio", "valor_inicio", "qtd_final", "valor_final"]

        response = main.filter_columns(self.df_merge, columns)
        pd.testing.assert_frame_equal(response, self.df_filter)

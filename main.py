from pyarrow import csv, parquet
import os
from subprocess import Popen
import glob
import tempfile


def convert_file_csv_to_parquet(local_file: str, encoding: str = 'utf8', compression: str = 'BROTLI', autogenerate_column_names: bool = False, delimiter: str = ';') -> None:
    """
    Description: Essa rotina convert os arquivos .csv em parquet

    :param local_file: str: local do arquivo .csv que será convertido
    :param encoding: str: enconding do arquivo, ser não for informado ele deverá pegar o enconding padrão UTF-8
    :param compression: str: Tipo de compressão do arquivo .parquet, os tipos de compactação são (parquet, gzip e brotli)
    :param autogenerate_column_names: bool: São para os arquivos .csv que não tem o cabeçalho do registro
    :param delimiter: str: Especificação do delimitador do arquivo .csv, caso não seja enviado ele irá utilizar o ';'
    """
    try:

        tmp_folder = tempfile.mkdtemp()

        parquet_file = os.path.splitext(local_file)[0]

        temp_file = local_file


        if len(temp_file) > 0:

            parse_options = csv.ParseOptions(delimiter=delimiter)
            data_arrow = csv.read_csv(temp_file, parse_options=parse_options, read_options=csv.ReadOptions(autogenerate_column_names=autogenerate_column_names, encoding=encoding))

            compression = str(compression).upper()

            if compression == 'GZIP':
                extensao_arquivo = '.gzip'
            elif compression == 'BROTLI':
                extensao_arquivo = '.brotli'
            else:
                extensao_arquivo = '.parquet'

            parquet.write_table(data_arrow, parquet_file + extensao_arquivo, compression=compression)

        else:
            raise Exception(f"A lista de arquivos está vazia, não conseguiu listar os arquivos da pasta {tmp_folder}")

    except Exception as error:
        raise Exception(f"Ocorreu um erro ao tentar converter o arquivo {local_file} para '{compression}'. MSG: {error}")


if __name__ == '__main__':
    convert_file_csv_to_parquet(local_file= r'C:\Users\Francisco\Downloads\file.csv', encoding='latin1',
                                compression= 'BROTLI', autogenerate_column_names= True, delimiter = ';')


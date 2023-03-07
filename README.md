<h1 align="center">
    🔗 Convert CSV para parquet/brotli
</h1>
<p align="center">🚀 Função usada para converter arquivos no formato .csv para brotli, essa rotina compacta os arquivos ao máximo e isso ajuda no armazenamento em DataLakes</p>

```bash
pip install pyarrow
```

## Como usar
```python
convert_file_csv_to_parquet(local_file= <path_file>, encoding='latin1',
                                compression= 'BROTLI', autogenerate_column_names= True, delimiter = ';')
```

## Licença

[MIT](https://choosealicense.com/licenses/mit/)

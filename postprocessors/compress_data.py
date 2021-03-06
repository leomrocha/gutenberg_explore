import gzip
import os

# TODO: merge with aggregate script

for file_name in os.listdir('data/gitignored/aggregate/by_language/'):
    with open(f'data/gitignored/aggregate/by_language/{file_name}', mode='rb') as source:
        with gzip.open(f'data/aggregate/by_language/{file_name}.gz', mode="wb") as target:
            target.write(source.read())

for language in os.listdir('data/gitignored/aggregate/by_author/'):
    for file_name in os.listdir(f'data/gitignored/aggregate/by_author/{language}/'):
        with open(f'data/gitignored/aggregate/by_author/{language}/{file_name}', mode='rb') as source:
            os.makedirs(f'data/aggregate/by_author/{language}/', exist_ok=True)
            with gzip.open(f'data/aggregate/by_author/{language}/{file_name}.gz', mode="wb") as target:
                target.write(source.read())
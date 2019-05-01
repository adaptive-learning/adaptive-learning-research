import os
import pandas as pd

# TODO: Fix the path (relative to this file, not the caller).
DATA_DIR = '../data/'

# TODO: Return a custom Dataset type to provide util methods.
def load(name, download=True, **kwargs):
    """Load a dataset of given name.

    Args:
        name: Identifier of the dataset.
        download: Whether to download the dataset (if it wasn't before).

    Return:
        Dataset containing all tables as pd.DataFrames

    >>> dataset = load('robomission-2018-10-27', nrows=10)
    >>> dataset['tasks'].head(2)
                       name  ...
    id                       ...
    51  three-steps-forward  ...
    49        turning-right  ...

    """
    # TODO: DRY mapping between dataset names and classes
    available_datasets = {
        'robomission-2018-10-27': RoboMission2018Dataset,
    }
    if name not in available_datasets:
        raise Exception(f'Unknown dataset "{name}"')
    return available_datasets[name](download=download, **kwargs)


class Dataset:
    def __init__(self, download=True, **kwargs):
        dataset_dir = os.path.join(DATA_DIR, self.name)
        # TODO: Download the data if not cached.
        self._tables = {}
        for table_name, options in self.tables_options.items():
            path = os.path.join(dataset_dir, table_name + '.csv')
            self._tables[table_name] = pd.read_csv(path, **options, **kwargs)
        # TODO: Postprocessing (setting-json.loads (convertors?),
        # program.fillna, imputation).

    def getcopy(self, key):
        return self._tables[key].copy()

    def __getitem__(self, key):
        return self._tables[key]

    #if name == 'tasks':
    #    df['setting'] = df.setting.map(json.loads)
    #if 'program' in df.columns:
    #    df.program.fillna('', inplace=True)
    #


class RoboMission2018Dataset(Dataset):
    name = 'robomission-2018-10-27'
    tables_options = {
        'program_snapshots': {'index_col': 'id', 'parse_dates': ['time']},
        'task_sessions':  {'index_col': 'id', 'parse_dates': ['start', 'end']},
        'tasks': {'index_col': 'id'},
        'problemsets': {'index_col': 'id'},
    }

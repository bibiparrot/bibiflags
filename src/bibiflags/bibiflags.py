'''
supported yaml with absl.flags.argparse_flags.ArgumentParser and argparse.ArgumentParser

# from absl.flags import argparse_flags
# parser = argparse_flags.ArgumentParser()

'''
import argparse
import builtins
import inspect
import os
import pathlib
from collections import OrderedDict
from pprint import pformat
import logging
import yaml

logger = logging.getLogger(__name__)


class BibiFlags:
    names = [
        'dest',
        'type',
        'const',
        'default',
        'option_strings',
        'help',
        'required',
        'nargs',
        'choices',
        'metavar',
    ]

    def __init__(self,
                 flags_path: str = None,
                 argparser: argparse.ArgumentParser = None,
                 app_name: str = None,
                 root: str = None,
                 key: str = 'flags',
                 encoding: str = 'UTF8'):
        '''

        :param flags_path:  the path of app_name.yaml
        :param argparser:  existing argparser which will be merged together
        :param app_name:  find default app_name.yaml when flags_path is None
        :param root: the directory to find app_name.yaml
        :param key: default root key for in  app_name.yaml
        :param encoding: encoding of app_name.yaml, default is UTF8
        '''
        _argparser = argparser if argparser is not None else argparse.ArgumentParser()
        app_name_ = app_name if app_name is not None else pathlib.Path(inspect.stack()[1][0].f_code.co_filename).stem
        self.app_name = app_name_
        if root is None:
            try:
                root = pathlib.Path(__file__).parent
            except NameError:
                # __file__ is not set
                root = pathlib.Path('.')
        self.root = root
        logger.info(f'root: {self.root}')
        if flags_path is None:
            self.app_flags_path = pathlib.Path(self.root).joinpath(f'{self.app_name}.yaml')
        else:
            self.app_flags_path = pathlib.Path(self.root).joinpath(flags_path)
        logger.info(f'app_flags_path: {self.app_flags_path}')
        if self.app_flags_path.exists():
            _argparser = self.from_yaml(str(self.app_flags_path), _argparser, encoding=encoding, key=key)
        else:
            self.to_yaml(_argparser, self.app_flags_path, encoding=encoding, key=key)
        self._argparser = _argparser
        self._argparser.parse_args()
        logger.info(f'app_name: {self.app_name}, key: {key}, parameters: {self.parameters}')

    @property
    def parameters(self):
        return vars(self._argparser.parse_args())

    @property
    def argparser(self):
        return self._argparser

    @staticmethod
    def to_yaml(argparser: argparse.ArgumentParser,
                yaml_file,
                encoding: str = 'utf-8',
                key='ArgumentParser'):
        flags = []
        for action in argparser._actions:
            flag = OrderedDict()
            suppressed = False
            for name in BibiFlags.names:
                val = getattr(action, name)
                if val == '==SUPPRESS==':
                    suppressed = True
                if name == 'type':
                    if val is None:
                        flag[name] = 'bool'  # default bool
                    else:
                        flag[name] = val.__name__
                elif val is not None:
                    flag[name] = val
            if len(flag) > 0 and not suppressed:
                flags.append(flag)
        config = dict()
        config[key] = flags
        BibiFlags.yaml_dump(config, yaml_file, encoding=encoding)
        # with open(yaml_file, 'w', encoding=encoding) as fp:
        #     OmegaConf.save(config=config, f=fp)

    @staticmethod
    def contains_yaml(yaml_file: str, encoding='utf-8', key='ArgumentParser'):
        # with open(yaml_file, 'r', encoding=encoding) as fp:
        #     config = OmegaConf.load(fp)
        config = BibiFlags.yaml_load(yaml_file, encoding=encoding)
        return key in config

    @staticmethod
    def from_yaml(yaml_file: str, parser=None, encoding='utf-8', key='ArgumentParser') -> argparse.ArgumentParser:
        # with open(yaml_file, 'r', encoding=encoding) as fp:
        #     config = OmegaConf.load(fp)
        #     config = OmegaConf.to_object(config)
        config = BibiFlags.yaml_load(yaml_file, encoding=encoding)
        logger.info(pformat(config))
        items = config.get(key, [])
        if len(items) == 0:
            logger.warning(f"Flags {key} NOT in {os.path.abspath(yaml_file)}")
        parser = argparse.ArgumentParser() if parser is None else parser
        for item in items:
            if item.get('type', 'str') == 'bool':
                item['type'] = None
            else:
                item['type'] = getattr(builtins, item.get('type', 'str'))
            if item.get('option_strings', None):
                action = argparse.Action(**item)
            else:
                item['option_strings'] = []
                action = argparse._StoreAction(**item)
            if action.dest not in [_action.dest for _action in parser._actions]:
                parser._add_action(action)
            else:
                logger.warning(f"CONFLICT ARGS '{action.dest}', NOT USED {os.path.abspath(yaml_file)}")
        return parser

    @staticmethod
    def yaml_dump(data, yamlfile=None, Dumper=yaml.SafeDumper,
                  encoding: str = 'utf-8', **kwds):
        class OrderedDumper(Dumper):
            pass

        def _dict_representer(dumper, data):
            return dumper.represent_mapping(
                yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                data.items())

        OrderedDumper.add_representer(OrderedDict, _dict_representer)
        with open(yamlfile, 'w', encoding=encoding) as stream:
            return yaml.dump(data, stream, OrderedDumper, **kwds)

    @staticmethod
    def yaml_load(yamlfile, Loader=yaml.Loader,
                  object_pairs_hook=OrderedDict,
                  encoding: str = 'utf-8'):
        class OrderedLoader(Loader):
            pass

        def construct_mapping(loader, node):
            loader.flatten_mapping(node)
            return object_pairs_hook(loader.construct_pairs(node))

        OrderedLoader.add_constructor(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            construct_mapping)
        with open(yamlfile, 'r', encoding=encoding) as stream:
            return yaml.load(stream, OrderedLoader)

    @staticmethod
    def _load_yaml_file(fp, config):
        pass

    @staticmethod
    def _save_yaml_file(config, fp):
        pass

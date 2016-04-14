import config


__all__ = [
    'get_config',
]


def get_config(key, default=None):
    """
    Get config from config module if exists,
    return default value otherwise
    """
    return getattr(config, key, default)

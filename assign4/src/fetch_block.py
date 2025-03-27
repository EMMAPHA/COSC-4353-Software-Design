import importlib

def fetch_block(block_name):
    return getattr(importlib.import_module(f"src.blocks.{block_name}"), block_name)

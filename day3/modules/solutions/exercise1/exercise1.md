1. Move to a different directory or move your script to a different directory (such that you can no longer import the module).
2. Modify the `PYTHONPATH` environment variable to add the location of your module to the list in `sys.path`.
    - export PYTHONPATH=/some/path/to/module
3. Ensure you can import/run the function in your module.

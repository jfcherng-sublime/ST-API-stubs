# Sublime Text API Stubs

With LSP properly configured and type annotations provided, you can have something like the following screenshot.

![LSP and pyright](https://raw.githubusercontent.com/jfcherng-sublime/ST-api-stubs/master/docs/with-pyright.png)

You can also use these stub files in [mypy][gh-mypy] to do static analysis for your plugin.

## How to Use Them

### Setup for [LSP-pyright][pc-lsp-pyright]

1. Configure the `pyright.dev_environment`:

   ST stubs have been bundled in `LSP-pyright` so you just have to activate the setup.

   ```js
   {
       "settings": {
           // a special predefined setup for developing ST plugins
           "pyright.dev_environment": "sublime_text",
       },
   }
   ```

1. Restart the language server (by restarting ST).

### Setup for [LSP-pylsp][pc-lsp-pylsp]

1. Copy `typings/` from this repository to `YOUR_PROJECT_ROOT/typings/` directory.
1. Make the language server able to see them.

   Configure the `pylsp.plugins.jedi.extra_paths`:

   ```js
   {
       "settings": {
           "pylsp.plugins.jedi.extra_paths": [
               // $folder is the first project folder in your ST project folders
               "$folder/typings",
           ],
       },
   }
   ```

1. Restart the language server (by restarting ST).

### Setup for [mypy][gh-mypy]

1. Copy `typings/` from this repository as `YOUR_PROJECT_ROOT/typings/` directory.
1. In your `mypy.ini`, in the `[mypy]` section, set the stub directories.

   ```ini
   [mypy]
   mypy_path = typings:stubs
   ```

1. `mypy` should be able to understand `sublime` and `sublime_plugin` modules now.

## Acknowledgment and Related Resources

This repository is initially mostly based on [AmjadHD/sublime_dev](https://github.com/AmjadHD/sublime_dev)'s work.

Apart from [@AmjadHD](https://github.com/AmjadHD)'s work, there are also some other similar works:

- https://github.com/sublimelsp/LSP/tree/st4000-exploration/stubs
- https://github.com/SublimeText/sublime_lib/tree/master/stubs

[gh-mypy]: https://github.com/python/mypy
[pc-lsp-pylsp]: https://packagecontrol.io/packages/LSP-pylsp
[pc-lsp-pyright]: https://packagecontrol.io/packages/LSP-pyright
[pc-lsp]: https://packagecontrol.io/packages/LSP

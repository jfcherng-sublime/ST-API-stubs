# Sublime Text API Stubs

With LSP proper configured, you can have something like the following screenshot.

![LSP properly configured](https://raw.githubusercontent.com/jfcherng-sublime/ST-api-stubs/master/docs/with-lsp.png)

## How to use

I personally use this with [LSP](https://packagecontrol.io/packages/LSP) + `a Python LSP server` setup.

1. First, you have to clone (or copy) this repository to wherever you like. I clone it into ST's `Data/` directory like [this](https://github.com/jfcherng-sublime/ST-my-settings/tree/210e269b56bc9a7903bf75d99fc799b28e0e25ee). Put it in `Data/` allows you to sync this stubs along with settings but it's not necessary.

1. Second, make your preferred LSP server able to "see" it.
   Note that LSP will expand some variables in settings such as
   `$packages` means the `Packages/` so `$packages/../` is the `Data/`.

   - If you use `pyls`, configure the `pyls.plugins.jedi.extra_paths`:

     ```js
     {
         "clients": {
             "pyls": {
                 "enabled": true,
                 "command": [
                     "pyls",
                 ],
                 "settings": {
                     "pyls.plugins.jedi.extra_paths": [
                         // for ST plugin development
                         "$packages/../st-stubs",
                     ],
                 },
             },
         },
     }
     ```

   - If you use [LSP-pyright](https://packagecontrol.io/packages/LSP-pyright), configure the `python.analysis.extraPaths`:

     ```js
     {
         "settings": {
             "python.analysis.extraPaths": [
                 // For Sublime Text plugin development
                 "$packages/../st-stubs",
                 "$sublime_py_files_dir",
                 "$packages",
             ],
         },
     }
     ```

1. Third, restart your ST and happy coding ♥

## Acknowledgment and related resources

This repository is mostly based on [AmjadHD/sublime_dev](https://github.com/AmjadHD/sublime_dev)'s work.

Apart from [@AmjadHD](https://github.com/AmjadHD)'s work, there are also some other similar works:

- https://github.com/sublimelsp/LSP/tree/master/stubs
- https://github.com/SublimeText/sublime_lib/tree/master/stubs

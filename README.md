# Sublime Text API Stubs

With LSP proper configured, you can have something like the following screenshot.

![LSP and pyls](https://raw.githubusercontent.com/jfcherng-sublime/ST-api-stubs/master/docs/with-pyls.png)

## How to Use

I personally use this with [LSP][pc-lsp] + [LSP-pyright][pc-lsp-pyright] / [LSP-pylance][private-lsp-pylance] setup.

1. Install the [LSP][pc-lsp] package via Package Control.
1. You have to copy those `.pyi` stub files from this repository to `YOUR_PROJECT_ROOT/typings/` directory.
1. Make your preferred LSP server able to "see" them.

   - If you use [LSP-pyright][pc-lsp-pyright] / [LSP-pylance][private-lsp-pylance],
     configure the `python.analysis.extraPaths`:

     ```js
     {
         "settings": {
             "python.analysis.extraPaths": [
                 // my custom stubs
                 "$packages/../typings",
                 // project's stubs
                 "$folder/typings",
             ],
         },
         // a special predefined setup for developing ST plugins
         "dev_environment": "sublime_text",
     }
     ```

   - If you use [LSP-pyls][gh-lsp-pysl], configure the `pyls.plugins.jedi.extra_paths`:

     ```js
     {
         "settings": {
             "pyls.plugins.jedi.extra_paths": [
                 // my custom stubs
                 "$packages/../typings",
                 // project's stubs
                 "$folder/typings",
             ],
         },
     }
     ```

1. Restart your ST and happy coding ♥

## Acknowledgment and Related Resources

This repository is initially mostly based on [AmjadHD/sublime_dev](https://github.com/AmjadHD/sublime_dev)'s work.

Apart from [@AmjadHD](https://github.com/AmjadHD)'s work, there are also some other similar works:

- https://github.com/sublimelsp/LSP/tree/st4000-exploration/stubs
- https://github.com/SublimeText/sublime_lib/tree/master/stubs

[gh-lsp-pysl]: https://github.com/sublimelsp/LSP-pyls
[pc-lsp-pyright]: https://packagecontrol.io/packages/LSP-pyright
[pc-lsp]: https://packagecontrol.io/packages/LSP
[private-lsp-pylance]: https://github.com/jfcherng-sublime/LSP-pylance

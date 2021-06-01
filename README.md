# Sublime Text API Stubs

With LSP proper configured, you can have something like the following screenshot.

![LSP and pyright](https://raw.githubusercontent.com/jfcherng-sublime/ST-api-stubs/master/docs/with-pyright.png)

## How to Use

I personally use this with [LSP][pc-lsp] + [LSP-pyright][pc-lsp-pyright] setup.

1. Install the [LSP][pc-lsp] package via Package Control.
1. You have to copy those `.pyi` stub files from this repository to `YOUR_PROJECT_ROOT/typings/` directory.
1. Make your preferred LSP server is able to "see" them.

   - If you use [LSP-pyright][pc-lsp-pyright],
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

   - If you use [LSP-pylsp][pc-lsp-pylsp], configure the `pylsp.plugins.jedi.extra_paths`:

     ```js
     {
         "settings": {
             "pylsp.plugins.jedi.extra_paths": [
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

[pc-lsp-pylsp]: https://packagecontrol.io/packages/LSP-pylsp
[pc-lsp-pyright]: https://packagecontrol.io/packages/LSP-pyright
[pc-lsp]: https://packagecontrol.io/packages/LSP

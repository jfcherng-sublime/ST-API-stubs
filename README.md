# Sublime Text API Stubs

With LSP proper configured, you can have something like the following screenshot.

![LSP and pyls](https://raw.githubusercontent.com/jfcherng-sublime/ST-api-stubs/master/docs/with-pyls.png)

## How to use

I personally use this with [LSP](https://packagecontrol.io/packages/LSP) + `Python LSP server` setup.

1. Install the [LSP](https://packagecontrol.io/packages/LSP) package via Package Control.
1. You have to clone (or copy) this repository to wherever you like. I clone it into ST's `Data/` directory like [this](https://github.com/jfcherng-sublime/ST-my-settings/tree/280184443caf95a96cab103c1827b8f3fd41f1f9). Put it in `Data/` allows you to sync this stubs along with settings but it's not necessary.

1. Make your preferred LSP server able to "see" it.
   Note that LSP will expand some variables in settings such as
   `$packages` means the `Packages/` so `$packages/../` is the `Data/`.

   - If you use [LSP-pyls](https://github.com/sublimelsp/LSP-pyls),
     configure the `pyls.plugins.jedi.extra_paths`:

     ```js
     {
         "settings": {
             "pyls.plugins.jedi.extra_paths": [
                 // add jfcherng-sublime/ST-API-stubs
                 "$packages/../st-stubs",
                 // the followings come from the default settings
                 "$sublime_py_files_dir",
                 "$packages",
             ],
         },
     }
     ```

   - If you use [LSP-pyright](https://packagecontrol.io/packages/LSP-pyright),
     configure the `python.analysis.extraPaths`:

     ```js
     {
         "settings": {
             "python.analysis.extraPaths": [
                 // add jfcherng-sublime/ST-API-stubs
                 "$packages/../st-stubs",
                 // the followings come from the default settings
                 "$sublime_py_files_dir",
                 "$packages",
             ],
         },
     }
     ```

1. Restart your ST and happy coding ♥

## Acknowledgment and related resources

This repository is initially mostly based on [AmjadHD/sublime_dev](https://github.com/AmjadHD/sublime_dev)'s work.

Apart from [@AmjadHD](https://github.com/AmjadHD)'s work, there are also some other similar works:

- https://github.com/sublimelsp/LSP/tree/master/stubs
- https://github.com/SublimeText/sublime_lib/tree/master/stubs

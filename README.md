# Sublime Text API Stubs

With LSP proper configured, you can have something like the following screenshot.

![LSP properly configured](https://raw.githubusercontent.com/jfcherng-sublime/ST-api-stubs/master/docs/with-lsp.png)

## How to use

Take the Python LSP server `pyls` as an example,

1. Clone (or copy) this repository into ST's `Data/` directory like [this](https://github.com/jfcherng-sublime/ST-my-settings/tree/210e269b56bc9a7903bf75d99fc799b28e0e25ee).

1. In the `LSP.sublime-settings`, add it into `pyls`'s `pyls.plugins.jedi.extra_paths` like [this](https://github.com/jfcherng-sublime/ST-my-settings/blob/210e269b56bc9a7903bf75d99fc799b28e0e25ee/Packages/User/LSP.sublime-settings#L45-L48):

   ```js
   {
       "clients": {
           "pyls": {
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

1. Restart your ST and happy coding ♥

## Acknowledgment and related resources

This repository is mostly based on [AmjadHD/sublime_dev](https://github.com/AmjadHD/sublime_dev)'s work.

Apart from [@AmjadHD](https://github.com/AmjadHD)'s work, there are also some other similar works:

- https://github.com/sublimelsp/LSP/tree/master/stubs
- https://github.com/SublimeText/sublime_lib/tree/master/stubs

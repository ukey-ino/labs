# Aim

To learn how use webpack

# Details

## Command Line History

* initialize

```
$ yarn init -yp
```

* install webpack

```
$ yarn add webpack webpack-cli --dev
```

* prepare files (The following has been omitted.)
```
$ touch src/index.js
$ touch src/modules/sub.js
```

* use webpack

```
$ npx webpack src/index.js
```

* deliverable

```
$ ls -l dist/
```

You can use dist/main.js as webpacked src/index.js.


* (Option) git settings

```
$ echo "node_modules" >> .gitignore
$ echo "dist" >> .gitignore
$ echo "yarn-error.log" >> .gitignore
```

* define npm scripts

```
$ vim package.json
$ yarn run build
```

* configuration

```
$ vim webpack.config.js
$ yarn run build
```

* use dev server

```
$ yarn add webpack webpack-cli webpack-dev-server --dev
$ vim package.json
$ vim webpack.config.js
$ yarn run start
```

* watch changing source code

```
$ vim package.json
$ yarn run watch
```

# Reference

* https://ics.media/entry/12140/


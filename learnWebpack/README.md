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
```

# Reference

* https://ics.media/entry/12140/


// gulpプラグインの読み込み
const gulp = require("gulp");
// Sassをコンパイルするプラグインの読み込み
const sass = require("gulp-sass");

gulp.task("default", function() {
  // 監視する
  return gulp.watch("css/style.scss", function() {
    // style.scssファイルを取得
    return (
      gulp
        .src("css/style.scss")
          // Sassのコンパイルを実行
          .pipe(sass({
            outputStyle: "expanded"
            })
            // sassのコンパイルエラーを表示する
            // (これがないと自動的に止まってしまう)
            .on("error", sass.logError)
          )
          // cssフォルダー以下に保存
          .pipe(gulp.dest("dist/css"))
    );
  });
});
